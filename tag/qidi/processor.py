from filament import GenericFilament
from reader.scan_result import ScanResult
from tag.mifare_classic_tag_processor import MifareClassicTagProcessor, TagAuthentication
from tag.tag_types import TagType
from . import constants as Constants
import logging

class QidiTagProcessor(MifareClassicTagProcessor):
    def __init__(self, config: dict):
        super().__init__(config)

        configured_sector_1_key = self.load_key_from_config("sector_1_key")
        self.sector_1_key = self.__parse_key_or_default(configured_sector_1_key, Constants.SECTOR_1_KEY_A)

        configured_default_key = self.load_key_from_config("default_key")
        self.default_key = self.__parse_key_or_default(configured_default_key, Constants.DEFAULT_MIFARE_KEY_A)

    def authenticate_tag(self, scan_result: ScanResult) -> TagAuthentication:
        if scan_result.tag_type != TagType.MifareClassic1k:
            raise ValueError("QidiTagProcessor can only authenticate Mifare Classic 1K tags")

        key_a = [list(self.default_key) for _ in range(16)]
        key_b = [list(Constants.DEFAULT_MIFARE_KEY_B) for _ in range(16)]

        # QIDI data is publicly documented in sector 1 block 0.
        key_a[1] = list(self.sector_1_key)

        return TagAuthentication(key_a, key_b)

    def process_tag(self, scan_result: ScanResult, data: bytes) -> GenericFilament | None:
        if scan_result.tag_type != TagType.MifareClassic1k:
            raise ValueError("QidiTagProcessor can only process Mifare Classic 1K tags")

        if len(data) != Constants.TAG_TOTAL_SIZE:
            return None

        tag_format_version = data[Constants.TAG_FORMAT_VERSION_POS]
        if tag_format_version != Constants.TAG_FORMAT_VERSION:
            return None

        material_code = data[Constants.MATERIAL_CODE_POS]
        color_code = data[Constants.COLOR_CODE_POS]
        manufacturer_code = data[Constants.MANUFACTURER_CODE_POS]

        material_name = Constants.MATERIAL_CODE_TO_NAME.get(material_code, None)
        if material_name is None:
            logging.warning("Unknown QIDI material code: 0x%02X", material_code)
            return None

        manufacturer_name = Constants.MANUFACTURER_CODE_TO_NAME.get(manufacturer_code, f"QIDI-{manufacturer_code}")
        color_argb = Constants.COLOR_CODE_TO_ARGB.get(color_code, 0xFFFFFFFF)

        filament_type, modifiers = self.__split_material_name(material_name)
        ext = Constants.FILAMENT_TYPE_TO_EXTENDED_DATA.get(
            filament_type,
            Constants.FilamentTypeExtendedData(190.0, 230.0, 60.0, 50.0, 8.0),
        )

        logging.debug("Found QIDI filament tag:")
        logging.debug(" Format Version: 0x%02X", tag_format_version)
        logging.debug(" Material Code: 0x%02X (%s)", material_code, material_name)
        logging.debug(" Color Code: 0x%02X", color_code)
        logging.debug(" Manufacturer Code: 0x%02X (%s)", manufacturer_code, manufacturer_name)

        return GenericFilament(
            source_processor=self.name,
            unique_id=GenericFilament.generate_unique_id(
                "QIDI",
                scan_result.uid.hex().upper(),
                material_code,
                color_code,
                manufacturer_code,
            ),
            manufacturer=manufacturer_name,
            type=filament_type,
            modifiers=modifiers,
            colors=[color_argb],
            diameter_mm=1.75,
            weight_grams=1000,
            hotend_min_temp_c=ext.hotend_min_temp_c,
            hotend_max_temp_c=ext.hotend_max_temp_c,
            bed_temp_c=ext.bed_temp_c,
            drying_temp_c=ext.drying_temp_c,
            drying_time_hours=ext.drying_time_hours,
            manufacturing_date="0001-01-01",
        )

    def __parse_key_or_default(self, value: str | None, default: bytes) -> bytes:
        if value is None or value.strip() == "":
            return default

        try:
            key_bytes = bytes.fromhex(value)
            if len(key_bytes) != 6:
                raise ValueError("Key must be exactly 6 bytes")
            return key_bytes
        except Exception as e:
            raise ValueError(f"Invalid key format '{value}': {e}") from e

    def __split_material_name(self, material_name: str) -> tuple[str, list[str]]:
        if "-" not in material_name:
            return material_name, []

        base, modifier = material_name.split("-", 1)
        return base, [modifier]

