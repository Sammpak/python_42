from pydantic import BaseModel, Field, ValidationError, field_validator
from datetime import datetime
from typing import Optional


class SpaceStation(BaseModel):
    station_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=1, max_length=50)
    crew_size: int = Field(ge=1, le=20)
    power_level: float = Field(ge=0.0, le=100.0)
    oxygen_level: float = Field(ge=0.0, le=100.0)
    last_maintenance: datetime
    is_operational: bool = Field(default=True)
    notes: Optional[str] = Field(default=None, max_length=200)

    def show(self) -> None:
        print(f"ID: {self.station_id}")
        print(f"Name: {self.name}")
        print(f"Crew: {self.crew_size}")
        print(f"Power: {self.power_level}")
        print(f"Oxygen: {self.oxygen_level}%")
        print(f"Status: {self.last_maintenance}%")
        print(f"Is Op: {self.is_operational}")
        if (self.notes is not None):
            print(f"Note: {self.notes}")


if __name__ == "__main__":
    print("Space Station Data Validation")
    print("========================================")
    print("Valid station created:")
    station = SpaceStation(
        station_id="ISS-01",
        name="Orbital Outpost Alpha",
        crew_size=6,
        power_level=94.5,
        oxygen_level=99.2,
        last_maintenance=datetime.now(),
    )
    station.show()
    print()
    print("========================================")
    print("Expected validation error:")
    try:
        station = SpaceStation(
            station_id="aaaaaaaaaaaaaaaaaaaaaaaaaaa",
            name="Orbital Outpost Alpha",
            crew_size=6,
            power_level=94.5,
            oxygen_level=99.2,
            last_maintenance=datetime.now(),
        )
    except ValidationError as e:
        print(e.errors()[0]["msg"])