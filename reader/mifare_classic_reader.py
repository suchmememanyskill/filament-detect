from abc import abstractmethod
from reader.rfid_reader import RfidReader
from reader.scan_result import ScanResult
from tag.mifare_classic_tag_processor import TagAuthentication

class MifareClassicReader(RfidReader):
    def __init__(self, config: dict):
        super().__init__(config)

    @abstractmethod
    def read_mifare_classic(self, scan_result : ScanResult, keys: TagAuthentication) -> bytes|None:
        """Reads data from a Mifare Classic tag using the provided keys for authentication."""
        raise NotImplementedError("Subclasses must implement this method")