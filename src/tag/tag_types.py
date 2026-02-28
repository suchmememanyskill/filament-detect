from enum import Enum

class TagType(Enum):
    Unknown = 0xff,
    MifareClassic1k = 0x08,
    MifareUltralight = 0x00,

def tag_type_from_sak(sak: bytes) -> TagType:
    if sak == b"\x08":
        return TagType.MifareClassic1k
    elif sak == b"\x04\x00":
        return TagType.MifareUltralight
    else:
        return TagType.Unknown
    
def tag_type_to_readable_name(tag_type: TagType) -> str:
    match tag_type:
        case TagType.MifareClassic1k:
            return "Mifare Classic 1K"
        case TagType.MifareUltralight:
            return "Mifare Ultralight / NTAG"
        case TagType.Unknown:
            return "Unknown"