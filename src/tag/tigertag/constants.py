TIGERTAG_VERSION_IDS = {
    0x00000000: "RFID Empty",
    0x6C41A2E1: "TigerTag Init V1.0",
    0x5BF59264: "TigerTag Maker V1.0",
    0xBC0FCB97: "TigerTag Pro V1.0",
}

TIGERTAG_VALID_DATA_IDS = {0x5BF59264, 0xBC0FCB97}

TIGERTAG_EPOCH_OFFSET = 946684800

OFF_TAG_ID = 0
OFF_PRODUCT_ID = 4
OFF_MATERIAL_ID = 8
OFF_ASPECT1_ID = 10
OFF_ASPECT2_ID = 11
OFF_TYPE_ID = 12
OFF_DIAMETER_ID = 13
OFF_BRAND_ID = 14
OFF_COLOR_RGBA = 16
OFF_WEIGHT = 20
OFF_UNIT_ID = 23
OFF_TEMP_MIN = 24
OFF_TEMP_MAX = 26
OFF_DRY_TEMP = 28
OFF_DRY_TIME = 29
OFF_TIMESTAMP = 32
OFF_METADATA = 48
OFF_SIGNATURE = 80

MIN_DATA_LENGTH = 96
USER_DATA_PAGE_OFFSET = 4
USER_DATA_BYTE_OFFSET = USER_DATA_PAGE_OFFSET * 4

MATERIAL_ID_TO_LABEL = {
    425: "ABS-CF", 735: "ABS-AF", 1173: "PA6-GF", 2053: "PA12-GF",
    3368: "PC-ABS", 3481: "PCTG-GF", 4587: "PC-PBT", 5733: "TPU for AMS",
    7649: "PETG HS", 7951: "PETG-rCF", 8345: "PLA+ Silk", 8504: "PPA-CF",
    9456: "PLA Marble", 9483: "PVA", 9691: "EVA", 10187: "PHA",
    10272: "PSU", 10478: "Castable Filament", 10602: "PLA Silk", 10738: "PC-PTFE",
    11053: "PET-CF", 11506: "PLA-LW (AERO)", 12264: "PA6-CF", 12844: "ASA",
    13850: "PPA", 15041: "PCTG", 18130: "PS", 18703: "PETP",
    18775: "PE-CF", 18922: "PLA-ESD", 20073: "PVC", 20562: "ABS",
    24115: "SEBS", 24116: "TPC", 24270: "PPS-CF", 24629: "PLA High Speed",
    26029: "HIPS", 27268: "PCTPE", 27635: "PE", 27676: "ASA-CF",
    28110: "SBC", 29815: "PEEK", 30458: "PC", 30594: "PA-GF",
    30884: "PP", 31011: "ASA-LW (AERO)", 33958: "TPE", 34049: "BVOH",
    34409: "TPS", 35100: "ASA-GF", 38219: "PLA", 38256: "PETG",
    39667: "PA12-CF", 39944: "PA-CF", 42623: "PMMA", 42962: "PP-GF",
    43518: "TPU", 45962: "PVB", 46154: "PPS", 46276: "PPA-GF",
    46591: "PLA+", 47651: "PC-PBT-CF", 48001: "PLA Wood", 48047: "TPU High Speed",
    48310: "PLA-CF", 48815: "PAHT-CF", 49074: "ABS-GF", 49152: "PPSU",
    49804: "ASA-AF (Kevlar)", 50206: "POM", 50497: "PP-CF", 51007: "Biopolymer",
    51861: "PETG-ESD", 52077: "PET", 53890: "PCTG-CF", 53970: "PEKK",
    54568: "ASA+", 55279: "PBT", 55418: "PETG-CF", 55796: "PA12",
    56527: "PEI", 56666: "PA6", 57469: "PETG HF", 58142: "TPU-GF",
    58498: "PEBA", 59328: "PA", 61048: "PVDF", 61563: "PC-PBT-GF",
    63946: "TPI", 65535: "None",
}

BRAND_ID_TO_NAME = {
    1: "Atome3D", 1120: "Proto-Pasta", 1421: "3DJake", 2517: "Smart Materials 3D",
    2833: "Xstrand", 3132: "Hatchbox", 4011: "QIDI Tech", 4048: "Owa",
    4344: "MatterHackers", 4356: "Landu", 7674: "Extrudr", 7812: "Jayo",
    7980: "Fillamentum", 8182: "Fiberlogy", 8303: "GST3D", 8384: "Taulman3D",
    8586: "NinjaTek", 8675: "SOVB 3D", 8756: "BlueCast", 8990: "Ice Filaments",
    9192: "3D Solutech", 9394: "Gizmo Dorks", 9596: "Ziro", 9798: "AMOLEN",
    11429: "3D4Makers", 11501: "InnovateFil", 12345: "MakerBot", 12498: "Forshape",
    14982: "3D-Fuel", 15899: "Kimya", 15962: "Anycubic", 18629: "PrintoMax 3D",
    19265: "CC3D", 19961: "Rosa3D", 20523: "Raise3D", 20851: "Tronxy",
    22652: "Spectrum", 23181: "ArianePlast", 23456: "Monoprice", 26595: "Sovol",
    26956: "Creality", 28055: "TAGin3D", 28136: "Polar Filament", 28940: "Eryone",
    29045: "Yousu", 29302: "IIIDMAX", 32587: "Amazon", 33788: "Verbatim",
    34567: "Push Plastic", 35123: "Bambu Lab", 36702: "Tianse", 37434: "Winkle",
    39382: "Longer", 39652: "3DXTech", 41932: "Jamg He", 45670: "Panchroma",
    45678: "Atomic Filament", 46010: "AceAddity", 46203: "Overture", 46392: "Prusa",
    47560: "Wanhao", 47930: "eSun", 48804: "R3D", 49784: "GIANTARN",
    50311: "G3D Pro", 50604: "Polymaker", 51443: "BASF", 51857: "Sunlu",
    52222: "ColorFabb", 52467: "Geeetech", 52757: "Yumi", 53043: "FormFutura",
    53640: "Magigoo", 53856: "Lattice Medical", 54112: "Kexcelled", 55763: "Nanovia",
    55869: "Biqu", 56780: "Fiberon", 56789: "Coex 3D", 57209: "FrancoFil",
    57632: "Elegoo", 58231: "IC3D", 58410: "AzureFilm", 60882: "Recreus",
    63340: "Flashforge", 65535: "Generic",
}

DIAMETER_ID_TO_MM = {
    56: 1.75,
    221: 2.85,
}

ASPECT_ID_TO_LABEL = {
    0: "", 21: "Clear", 24: "Tricolor", 64: "Glitter",
    67: "Translucent", 91: "Glow in the Dark", 92: "Silk", 97: "Lithophane",
    104: "Basic", 123: "Wood", 126: "Pearl", 129: "Gloss",
    134: "Satin", 145: "Rainbow", 168: "Thermoreactif", 173: "Stone",
    216: "Neon", 220: "Pastel", 232: "Marble", 238: "Carbon",
    247: "Matt", 252: "Bicolor", 255: "None",
}

TYPE_ID_TO_LABEL = {
    142: "Filament",
    173: "Resin",
}

UNIT_ID_TO_LABEL = {
    1: "g", 2: "kg",
    10: "mg", 21: "g", 35: "kg",
    48: "ml", 62: "cl", 79: "L",
    95: "m³", 112: "mm", 130: "cm", 149: "m", 170: "m²",
}
