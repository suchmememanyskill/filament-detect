import spidev
from config import ConfigurableEntity, TYPE_SOFTWARE_SPI

class SoftwareSPI(ConfigurableEntity):
    def __init__(self, config : dict):
        super().__init__(config, TYPE_SOFTWARE_SPI)
        self.bus = int(config["bus"])
        self.device = int(config["device"])
        self.max_speed_hz = int(config.get("max_speed_hz", 500000))
        self.mode = int(config.get("mode", 0))
        self.spi = spidev.SpiDev()
        self.spi.open(self.bus, self.device)
        self.spi.max_speed_hz = self.max_speed_hz
        self.spi.mode = self.mode

    def transfer(self, data : list[int]) -> list[int]:
        return self.spi.xfer(data)