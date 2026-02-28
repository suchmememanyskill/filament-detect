import struct

def extract_string(data: bytes, pos: int, length: int) -> str:
    """Extract a null-terminated ASCII string from the data."""
    raw = data[pos:pos+length]
    return raw.decode('ascii', errors='ignore').rstrip('\x00')

def extract_uint16_le(data: bytes, pos: int) -> int:
    """Extract a little-endian uint16 from the data."""
    return struct.unpack('<H', data[pos:pos+2])[0]

def extract_uint16_be(data: bytes, pos: int) -> int:
    """Extract a big-endian uint16 from the data."""
    return struct.unpack('>H', data[pos:pos+2])[0]

def extract_uint32_le(data: bytes, pos: int) -> int:
    """Extract a little-endian uint32 from the data."""
    return struct.unpack('<I', data[pos:pos+4])[0]

def extract_uint32_be(data: bytes, pos: int) -> int:    
    """Extract a big-endian uint32 from the data."""
    return struct.unpack('>I', data[pos:pos+4])[0]

def extract_float_le(data: bytes, pos: int) -> float:
    """Extract a little-endian float from the data."""
    return struct.unpack('<f', data[pos:pos+4])[0]