from abc import ABC, abstractmethod
from typing import Any

class Ingest_Error(Exception):
    def __init__(self, message: str = "Unknown ingest error") -> None:
        self.message = message
        super().__init__(self.message)

class DataProcessor(ABC):
    def __init__(self) -> None:
        self._stack: list[str] = []
        self._rank: int = 0

    @abstractmethod
    def validate(self, data: Any) -> bool:
        return True

    @abstractmethod
    def ingest(self, data: Any) -> None:
        pass

    def output(self) -> list[tuple[int, str]]:
        if not self._stack:
            raise Ingest_Error("Empty stack")
        else:
            res: list[tuple[int, str]] = []
            for i, value in enumerate(self._stack):
                res.append((i, value))
            return res

# int, float, set, list
class NumericProcessor(DataProcessor):
    def __init__(self) -> None:
        super().__init__()

    def validate(self, data) -> bool:
        # bool
        if (isinstance(data, bool)):
            return False
        # int & float
        elif (isinstance(data, int) or isinstance(data, float)):
            return True
        # tuple int & float
        elif (isinstance(data, tuple) or isinstance(data, list)):
            for nbr in data:
                if (isinstance(nbr, bool)):
                    return False
                if (not isinstance(nbr, int) and not isinstance(nbr, float)):
                    return False
            return True
        else:
            return False

    # convert to str and store in list ig
    def ingest(self, data: Any) -> None:
        try:
            if (self.validate(data)):
                # int & float
                if (isinstance(data, int) or isinstance(data, float)):
                    self._stack.append(str(data))
                    print(f"{self._stack}")
                elif (isinstance(data, tuple) or isinstance(data, list)):
                    for nbr in data:
                        self._stack.append(str(nbr))
            else:
                raise Ingest_Error("Improper numeric data")
        except (Ingest_Error, Exception) as e:
            print(f"Got exception: {e}")

    def output(self) -> list[tuple[int, str]]:
        res = super().output()
        for rank, value in res:
            print(f"Numeric value {rank}: {value}")
        return res
    
# list
class TextProcessor(DataProcessor):
    def __init__(self) -> None:
        super().__init__()

    # str, list, set
    def validate(self, data) -> bool:
        if (isinstance(data, str)):
            return True
        elif (isinstance(data, tuple) or isinstance(data, list)):
            for c in data:
                if (not isinstance(c, str)):
                    return False
            return True
        else:
            return False

    def ingest(self, data: Any) -> None:
        try:
            if (self.validate(data)):
                if (isinstance(data, str)):
                    self._stack.append(data)
                elif (isinstance(data, tuple) or isinstance(data, list)):
                    for c in data:
                        self._stack.append(c)
            else:
                raise Ingest_Error("Improper numeric data")
        except (Ingest_Error, Exception) as e:
            print(f"Got exception: {e}")

    def output(self) -> list[tuple[int, str]]:
        res = super().output()
        for rank, value in res:
            print(f"Text value {rank}: {value}")
        return res
    
# dict, list
class LogProcessor(DataProcessor):
    def __init__(self) -> None:
        super().__init__()

    def validate(self, data) -> bool:
        if (isinstance(data, dict)):
            return True
        elif (isinstance(data, list)):
            for nbr in data:
                if (not isinstance(nbr, dict)):
                    return False
            return True
        return False

    def ingest(self, data: dict[str, str]) -> None:
        if not self.validate(data):
            raise Ingest_Error("Improper log data")
        if isinstance(data, dict):
            data = [data]
        for log in data:
            entry = ", ".join(f"{key}:{value}" for key, value in log.items())
            self._stack.append(entry)


    def output(self) -> list[tuple[int, str]]:
        res = super().output()
        for rank, value in res:
            print(f"Text value {rank}: {value}")
        return res

if __name__ == "__main__":
    print("=== Code Nexus - Data Processor ===")

    print("Testing Numeric Processor...")
    nume_process = NumericProcessor()
    print(f"Trying to validate input '42': {nume_process.validate(42)}")
    print(f"Trying to validate input 'hello': {nume_process.validate("hello")}")
    print(f"Trying to validate input 'True': {nume_process.validate(True)}")

    print("Test invalid ingestion of string 'foo' without prior validation:")
    nume_process.ingest("foo")

    print(f"Processing data: {[1, 2, 3, 4, 5]}")
    nume_process.ingest([1, 2, 3, 4, 5])

    res = nume_process.output()

    print(" ")
    text_process = TextProcessor()
    print("Testing Text Processor...")
    print(f"Trying to validate input '42': {text_process.validate(42)}")

    print("Processing data: ['Hello', 'Nexus', 'World']")
    text_process.ingest(['Hello', 'Nexus', 'World'])
    text_process.output()

    print(" ")
    print("Testing Log Processor...")
    log_process = LogProcessor()
    print(f"Trying to validate input 'Hello': {log_process.validate('Hello')}")

    print("Processing data: [{'log_level': 'NOTICE', 'log_message': 'Connection to server'}, {'log_level': 'ERROR', 'log_message': 'Unauthorized access!!'}]")
    log_process.ingest([{'log_level': 'NOTICE', 'log_message': 'Connection to server'}, {'log_level': 'ERROR', 'log_message': 'Unauthorized access!!'}])
    log_process.output()