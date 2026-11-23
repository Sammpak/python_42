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
    def __init__(self, name: str, type_crea: str) -> None:
        return super().__init__(name, type_crea)

    def describe(self) -> None:
        return super().describe()

    def attack(self) -> None:
        print(f"{self._name} use Flamethrower")


class Pyrodon(Creature):
    def __init__(self, name: str, type_crea: str) -> None:
        return super().__init__(name, type_crea)

    def describe(self) -> None:
        return super().describe()

    def attack(self) -> None:
        print(f"{self._name} uses Super attack")


class Aquabub(Creature):
    def __init__(self, name: str, type_crea: str) -> None:
        return super().__init__(name, type_crea)

    def describe(self) -> None:
        return super().describe()

    def attack(self) -> None:
        print(f"{self._name} uses Water Gun!")


class Torragon(Creature):
    def __init__(self, name: str, type_crea: str) -> None:
        return super().__init__(name, type_crea)

    def describe(self) -> None:
        return super().describe()

    def attack(self) -> None:
        print(f"{self._name} uses Hydro Pump!")


class CreatureFactory(ABC):

    @abstractmethod
    def create_base(self) -> Creature:
        pass

    @abstractmethod
    def create_evolved(self) -> Creature:
        pass


class FlameFactory(CreatureFactory):

    def create_base(self) -> Creature:
        return Torragon("toragon", "Fire")

    def create_evolved(self) -> Creature:
        return Flameling("flameling", "Fire")


class AquaFactory(CreatureFactory):
    def create_base(self) -> Creature:
        return Aquabub("Aquabub", "Water")

    def create_evolved(self) -> Creature:
        return Torragon("Torragon", "Water")


def fight(mob1: Creature, mob2: Creature) -> None:
    mob1.describe()
    print("vs.")
    mob2.describe()
    print("fight!")
    mob1.attack()
    mob2.attack()
