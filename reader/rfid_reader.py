from abc import abstractmethod
from config import ConfigurableEntity, TYPE_RFID_READER
from reader.scan_result import ScanResult

class RfidReader(ConfigurableEntity):
    def __init__(self, config : dict):
        super().__init__(config, TYPE_RFID_READER)
        self.name = config["__name"]
        self.use_reader = config.get("use_reader", True)

    @abstractmethod
    def start_session(self):
        raise NotImplementedError("Subclasses must implement this method")
    
    @abstractmethod
    def end_session(self):
        raise NotImplementedError("Subclasses must implement this method")

    @abstractmethod
    def scan(self) -> ScanResult | None:
        raise NotImplementedError("Subclasses must implement this method")