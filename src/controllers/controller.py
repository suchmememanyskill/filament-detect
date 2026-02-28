from abc import abstractmethod
from config import ConfigurableEntity, TYPE_CONTROLLER, get_required_configurable_entity_by_name, TYPE_RUNTIME
class Controller(ConfigurableEntity):
    def __init__(self, config: dict):
        super().__init__(config, TYPE_CONTROLLER)
        self.runtime = None

    @abstractmethod
    def loop(self):
        """Main loop of the controller. This method will be called once."""
        raise NotImplementedError("Subclasses must implement this method")
    
