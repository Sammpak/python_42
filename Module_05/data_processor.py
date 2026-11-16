from abc import ABC, abstractmethod
from typing import Any


class DataProcessor(ABC):

    @abstractmethod
    def validate(self, data: Any) -> bool:
        return True

    @abstractmethod
    def ingest(self, data: Any) -> None:
        pass

    def output(self) -> tuple[int, str]:
        return (0, "0")


# int, float, set, list
class NumericProcessor(DataProcessor):
    def __init__(self) -> None:
        self._stack: list[str] = []

    def validate(self, data) -> bool:
        # bool
        if (isinstance(data, bool)):
            print("ko")
            return False
        # int & float
        elif (isinstance(data, int) or isinstance(data, float)):
            print("ok")
            return True
        # tuple int & float
        elif (isinstance(data, tuple) or isinstance(data, list)):
            print("tuple or list")
            for nbr in data:
                if (isinstance(nbr, bool)):
                    print("ko")
                    return False
                if (not isinstance(nbr, int) and not isinstance(nbr, float)):
                    print("ko")
                    return False
            print("ok")
            return True

    # convert to str and store in list ig
    def ingest(self, data: Any) -> None:
        print("ingesting")
        # int & float
        if (isinstance(data, int) or isinstance(data, float)):
            self._stack.append(str(data))
            print(f"{self._stack}")
        elif (isinstance(data, tuple) or isinstance(data, list)):
            print("list or tupple")
            for nbr in data:
                self._stack.append(str(nbr))
            print(f"{self._stack}")


    def output(self) -> tuple[int, str]:
        pass


if __name__ == "__main__":
    print("=== Code Nexus - Data Processor ===")

    print("Testing Numeric Processor...")
    nume_process = NumericProcessor()
    # int
    nume_process.validate(42)
    # float
    nume_process.validate(-2.5)
    # bool
    nume_process.validate(True)
    # tuple
    nume_process.validate((1, 2, 3, 4, 0.4, 1))
    # str
    nume_process.validate("je suis un nbr trust")
    # list
    nume_process.validate([1, 2, 3, 4, 0.6, 1])
    nume_process.ingest([1, 2, 3, 4, 0.6, 1])
    nume_process.ingest(12)