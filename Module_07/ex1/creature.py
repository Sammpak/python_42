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


class HealCapability(ABC):
    def __init__(self, target: str):
        self._target = target
        super().__init__()

    @abstractmethod
    def heal(self) -> None:
        pass


class TransformCapability(ABC):
    def __init__(self, is_tranformed: bool):
        self._is_tranformed = is_tranformed
        super().__init__()

    @abstractmethod
    def revert(self) -> None:
        pass

    @abstractmethod
    def transform(self) -> None:
        pass


class Sproutling(Creature, HealCapability):
    def __init__(self, name: str, type_crea: str):
        super().__init__(name, type_crea)

    def heal(self) -> None:
        print(f"{self._name} heals itself for a small amount")

    def attack(self) -> None:
        print(f"{self._name} is using Vine Whip")


class Bloomelle(Creature, HealCapability):
    def __init__(self, name: str, type_crea: str):
        super().__init__(name, type_crea)

    def heal(self) -> None:
        print("bloomelle is healing")

    def attack(self) -> None:
        print(f"{self._name} use Petal Dance!")


class Shiftling(Creature, TransformCapability):
    def __init__(self, name: str, type_crea: str):
        super().__init__(name, type_crea)

    def revert(self) -> None:
        print("shifling is reverting")

    def transform(self) -> None:
        print("shifling is transforming")

    def attack(self) -> None:
        print(f"{self._name} attack normal")


class Morphagon(Creature, TransformCapability):
    def __init__(self, name: str, type_crea: str):
        super().__init__(name, type_crea)

    def revert(self) -> None:
        print("morphagon is reverting")

    def transform(self) -> None:
        print("morphagon is transforming")


class HealingCreatureFactory(CreatureFactory):
    def create_base(self) -> Creature:
        return Sproutling("Sproutling", "grass")

    def create_evolved(self) -> Creature:
        return Bloomelle("Bloomelle", "Grass/Fairy")


class TransformCreatureFactory(CreatureFactory):
    def create_base(self) -> Creature:
        return Shiftling("Shiftling", "normal")

    def create_evolved(self) -> Creature:
        return Morphagon()
