from abc import ABC, abstractmethod
from reader.scan_result import ScanResult
from filament import GenericFilament

class TagProcessor(ABC):
    def __init__(self, name: str):
        self.name = name

    def process_tag(self, scan_result : ScanResult, data : bytes) -> GenericFilament | None:
        """Process a scanned tag and its data, returning a GenericFilament if recognized, else None."""
        raise NotImplementedError("Subclasses must implement this method")