from abc import abstractmethod
from reader.rfid_reader import RfidReader
from reader.scan_result import ScanResult

class MifareUltralightReader(RfidReader):
    def __init__(self, config: dict):
        super().__init__(config)

    @abstractmethod
    def read_mifare_ultralight(self, scan_result : ScanResult) -> bytes|None:
        """Reads data from a Mifare Ultralight tag."""
        raise NotImplementedError("Subclasses must implement this method")