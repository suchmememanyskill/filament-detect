from reader.scan_result import ScanResult
from filament import GenericFilament
from config import ConfigurableEntity, TYPE_TAG_PROCESSOR

class TagProcessor(ConfigurableEntity):
    def __init__(self, config : dict):
        super().__init__(config, TYPE_TAG_PROCESSOR)
        
    def process_tag(self, scan_result : ScanResult, data : bytes) -> GenericFilament | None:
        """Process a scanned tag and its data, returning a GenericFilament if recognized, else None."""
        raise NotImplementedError("Subclasses must implement this method")