from tag.tag_types import TagType, tag_type_to_readable_name


class ScanResult:
    def __init__(self, tag_type : TagType, uid : bytes, atqa : bytes, bcc : bytes, sak: bytes):
        self.tag_type = tag_type
        self.uid = uid
        self.atqa = atqa
        self.bcc = bcc
        self.sak = sak
    
    def pretty_text(self) -> str:
        return "Tag detected:\n- TagType: {}\n- UID: {}\n- ATQA: {}\n- BCC: {}\n- SAK: {}".format(
            tag_type_to_readable_name(self.tag_type),
            self.uid.hex(":").upper(),
            self.atqa.hex(":").upper(),
            self.bcc.hex(":").upper(),
            self.sak.hex(":").upper()
        )
    
    def to_dict(self) -> dict:
        return {
            "tag_type": self.tag_type.name,
            "uid": self.uid.hex().upper(),
            "atqa": self.atqa.hex().upper(),
            "bcc": self.bcc.hex().upper(),
            "sak": self.sak.hex().upper()
        }