from abc import ABC, abstractmethod


class HealCapability(ABC):
    @abstractmethod
    def heal(self) -> None:
        pass


class TransformCapability(ABC):
    @abstractmethod
    def revert(self) -> None:
        pass

    @abstractmethod
    def transform(self) -> None:
        pass
