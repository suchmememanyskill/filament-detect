
from bus import OutputPin, SoftwareSPI
from config import register_configurable_entity
from reader.fm175xx.rfid import Fm175xx
from reader.gpio_enabled_rfid_reader import GpioEnabledRfidReader
import time
import logging
import requests

from reader.mifare_classic_reader import MifareClassicReader
from reader.mifare_ultralight_reader import MifareUltralightReader
from tag.anycubic.processor import AnycubicTagProcessor
from tag.bambu.processor import BambuTagProcessor
from tag.creality.processor import CrealityTagProcessor
from tag.mifare_classic_tag_processor import MifareClassicTagProcessor
from tag.mifare_ultralight_tag_processor import MifareUltralightTagProcessor
from tag.openspool.processor import OpenspoolTagProcessor
from tag.snapmaker.processor import SnapmakerTagProcessor
from tag.tag_types import TagType

logging.basicConfig(level=logging.DEBUG)

rf_1_pin = OutputPin({
    "__name": "rf_1_pin",
    "gpio_device": 1,
    "line": 27
})

rf_2_pin = OutputPin({
    "__name": "rf_2_pin",
    "gpio_device": 1,
    "line": 24
})

fm175_1_reset_pin = OutputPin({
    "__name": "fm175_1_reset_pin",
    "gpio_device": 1,
    "line": 25
})

fm175_2_reset_pin = OutputPin({
    "__name": "fm175_2_reset_pin",
    "gpio_device": 1,
    "line": 28
})

software_spi_1 = SoftwareSPI({
    "__name": "software_spi_1",
    "bus": 2,
    "device": 0,
    "max_speed_hz": 500000,
    "mode": 0
})

software_spi_2 = SoftwareSPI({
    "__name": "software_spi_2",
    "bus": 2,
    "device": 1,
    "max_speed_hz": 500000,
    "mode": 0
})

register_configurable_entity(rf_1_pin)
register_configurable_entity(rf_2_pin)
register_configurable_entity(fm175_1_reset_pin)
register_configurable_entity(fm175_2_reset_pin)
register_configurable_entity(software_spi_1)
register_configurable_entity(software_spi_2)

fm175_1 = Fm175xx({
    "__name": "fm175_1",
    "spi": "software_spi_1",
    "reset_pin": "fm175_1_reset_pin"
})

fm175_2 = Fm175xx({
    "__name": "fm175_2",
    "spi": "software_spi_2",
    "reset_pin": "fm175_2_reset_pin"
})

register_configurable_entity(fm175_1)
register_configurable_entity(fm175_2)

gpio_enabled_rfid_reader_1 = GpioEnabledRfidReader({
    "__name": "gpio_enabled_rfid_reader_1",
    "rfid_reader": "fm175_1",
    "gpio_pins_high": ["rf_1_pin"],
    "gpio_pins_low": ["rf_2_pin"],
    "slot": 2,
})

gpio_enabled_rfid_reader_2 = GpioEnabledRfidReader({
    "__name": "gpio_enabled_rfid_reader_1_mode_2",
    "rfid_reader": "fm175_1",
    "gpio_pins_high": ["rf_2_pin"],
    "gpio_pins_low": ["rf_1_pin"],
    "slot": 3,
})

gpio_enabled_rfid_reader_3 = GpioEnabledRfidReader({
    "__name": "gpio_enabled_rfid_reader_2",
    "rfid_reader": "fm175_2",
    "gpio_pins_high": ["rf_1_pin"],
    "gpio_pins_low": ["rf_2_pin"],
    "slot": 0,
})

gpio_enabled_rfid_reader_4 = GpioEnabledRfidReader({
    "__name": "gpio_enabled_rfid_reader_2_mode_2",
    "rfid_reader": "fm175_2",
    "gpio_pins_high": ["rf_2_pin"],
    "gpio_pins_low": ["rf_1_pin"],
    "slot": 1,
})

register_configurable_entity(gpio_enabled_rfid_reader_1)
register_configurable_entity(gpio_enabled_rfid_reader_2)
register_configurable_entity(gpio_enabled_rfid_reader_3)
register_configurable_entity(gpio_enabled_rfid_reader_4)

readers = [
    gpio_enabled_rfid_reader_1,
    gpio_enabled_rfid_reader_2,
    gpio_enabled_rfid_reader_3,
    gpio_enabled_rfid_reader_4
]

mifare_classic_processors : list[MifareClassicTagProcessor] = [
    SnapmakerTagProcessor(),
    BambuTagProcessor(),
    CrealityTagProcessor(),
]

mifare_ultralight_processors : list[MifareUltralightTagProcessor] = [
    OpenspoolTagProcessor(),
    AnycubicTagProcessor(),
]

while True:
    snapmaker_tag_processor = SnapmakerTagProcessor()
    for reader in readers:
        logging.debug(f"Starting scan with reader: {reader.name}")
        reader.start_session()
        scan_result = reader.scan()
        reader.end_session()
        if scan_result is not None:
            parsed_data = None
            logging.info(scan_result.pretty_text())
            if scan_result.tag_type == TagType.MifareClassic1k and isinstance(reader, MifareClassicReader):
                read = False
                for processor in mifare_classic_processors:
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
                        parsed_data = processor.process_tag(scan_result, card_data)
                        break
                    else:
                        logging.warning("Failed to read MIFARE Classic card data")
                        continue
            elif scan_result.tag_type == TagType.MifareUltralight and isinstance(reader, MifareUltralightReader):
                reader.start_session()

                if reader.scan() == None:
                    logging.warning("Tag lost before reading")
                    reader.end_session()
                    continue

                card_data = reader.read_mifare_ultralight(scan_result)
                reader.end_session()

                if card_data is not None:
                    logging.debug(f"Read MIFARE Ultralight card data: {card_data.hex().upper()}")

                    for processor in mifare_ultralight_processors:
                        logging.debug(f"Attempting to read with processor: {processor.name}")
                        parsed_data = processor.process_tag(scan_result, card_data)

                        if parsed_data is not None:
                            break
                else:
                    logging.warning("Failed to read MIFARE Ultralight card data")
            else:
                logging.warning("Failed to find compatible reader for tag type %s", scan_result.tag_type.name)

            if parsed_data is not None:
                logging.info(parsed_data.pretty_text())
                logging.debug(f"Parsed filament data")

                requests.post("http://localhost/printer/gcode/script", json={
                    "script": f"SET_PRINT_FILAMENT_CONFIG CONFIG_EXTRUDER={reader.slot} FILAMENT_TYPE={parsed_data.type} FILAMENT_SUBTYPE=\"{' '.join(parsed_data.modifiers)}\" VENDOR=\"{parsed_data.manufacturer}\" FILAMENT_COLOR_RGBA={parsed_data.rgba:08X} FILAMENT_SPOOL_ID=test"
                })
                
    time.sleep(1)