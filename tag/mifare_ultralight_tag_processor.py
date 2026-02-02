from tag.tag_processor import TagProcessor

class MifareUltralightTagProcessor(TagProcessor):
    def __init__(self, name : str):
        super().__init__(name)