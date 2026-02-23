from filament import GenericFilament
from abc import abstractmethod
import hashlib

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
    def authenticate_tag(self, scan_result : ScanResult) -> TagAuthentication|None:
        """Return a list of sector keys for authentication."""
        raise NotImplementedError("Subclasses must implement this method")
    
    def load_key_from_config(self, key_name : str = "key") -> str|None:
        key = self.config.get(key_name, None)
        if not key:
            return None
    
        return key

    def load_text_key_from_config(self, expected_hash : str, key_name : str = "key") -> str|None:
        key = self.load_key_from_config(key_name)
        if not key:
            return None
        
        key_hash = hashlib.sha256(key.encode('utf-8')).hexdigest()
        if key_hash.lower() != expected_hash.lower():
            return None
        
        return key
    
    def load_hex_key_from_config(self, expected_hash : str, key_name : str = "key") -> bytes|None:
        key_str = self.load_key_from_config(key_name)
        if not key_str:
            return None
        
        try:
            key_bytes = bytes.fromhex(key_str.upper())
        except ValueError:
            return None
        
        key_hash = hashlib.sha256(key_bytes).hexdigest()
        if key_hash.lower() != expected_hash.lower():
            return None
        
        return key_bytes