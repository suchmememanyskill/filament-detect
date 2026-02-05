from config import ConfigurableEntity, TYPE_EXPORTER
from abc import abstractmethod

from filament.generic import GenericFilament
from reader.rfid_reader import RfidReader
from reader.scan_result import ScanResult


class Exporter(ConfigurableEntity):
    def __init__(self, config: dict):
        super().__init__(config, TYPE_EXPORTER)

    @abstractmethod
    def export_data(self, scan: ScanResult|None, filament: GenericFilament|None, reader : RfidReader):
        """Exports the given filament data associated with a scan result. The scan and filament may be None if the export is triggered by a read error or unrecognized tag."""
        raise NotImplementedError("Subclasses must implement this method")