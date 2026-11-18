from abc import ABC, abstractmethod
from typing import Any, Protocol


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
            level = log.get("log_level")
            message = log.get("log_message")
            if level is not None and message is not None:
                entry = f"{level}: {message}"
            else:
                entry = ", ".join(f"{k}:{v}" for k, v in log.items())
            self._stack.append(entry)
            self._total += 1


class ExportPlugin(Protocol):
    def process_output(self, data: list[tuple[int, str]]) -> None:
        ...


class CSVExportPlugin:
    def _escape(self, value: str) -> str:
        if any(c in value for c in ',"\n'):
            return '"' + value.replace('"', '""') + '"'
        return value

    def process_output(self, data: list[tuple[int, str]]) -> None:
        print("CSV Output:")
        print(",".join(self._escape(value) for _, value in data))


class JSONExportPlugin:
    def _escape(self, value: str) -> str:
        return (value.replace("\\", "\\\\")
                     .replace('"', '\\"')
                     .replace("\n", "\\n"))

    def process_output(self, data: list[tuple[int, str]]) -> None:
        print("JSON Output:")
        items = ", ".join(f'"item_{rank}": "{self._escape(value)}"'
                          for rank, value in data)
        print("{" + items + "}")


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

    def output_pipeline(self, nb: int, plugin: ExportPlugin) -> None:
        for proc in self._processors:
            data: list[tuple[int, str]] = []
            for _ in range(nb):
                try:
                    data.append(proc.output())
                except Ingest_Error:
                    break
            if data:
                plugin.process_output(data)


if __name__ == "__main__":
    print("=== Code Nexus - Data Pipeline ===")
    print("Initialize Data Stream...")
    stream = DataStream()
    stream.print_processors_stats()

    print("Registering Processors")
    stream.register_processor(NumericProcessor())
    stream.register_processor(TextProcessor())
    stream.register_processor(LogProcessor())

    batch1 = [
        'Hello world',
        [3.14, -1, 2.71],
        [{'log_level': 'WARNING',
          'log_message': 'Telnet access! Use ssh instead'},
         {'log_level': 'INFO', 'log_message': 'User wil is connected'}],
        42,
        ['Hi', 'five'],
    ]
    print(f"Send first batch of data on stream: {batch1}")
    stream.process_stream(batch1)
    stream.print_processors_stats()

    print("Send 3 processed data from each processor to a CSV plugin:")
    stream.output_pipeline(3, CSVExportPlugin())
    stream.print_processors_stats()

    batch2 = [
        21,
        ['I love AI', 'LLMs are wonderful', 'Stay healthy'],
        [{'log_level': 'ERROR', 'log_message': '500 server crash'},
         {'log_level': 'NOTICE',
          'log_message': 'Certificate expires in 10 days'}],
        [32, 42, 64, 84, 128, 168],
        'World hello',
    ]
    print(f"Send another batch of data: {batch2}")
    stream.process_stream(batch2)
    stream.print_processors_stats()

    print("Send 5 processed data from each processor to a JSON plugin:")
    stream.output_pipeline(5, JSONExportPlugin())
    stream.print_processors_stats()