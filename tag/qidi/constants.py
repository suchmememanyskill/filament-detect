TAG_TOTAL_SIZE = 1024

# MIFARE Classic 1K sector 1 block 0 starts at byte 64 (4 blocks * 16 bytes)
SECTOR_1_BLOCK_0_POS = 64
SECTOR_1_BLOCK_0_LEN = 16

# QIDI tag payload format (offsets relative to sector 1 block 0)
TAG_FORMAT_VERSION_POS = SECTOR_1_BLOCK_0_POS + 0
MATERIAL_CODE_POS = SECTOR_1_BLOCK_0_POS + 1
COLOR_CODE_POS = SECTOR_1_BLOCK_0_POS + 2
MANUFACTURER_CODE_POS = SECTOR_1_BLOCK_0_POS + 3

# Publicly documented tag format version
TAG_FORMAT_VERSION = 0x06

# Publicly documented read key for sector 1
SECTOR_1_KEY_A = bytes.fromhex("A0A1A2A3A4A5")

# Default MIFARE key used for sectors that are not QIDI-protected
DEFAULT_MIFARE_KEY_A = bytes.fromhex("FFFFFFFFFFFF")
DEFAULT_MIFARE_KEY_B = bytes.fromhex("FFFFFFFFFFFF")

MANUFACTURER_CODE_TO_NAME = {
    0x01: "QIDI",
    0x02: "X-MAKER",
}

MATERIAL_CODE_TO_NAME = {
    0x00: "PLA",
    0x01: "PETG",
    0x02: "ABS",
    0x03: "PA",
    0x04: "TPU",
    0x05: "PVA",
    0x06: "HIPS",
    0x07: "PC",
    0x08: "ASA",
    0x09: "PP",
    0x0A: "POM",
    0x0B: "PMMA",
    0x0C: "WOOD",
    0x0D: "CARBON",
    0x0E: "GLASS",
    0x0F: "METAL",
    0x10: "PLA-CF",
    0x11: "PETG-CF",
    0x12: "PA-CF",
    0x13: "ABS-CF",
    0x14: "PC-CF",
    0x15: "ASA-CF",
}

COLOR_CODE_TO_ARGB = {
    0x00: 0xFF111111,  # Black
    0x01: 0xFFFFFFFF,  # White
    0x02: 0xFFE53935,  # Red
    0x03: 0xFFFF8C00,  # Orange
    0x04: 0xFFFFEB3B,  # Yellow
    0x05: 0xFF43A047,  # Green
    0x06: 0xFF1E88E5,  # Blue
    0x07: 0xFF8E24AA,  # Purple
    0x08: 0xFF8D6E63,  # Brown
    0x09: 0xFF757575,  # Gray
    0x0A: 0xFFFFD700,  # Gold
    0x0B: 0xFFC0C0C0,  # Silver
    0x0C: 0x80FFFFFF,  # Transparent
    0x0E: 0xFF76FF03,  # Fluorescent green
    0x11: 0xFFEC407A,  # Pink
    0x12: 0xFF00BCD4,  # Cyan
}

class FilamentTypeExtendedData:
    def __init__(self, hotend_min_temp_c: float, hotend_max_temp_c: float, bed_temp_c: float, drying_temp_c: float, drying_time_hours: float):
        self.hotend_min_temp_c = hotend_min_temp_c
        self.hotend_max_temp_c = hotend_max_temp_c
        self.bed_temp_c = bed_temp_c
        self.drying_temp_c = drying_temp_c
        self.drying_time_hours = drying_time_hours

FILAMENT_TYPE_TO_EXTENDED_DATA = {
    "PLA": FilamentTypeExtendedData(190.0, 230.0, 60.0, 50.0, 8.0),
    "PETG": FilamentTypeExtendedData(220.0, 260.0, 80.0, 65.0, 8.0),
    "ABS": FilamentTypeExtendedData(230.0, 270.0, 100.0, 80.0, 8.0),
    "PA": FilamentTypeExtendedData(240.0, 290.0, 90.0, 80.0, 8.0),
    "TPU": FilamentTypeExtendedData(200.0, 240.0, 50.0, 70.0, 8.0),
    "PVA": FilamentTypeExtendedData(180.0, 220.0, 60.0, 45.0, 8.0),
    "HIPS": FilamentTypeExtendedData(220.0, 250.0, 90.0, 70.0, 8.0),
    "PC": FilamentTypeExtendedData(260.0, 310.0, 110.0, 90.0, 8.0),
    "ASA": FilamentTypeExtendedData(240.0, 280.0, 100.0, 80.0, 8.0),
    "PP": FilamentTypeExtendedData(220.0, 260.0, 80.0, 80.0, 8.0),
    "POM": FilamentTypeExtendedData(210.0, 240.0, 90.0, 80.0, 8.0),
    "PMMA": FilamentTypeExtendedData(230.0, 260.0, 90.0, 80.0, 8.0),
    "WOOD": FilamentTypeExtendedData(180.0, 220.0, 60.0, 55.0, 8.0),
    "CARBON": FilamentTypeExtendedData(240.0, 280.0, 90.0, 80.0, 8.0),
    "GLASS": FilamentTypeExtendedData(230.0, 270.0, 90.0, 80.0, 8.0),
    "METAL": FilamentTypeExtendedData(200.0, 240.0, 60.0, 60.0, 8.0),
}

