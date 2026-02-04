from config import ConfigurableEntity, TYPE_EXPORTER
from abc import abstractmethod

from filament.generic import GenericFilament
from reader.scan_result import ScanResult


class Exporter(ConfigurableEntity):
    def __init__(self, config: dict):
        super().__init__(config, TYPE_EXPORTER)

    def export_data(self, scan: ScanResult, filament: GenericFilament):
        """Exports the given filament data associated with a scan result."""
        raise NotImplementedError("Subclasses must implement this method")