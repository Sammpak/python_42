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
        self._total: int = 0
        self._name: str = "Data Processor"

    @abstractmethod
    def validate(self, data: Any) -> bool:
        return True

    @abstractmethod
    def ingest(self, data: Any) -> None:
        pass

    def output(self) -> tuple[int, str]:
        if not self._stack:
            raise Ingest_Error("Empty stack")
        value = self._stack.pop(0)
        rank = self._rank
        self._rank += 1
        return (rank, value)

    def statistic(self) -> None:
        print(f"{self._name}: total {self._total} items processed, "
              f"remaining {len(self._stack)} on processor")


# int, float, list/tuple of int & float
class NumericProcessor(DataProcessor):
    def __init__(self) -> None:
        super().__init__()
        self._name = "Numeric Processor"

    def validate(self, data: Any) -> bool:
        if isinstance(data, bool):
            return False
        if isinstance(data, (int, float)):
            return True
        if isinstance(data, (tuple, list)):
            for nbr in data:
                if isinstance(nbr, bool):
                    return False
                if not isinstance(nbr, (int, float)):
                    return False
            return True
        return False

    def ingest(self, data: Any) -> None:
        if not self.validate(data):
            raise Ingest_Error("Improper numeric data")
        if isinstance(data, (int, float)):
            data = [data]
        for nbr in data:
            self._stack.append(str(nbr))
            self._total += 1

    def output(self) -> tuple[int, str]:
        rank, value = super().output()
        print(f"Numeric value {rank}: {value}")
        return (rank, value)


# str, list/tuple of str
class TextProcessor(DataProcessor):
    def __init__(self) -> None:
        super().__init__()
        self._name = "Text Processor"

    def validate(self, data: Any) -> bool:
        if isinstance(data, str):
            return True
        if isinstance(data, (tuple, list)):
            for c in data:
                if not isinstance(c, str):
                    return False
            return True
        return False

    def ingest(self, data: Any) -> None:
        if not self.validate(data):
            raise Ingest_Error("Improper text data")
        if isinstance(data, str):
            data = [data]
        for c in data:
            self._stack.append(c)
            self._total += 1

    def output(self) -> tuple[int, str]:
        rank, value = super().output()
        print(f"Text value {rank}: {value}")
        return (rank, value)


# dict, list of dict
class LogProcessor(DataProcessor):
    def __init__(self) -> None:
        super().__init__()
        self._name = "Log Processor"

    def validate(self, data: Any) -> bool:
        if isinstance(data, dict):
            return True
        if isinstance(data, list):
            for log in data:
                if not isinstance(log, dict):
                    return False
            return True
        return False

    def ingest(self, data: Any) -> None:
        if not self.validate(data):
            raise Ingest_Error("Improper log data")
        if isinstance(data, dict):
            data = [data]
        for log in data:
            entry = ", ".join(f"{key}:{value}" for key, value in log.items())
            self._stack.append(entry)
            self._total += 1

    def output(self) -> tuple[int, str]:
        rank, value = super().output()
        print(f"Log entry {rank}: {value}")
        return (rank, value)


class DataStream:
    def __init__(self) -> None:
        self._processors: list[DataProcessor] = []

    def register_processor(self, proc: DataProcessor) -> None:
        self._processors.append(proc)

    def process_stream(self, stream: list[Any]) -> None:
        for element in stream:
            for proc in self._processors:
                if proc.validate(element):
                    proc.ingest(element)
                    break
            else:
                print("DataStream error - Can't process element in "
                      f"stream: {element}")

    def print_processors_stats(self) -> None:
        print("== DataStream statistics ==")
        if not self._processors:
            print("No processor found, no data")
            return
        for proc in self._processors:
            proc.statistic()


if __name__ == "__main__":
    print("=== Code Nexus - Data Stream ===")
    print("Initialize Data Stream...")
    stream = DataStream()

    print("Registering Numeric Processor")
    numeric = NumericProcessor()
    stream.register_processor(numeric)
    batch = ['Hello world', [3.14, -1, 2.71], [{'log_level': 'WARNING'}], 42, ['Hi', 'five']]
    stream.process_stream(batch)

    print("== DataStream statistics ==")
    stream.print_processors_stats()

    print("")
    print("Registering other data processors")
    log_Processor = LogProcessor()
    str_processor = TextProcessor()
    stream.register_processor(log_Processor)
    stream.register_processor(str_processor)
    print("sending the same batch again")
    batch = ['Hello world', [3.14, -1, 2.71], [{'log_level': 'WARNING'}], 42, ['Hi', 'five']]
    stream.process_stream(batch)
    print("== DataStream statistics ==")
    stream.print_processors_stats()

    print("Consume some elements from the data processors: "
          "Numeric 3, Text 2, Log 1")
    for _ in range(3):
        numeric.output()
    for _ in range(2):
        str_processor.output()
    log_Processor.output()
    stream.print_processors_stats()
