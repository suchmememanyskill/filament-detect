from filament import GenericFilament
from abc import abstractmethod

from reader.scan_result import ScanResult
from tag.tag_processor import TagProcessor

class TagAuthentication:
    def __init__(self, hkdf_key_a : list[list[int]], hkdf_key_b : list[list[int]]):
        self.hkdf_key_a = hkdf_key_a
        self.hkdf_key_b = hkdf_key_b

class MifareClassicTagProcessor(TagProcessor):
    def __init__(self, config : dict):
        super().__init__(config)
    
    @abstractmethod
    def authenticate_tag(self, scan_result : ScanResult) -> TagAuthentication:
        """Return a list of sector keys for authentication."""
        raise NotImplementedError("Subclasses must implement this method")