from filament import GenericFilament

class SnapmakerFilament:
    def __init__(self,
                 version: int,
                 vendor: str,
                 manufacturer: str,
                 main_type: str,
                 sub_type: str,
                 tray: int,
                 alpha: int,
                 color_nums: int,
                 argb_color: int,
                 rgb_1: int,
                 rgb_2: int,
                 rgb_3: int,
                 rgb_4: int,
                 rgb_5: int,
                 diameter_mm: int,
                 weight_grams: int,
                 length_meters: int,
                 drying_temp: int,
                 drying_time_hours: int,
                 hotend_max_temp: int,
                 hotend_min_temp: int,
                 bed_type: int,
                 bed_temp: int,
                 first_layer_temp: int,
                 other_layer_temp: int,
                 sku: str,
                 manufacturing_date: str,
                 rsa_key_version: int,
                 official: bool,
                 card_uid: int):
        self.version = version
        self.vendor = vendor
        self.manufacturer = manufacturer
        self.main_type = main_type
        self.sub_type = sub_type
        self.tray = tray
        self.alpha = alpha
        self.color_nums = color_nums
        self.argb_color = argb_color
        self.rgb_1 = rgb_1
        self.rgb_2 = rgb_2
        self.rgb_3 = rgb_3
        self.rgb_4 = rgb_4
        self.rgb_5 = rgb_5
        self.diameter_mm = diameter_mm
        self.weight_grams = weight_grams
        self.length_meters = length_meters
        self.drying_temp = drying_temp
        self.drying_time_hours = drying_time_hours
        self.hotend_max_temp = hotend_max_temp
        self.hotend_min_temp = hotend_min_temp
        self.bed_type = bed_type
        self.bed_temp = bed_temp
        self.first_layer_temp = first_layer_temp
        self.other_layer_temp = other_layer_temp
        self.sku = sku
        self.manufacturing_date = manufacturing_date
        self.rsa_key_version = rsa_key_version
        self.official = official
        self.card_uid = card_uid

    def pretty_text(self) -> str:
        # TODO: Implement
        return ""
    
    def to_generic_filament(self) -> GenericFilament:
        # TODO: Mapping
        return None