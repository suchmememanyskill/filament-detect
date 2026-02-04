from abc import abstractmethod
from config import ConfigurableEntity, TYPE_RFID_READER
from reader.scan_result import ScanResult

class RfidReader(ConfigurableEntity):
    def __init__(self, config : dict):
        super().__init__(config, TYPE_RFID_READER)
        self.name = config["__name"]
        self.use_reader = config.get("use_reader", True)
        self.slot = int(config.get("slot", 0))
        self.last_read_uid : str|None = None

    @abstractmethod
    def start_session(self):
        raise NotImplementedError("Subclasses must implement this method")
    
    @abstractmethod
    def end_session(self):
        raise NotImplementedError("Subclasses must implement this method")

    @abstractmethod
    def scan(self) -> ScanResult | None:
        raise NotImplementedError("Subclasses must implement this method")
    
    def is_same_tag(self, uid: str) -> bool:
        """Check if the given UID matches the last read UID."""
        return self.last_read_uid == uid
    
    def set_last_read_uid(self, uid: str):
        """Set the last read UID."""
        self.last_read_uid = uid