from config import ConfigurableEntity, register_configurable_entity, get_required_configurable_entity_by_name, TYPE_RUNTIME, TYPE_EXPORTER, TYPE_TAG_PROCESSOR, TYPE_RFID_READER
from bus import OutputPin, SoftwareSPI
from reader.fm175xx import Fm175xx
from reader.gpio_enabled_rfid_reader import GpioEnabledRfidReader
from tag.bambu import BambuTagProcessor
from tag.anycubic import AnycubicTagProcessor
from tag.creality import CrealityTagProcessor
from tag.openspool import OpenspoolTagProcessor
from tag.snapmaker import SnapmakerTagProcessor
from tag.tag_types import TagType
from tag.tag_processor import TagProcessor
from tag.mifare_classic_tag_processor import MifareClassicTagProcessor
from tag.mifare_ultralight_tag_processor import MifareUltralightTagProcessor
from reader.mifare_classic_reader import MifareClassicReader
from reader.mifare_ultralight_reader import MifareUltralightReader
from reader.rfid_reader import RfidReader
from exporters.webhook import WebhookExporter
from exporters.exporter import Exporter
from reader.scan_result import ScanResult
from filament import GenericFilament
from typing import cast
import time
import logging

class Runtime(ConfigurableEntity):
    def __init__(self, config : dict):
        config["__name"] = "runtime"
        super().__init__(config, "runtime")

        self.auto_read_mode = bool(config.get("auto_read_mode", False))

        self.readers : list[RfidReader] = [cast(RfidReader, get_required_configurable_entity_by_name(name, TYPE_RFID_READER)) for name in config.get("readers", [])]
        self.tag_processors : list[TagProcessor] = [cast(TagProcessor, get_required_configurable_entity_by_name(name, TYPE_TAG_PROCESSOR)) for name in config.get("tag_processors", [])]
        self.exporters : list[Exporter] = [cast(Exporter, get_required_configurable_entity_by_name(name, TYPE_EXPORTER)) for name in config.get("exporters", [])]

        self.mifare_classic_processors = [processor for processor in self.tag_processors if isinstance(processor, MifareClassicTagProcessor)]
        self.mifare_ultralight_processors = [processor for processor in self.tag_processors if isinstance(processor, MifareUltralightTagProcessor)]

        self.read_requested = [False] * len(self.readers)

    def loop(self):
        while True:
            for i, reader in enumerate(self.readers):
                if self.auto_read_mode or self.read_requested[i]:
                    result = self.process_reader_single(reader)

                    if result is not None:
                        scan_result, filament = result
                        logging.info(f"Processed tag with UID {scan_result.uid} into filament: {filament}")

                        for exporter in self.exporters:
                            exporter.export_data(scan_result, filament)

                        self.read_requested[i] = False

            time.sleep(1)
        
    def process_reader_single(self, reader: RfidReader) -> tuple[ScanResult, GenericFilament]|None:
        reader.start_session()
        scan_result = reader.scan()
        reader.end_session()
        if scan_result is None:
            logging.debug("No tag detected")
            return
        
        uid = scan_result.uid.hex()
        
        if self.auto_read_mode and reader.is_same_tag(uid):
            logging.debug("Same tag detected as last read, skipping processing")
            return
        
        logging.info(f"Detected tag type {scan_result.tag_type.name} with UID {scan_result.uid}")

        filament = None
        if scan_result.tag_type == TagType.MifareClassic1k and isinstance(reader, MifareClassicReader):
            filament = self.process_mifare_classic(reader, scan_result)
        elif scan_result.tag_type == TagType.MifareUltralight and isinstance(reader, MifareUltralightReader):
            filament = self.process_mifare_ultralight(reader, scan_result)
        
        if filament is None:
            logging.warning("Failed to read data from tag")
            return
        
        logging.info(filament.pretty_text())
        
        reader.set_last_read_uid(uid)
        return (scan_result, filament)

    def process_mifare_classic(self, reader: MifareClassicReader, scan_result: ScanResult) -> GenericFilament | None:
        for processor in self.mifare_classic_processors:
            reader.start_session()

            if reader.scan() == None:
                logging.warning("Tag lost before reading")
                reader.end_session()
                continue

            logging.debug(f"Attempting to read with processor: {processor.name}")
            auth = processor.authenticate_tag(scan_result)
            card_data = reader.read_mifare_classic(scan_result, auth)
            reader.end_session()

            if card_data is not None:
                logging.debug(f"Read MIFARE Classic card data: {card_data.hex().upper()}")
                return processor.process_tag(scan_result, card_data)
            else:
                logging.warning("Failed to read MIFARE Classic card data")
                continue

        return None
    
    def process_mifare_ultralight(self, reader: MifareUltralightReader, scan_result: ScanResult) -> GenericFilament | None:
        reader.start_session()

        if reader.scan() == None:
            logging.warning("Tag lost before reading")
            reader.end_session()
            return None

        card_data = reader.read_mifare_ultralight(scan_result)
        reader.end_session()

        if card_data is not None:
            logging.debug(f"Read MIFARE Ultralight card data: {card_data.hex().upper()}")

            for processor in self.mifare_ultralight_processors:
                logging.debug(f"Attempting to read with processor: {processor.name}")
                filament = processor.process_tag(scan_result, card_data)

                if filament is not None:
                    return filament
        else:
            logging.warning("Failed to read MIFARE Ultralight card data")

        return None

def consume_config(config: dict) -> Runtime:
    for key, value in config.items():
        configurable_entity = create_configurable_entity(key, value)
        register_configurable_entity(configurable_entity)

    return cast(Runtime, get_required_configurable_entity_by_name("runtime", TYPE_RUNTIME))

def create_configurable_entity(key: str, config: dict) -> ConfigurableEntity:
    key_split = key.split(" ", 2)
    name = key_split[1] if len(key_split) > 1 else key_split[0]
    config["__name"] = name

    match key_split[0]:
        case "runtime":
            return Runtime(config)
        case "output_pin":
            return OutputPin(config)
        case "software_spi":
            return SoftwareSPI(config)
        case "fm175xx":
            return Fm175xx(config)
        case "gpio_enabled_rfid_reader":
            return GpioEnabledRfidReader(config)
        case "bambu_lab_tag_processor":
            return BambuTagProcessor(config)
        case "anycubic_tag_processor":
            return AnycubicTagProcessor(config)
        case "creality_tag_processor":
            return CrealityTagProcessor(config)
        case "openspool_tag_processor":
            return OpenspoolTagProcessor(config)
        case "snapmaker_tag_processor":
            return SnapmakerTagProcessor(config)
        case "webhook_exporter":
            return WebhookExporter(config)
        case _:
            raise ValueError(f"Unknown configurable entity type: {key_split[0]}")