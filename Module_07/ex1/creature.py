from ex0.creature import Creature
from .capabilities import HealCapability, TransformCapability


class Sproutling(Creature, HealCapability):
    def heal(self) -> None:
        print(f"{self._name} heals itself for a small amount")

    def attack(self) -> None:
        print(f"{self._name} is using Vine Whip")


class Bloomelle(Creature, HealCapability):
    def heal(self) -> None:
        print(f"{self._name} is healing")

    def attack(self) -> None:
        print(f"{self._name} uses Petal Dance!")


class Shiftling(Creature, TransformCapability):
    def __init__(self, name: str, type_crea: str,
                 is_transformed: bool = False) -> None:
        super().__init__(name, type_crea)
        self._is_transformed = is_transformed

    def transform(self) -> None:
        print(f"{self._name} shifts into a sharper form!")
        self._is_transformed = True

    def revert(self) -> None:
        print(f"{self._name} returns to normal.")
        self._is_transformed = False

    def attack(self) -> None:
        if self._is_transformed:
            print(f"{self._name} performs a boosted strike")
        else:
            print(f"{self._name} attacks normally")


class Morphagon(Creature, TransformCapability):
    def __init__(self, name: str, type_crea: str,
                 is_transformed: bool = False) -> None:
        super().__init__(name, type_crea)
        self._is_transformed = is_transformed

    def transform(self) -> None:
        print(f"{self._name} morphs into a dragonic battle form!")
        self._is_transformed = True

    def revert(self) -> None:
        print(f"{self._name} stabilizes its form")
        self._is_transformed = False

    def attack(self) -> None:
        if self._is_transformed:
            print(f"{self._name} unleashes a devastating morph strike")
        else:
            print(f"{self._name} attacks normally")
