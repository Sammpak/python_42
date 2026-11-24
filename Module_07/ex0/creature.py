from abc import ABC, abstractmethod


class Creature(ABC):
    def __init__(self, name: str, type_crea: str) -> None:
        self._name = name
        self._type = type_crea

    def describe(self) -> None:
        print(f"{self._name} is a {self._type} type creature")

    @abstractmethod
    def attack(self) -> None:
        pass


class Flameling(Creature):
    def attack(self) -> None:
        print(f"{self._name} uses Flamethrower")


class Pyrodon(Creature):
    def attack(self) -> None:
        print(f"{self._name} uses Super attack")


class Aquabub(Creature):
    def attack(self) -> None:
        print(f"{self._name} uses Water Gun!")


class Torragon(Creature):
    def attack(self) -> None:
        print(f"{self._name} uses Hydro Pump!")
