from .config_manager import register_configurable_entity, get_configurable_entity_by_name, get_required_configurable_entity_by_name, get_entities_by_type
from .configurable_entity import ConfigurableEntity

TYPE_SOFTWARE_SPI = "software_spi"
TYPE_OUTPUT_PIN = "output_pin"
TYPE_RFID_READER = "rfid_reader"
TYPE_EXPORTER = "exporter"
TYPE_RUNTIME = "runtime"
TYPE_TAG_PROCESSOR = "tag_processor"
TYPE_CONTROLLER = "controller"
TYPE_CONFIGURATION = "configuration"