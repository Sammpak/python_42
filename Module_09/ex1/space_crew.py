from datetime import datetime
from enum import Enum
from typing import Self
from pydantic import BaseModel, Field, ValidationError, model_validator


class Rank(str, Enum):
    COMMANDER = "Commander"
    PILOT = "Pilot"
    SPECIALIST = "Specialist"
    CADET = "Cadet"
    CAPTAIN = "Captain"
    LIEUTENANT = "Lieutenant"


class Crew(BaseModel):
    member_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=2, max_length=50)
    rank: Rank
    age: int = Field(ge=18, le=80)
    specialisation: str = Field(min_length=3, max_length=30)
    years_experience: int = Field(ge=0, le=50)
    is_active: bool = Field(default=True)


class SpaceMission(BaseModel):
    mission_id: str = Field(min_length=5, max_length=15)
    mission_name: str = Field(min_length=3, max_length=100)
    destination: str = Field(min_length=3, max_length=50)
    launch_date: datetime
    duration_days: int = Field(ge=1, le=3650)
    crew: list[Crew] = Field(min_length=1, max_length=12)
    mission_status: str = Field(default="planned")
    budget_millions: float = Field(ge=1, le=10000)

    def show(self) -> None:
        print(f"Mission: {self.mission_name}")
        print(f"ID: {self.mission_id}")
        print(f"Destination: {self.destination}")
        print(f"Duration: {self.duration_days} days")
        print(f"Budget: ${self.budget_millions:.1f}M")
        print(f"Crew size: {len(self.crew)}")
        for c in self.crew:
            print(f"- {c.name} ({c.rank.value}) - {c.specialisation}")

    @model_validator(mode="after")
    def check_mission(self) -> Self:
        if not self.mission_id.startswith("M"):
            raise ValueError("Mission ID doesn't start with 'M'")
        return self

    @model_validator(mode="after")
    def check_commander(self) -> Self:
        if not any(c.rank in (Rank.COMMANDER, Rank.CAPTAIN) for c in self.crew):
            raise ValueError("Mission requires at least one Commander or Captain")
        return self

    @model_validator(mode="after")
    def check_long_mission(self) -> Self:
        if self.duration_days > 365:
            experienced_count = sum(1 for c in self.crew if c.years_experience > 5)
            if (experienced_count / len(self.crew)) < 0.5:
                raise ValueError("Long missions (>365 days) require at least 50% experienced crew (>5 yrs)")
        return self

    @model_validator(mode="after")
    def crew_active_check(self) -> Self:
        if any(not c.is_active for c in self.crew):
            raise ValueError("All crew members must be active")
        return self


if __name__ == "__main__":
    sarah = Crew(
        member_id="001",
        name="Sarah Connor",
        rank=Rank.COMMANDER,
        age=28,
        specialisation="Navigation",
        years_experience=6,
        is_active=True
    )

    john = Crew(
        member_id="002",
        name="John Smith",
        rank=Rank.LIEUTENANT,
        age=30,
        specialisation="Mission command",
        years_experience=7,
        is_active=True
    )

    alice = Crew(
        member_id="003",
        name="Alice Johnson",
        rank=Rank.CADET,
        age=26,
        specialisation="Morale Officer",
        years_experience=2,
        is_active=True
    )

    mission_1 = SpaceMission(
        mission_id="M2024_MARS",
        mission_name="Mars Colony Establishment",
        destination="Mars",
        duration_days=900,
        budget_millions=2500,
        launch_date=datetime.now(),
        mission_status="GOOD",
        crew=[alice, john, sarah]
    )

    print("Space Mission Crew Validation")
    print("=========================================")
    mission_1.show()
    print()
    print("=========================================")
    print("Expected validation error:")
    try:
        mission_2 = SpaceMission(
            mission_id="B2024_MARS",
            mission_name="Mars Colony Establishment",
            destination="Mars",
            duration_days=900,
            budget_millions=2500,
            launch_date=datetime.now(),
            mission_status="GOOD",
            crew=[alice, jhon, sarah]
        )
    except ValidationError as e:
        print(e.errors()[0]["msg"])
