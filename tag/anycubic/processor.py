from filament import GenericFilament
from reader.scan_result import ScanResult
from tag.mifare_ultralight_tag_processor import MifareUltralightTagProcessor
from tag.tag_types import TagType
import struct

# Adapted from https://github.com/DnG-Crafts/ACE-RFID

class AnycubicTagProcessor(MifareUltralightTagProcessor):
    def __init__(self):
        super().__init__("Anycubic Tag Processor")

    def process_tag(self, scan_result: ScanResult, data: bytes) -> GenericFilament | None:
        if scan_result.tag_type != TagType.MifareUltralight:
            raise ValueError("AnycubicTagProcessor can only process Mifare Ultralight tags")
        
        if len(data) != 192:
            return None
        
        if data[0x10:0x14] != b'\x7B\x00\x65\x00':
            return None
        
        sku = data[0x14:0x24].decode('ASCII').rstrip('\x00')
        brand = data[0x28:0x38].decode('ASCII').rstrip('\x00')
        filament_type = data[0x3C:0x4C].decode('ASCII').rstrip('\x00')
        filament_types = filament_type.replace("-", " ").split(" ")

        a = data[0x50]
        r = data[0x51]
        g = data[0x52]
        b = data[0x53]

        argb = (0xFF << 24) | (r << 16) | (g << 8) | b

        extruder_min_temp_c = self.__extract_uint16_le(data, 0x60)
        extruder_max_temp_c = self.__extract_uint16_le(data, 0x62)

        heated_bed_min_temp_c = self.__extract_uint16_le(data, 0x74)
        heated_bed_max_temp_c = self.__extract_uint16_le(data, 0x76)

        filament_diameter_mm = float(self.__extract_uint16_le(data, 0x78)) / 100.0
        filament_length_m = self.__extract_uint16_le(data, 0x7A)

        match filament_length_m:
            case 330:
                weight_grams = 1000
            case 165:
                weight_grams = 500
            case 80:
                weight_grams = 250
            case _:
                weight_grams = 1000  # Default to 1000g if unknown

        return GenericFilament(
            source_processor=self.name,
            unique_id=f"Anycubic_{sku}", # TODO: Improve unique ID
            manufacturer=brand,
            type=filament_types[0] if filament_types else "PLA",
            modifiers=filament_types[1:],
            colors=[argb],
            diameter_mm=filament_diameter_mm,
            weight_grams=weight_grams,
            hotend_min_temp_c=extruder_min_temp_c,
            hotend_max_temp_c=extruder_max_temp_c,
            bed_temp_c=heated_bed_max_temp_c,
            drying_temp_c=0,
            drying_time_hours=0,
            manufacturing_date="0001-01-01"
        )

    def __extract_uint16_le(self, data: bytes, pos: int) -> int:
        """Extract a little-endian uint16 from the data."""
        return struct.unpack('<H', data[pos:pos+2])[0]