class CrealityAdditonalData:
    def __init__(self, type: str, modifiers: list[str], hotend_min_temp_c: float, hotend_max_temp_c: float, bed_temp_c: float, drying_temp_c: float, drying_time_hours: float):
        self.type = type
        self.modifiers = modifiers
        #self.density = density TODO: implement density
        self.hotend_min_temp_c = hotend_min_temp_c
        self.hotend_max_temp_c = hotend_max_temp_c
        self.bed_temp_c = bed_temp_c
        self.drying_temp_c = drying_temp_c
        self.drying_time_hours = drying_time_hours

CREALITY_FILAMENT_CODE_TO_DATA = {
    "01001": CrealityAdditonalData("PLA", ["Hyper"], 190.0, 230.0, 60.0, 55.0, 8.0),
}