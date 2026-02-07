# I have no idea what freakish version of gpiod this is. '1.6.4' apparently.
import gpiod
from config import ConfigurableEntity, TYPE_OUTPUT_PIN
import atexit

class OutputPin(ConfigurableEntity):
    def __init__(self, config : dict):
        super().__init__(config, TYPE_OUTPUT_PIN)
        self.gpio_device = str(config["gpio_device"])
        self.line_offset = int(config["line"])
        self.value = str(config.get("default_high", "false")).lower() == "true"
        
        self.chip = gpiod.Chip(f"/dev/gpiochip{self.gpio_device}")
        self.pin = self.chip.get_line(self.line_offset)
        self.pin.request(
            consumer = self.name,
            type = gpiod.LINE_REQ_DIR_OUT,
            default_val = self.value and 1 or 0
        )

        atexit.register(self.__at_exit)

    def set_high(self):
        self.pin.set_value(1)
        self.value = True

    def set_low(self):
        self.pin.set_value(0)
        self.value = False

    def __at_exit(self):
        self.pin.release()