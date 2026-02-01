class GenericFilament:
    def __init__(self,
                 source_processor: str,
                 unique_id: str,
                 manufacturer: str,
                 type: str, # TODO: Should probably be an enum?
                 modifiers: list[str],
                 colors : list[int], # Format 0xAARRGGBB
                 diameter_mm: float,
                 weight_grams: float,
                 hotend_min_temp_c: float,
                 hotend_max_temp_c: float,
                 bed_temp_c: float,
                 drying_temp_c: float,
                 drying_time_hours: float,
                 manufacturing_date: str # ISO 8601 date string
                 ):
        self.source_processor = source_processor
        self.unique_id = unique_id
        self.manufacturer = manufacturer
        self.type = type
        self.modifiers = modifiers
        self.colors = colors
        self.diameter_mm = diameter_mm
        self.weight_grams = weight_grams
        self.hotend_min_temp_c = hotend_min_temp_c
        self.hotend_max_temp_c = hotend_max_temp_c
        self.bed_temp_c = bed_temp_c
        self.drying_temp_c = drying_temp_c
        self.drying_time_hours = drying_time_hours
        self.manufacturing_date = manufacturing_date

    def pretty_text(self) -> str:
        return "\n".join([
            f"{self.manufacturer} {self.type} {' '.join(self.modifiers)} Filament:",
            f"- Color (ARGB): {' '.join([f'#{color:06X}' for color in self.colors])}",
            f"- Diameter: {self.diameter_mm:.2f} mm",
            f"- Weight: {self.weight_grams} grams",
            f"- Hotend Temp: {self.hotend_min_temp_c:.1f}C - {self.hotend_max_temp_c:.1f}C",
            f"- Bed Temp: {self.bed_temp_c:.1f}C",
            f"- Drying: {self.drying_temp_c:.1f}C for {self.drying_time_hours:.1f} hours",
            f"- Manufactured on: {self.manufacturing_date}"
        ])