from abc import ABC

class ConfigurableEntity(ABC):
    def __init__(self, config: dict, type : str):
        self.name = config["__name"]
        self.type = type