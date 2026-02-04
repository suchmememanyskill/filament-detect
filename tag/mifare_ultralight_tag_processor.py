from tag.tag_processor import TagProcessor

class MifareUltralightTagProcessor(TagProcessor):
    def __init__(self, config: dict):
        super().__init__(config)