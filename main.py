
from bus import OutputPin, SoftwareSPI
from config import register_configurable_entity
from reader.fm175xx.rfid import Fm175xx
from reader.gpio_enabled_rfid_reader import GpioEnabledRfidReader
import time
import logging
import requests
import runtime
import sys
import os
import json

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

#rf_1_pin = OutputPin({
#    "__name": "rf_1_pin",
#    "gpio_device": 1,
#    "line": 27
#})
#
#rf_2_pin = OutputPin({
#    "__name": "rf_2_pin",
#    "gpio_device": 1,
#    "line": 24
#})
#
#fm175_1_reset_pin = OutputPin({
#    "__name": "fm175_1_reset_pin",
#    "gpio_device": 1,
#    "line": 25
#})
#
#fm175_2_reset_pin = OutputPin({
#    "__name": "fm175_2_reset_pin",
#    "gpio_device": 1,
#    "line": 28
#})
#
#software_spi_1 = SoftwareSPI({
#    "__name": "software_spi_1",
#    "bus": 2,
#    "device": 0,
#    "max_speed_hz": 500000,
#    "mode": 0
#})
#
#software_spi_2 = SoftwareSPI({
#    "__name": "software_spi_2",
#    "bus": 2,
#    "device": 1,
#    "max_speed_hz": 500000,
#    "mode": 0
#})
#
#register_configurable_entity(rf_1_pin)
#register_configurable_entity(rf_2_pin)
#register_configurable_entity(fm175_1_reset_pin)
#register_configurable_entity(fm175_2_reset_pin)
#register_configurable_entity(software_spi_1)
#register_configurable_entity(software_spi_2)
#
#fm175_1 = Fm175xx({
#    "__name": "fm175_1",
#    "spi": "software_spi_1",
#    "reset_pin": "fm175_1_reset_pin"
#})
#
#fm175_2 = Fm175xx({
#    "__name": "fm175_2",
#    "spi": "software_spi_2",
#    "reset_pin": "fm175_2_reset_pin"
#})
#
#register_configurable_entity(fm175_1)
#register_configurable_entity(fm175_2)
#
#gpio_enabled_rfid_reader_1 = GpioEnabledRfidReader({
#    "__name": "gpio_enabled_rfid_reader_1",
#    "rfid_reader": "fm175_1",
#    "gpio_pins_high": ["rf_1_pin"],
#    "gpio_pins_low": ["rf_2_pin"],
#    "slot": 2,
#})
#
#gpio_enabled_rfid_reader_2 = GpioEnabledRfidReader({
#    "__name": "gpio_enabled_rfid_reader_1_mode_2",
#    "rfid_reader": "fm175_1",
#    "gpio_pins_high": ["rf_2_pin"],
#    "gpio_pins_low": ["rf_1_pin"],
#    "slot": 3,
#})
#
#gpio_enabled_rfid_reader_3 = GpioEnabledRfidReader({
#    "__name": "gpio_enabled_rfid_reader_2",
#    "rfid_reader": "fm175_2",
#    "gpio_pins_high": ["rf_1_pin"],
#    "gpio_pins_low": ["rf_2_pin"],
#    "slot": 0,
#})
#
#gpio_enabled_rfid_reader_4 = GpioEnabledRfidReader({
#    "__name": "gpio_enabled_rfid_reader_2_mode_2",
#    "rfid_reader": "fm175_2",
#    "gpio_pins_high": ["rf_2_pin"],
#    "gpio_pins_low": ["rf_1_pin"],
#    "slot": 1,
#})
#
#register_configurable_entity(gpio_enabled_rfid_reader_1)
#register_configurable_entity(gpio_enabled_rfid_reader_2)
#register_configurable_entity(gpio_enabled_rfid_reader_3)
#register_configurable_entity(gpio_enabled_rfid_reader_4)
#
#readers = [
#    gpio_enabled_rfid_reader_1,
#    gpio_enabled_rfid_reader_2,
#    gpio_enabled_rfid_reader_3,
#    gpio_enabled_rfid_reader_4
#]

def main():
    if len(sys.argv) < 2:
        logging.error("No config file provided")
        sys.exit(1)
    
    config_file = sys.argv[1]

    if not os.path.exists(config_file):
        logging.error(f"Config file does not exist: {config_file}")
        sys.exit(1)
    
    with open(config_file, "r") as f:
        config = f.read()

    json_config = json.loads(config)

    run = runtime.consume_config(json_config)
    run.loop()
    
if __name__ == "__main__":
    main()