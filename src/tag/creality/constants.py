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
    "01001": CrealityAdditonalData("PLA", ["Hyper"], 190.0, 240.0, 50.0, 50.0, 8.0),
    "02001": CrealityAdditonalData("PLA-CF", ["Hyper"], 190.0, 240.0, 50.0, 50.0, 8.0),
    "06002": CrealityAdditonalData("PETG", ["Hyper"], 220.0, 270.0, 70.0, 60.0, 8.0),
    "03001": CrealityAdditonalData("ABS", ["Hyper"], 240.0, 280.0, 80.0, 80.0, 8.0),
    "09002": CrealityAdditonalData("PLA", ["Ender", "Fast"], 190.0, 240.0, 50.0, 50.0, 6.0),
    "04001": CrealityAdditonalData("PLA", ["CR"], 190.0, 240.0, 50.0, 50.0, 8.0),
    "05001": CrealityAdditonalData("PLA", ["CR", "Silk"], 190.0, 240.0, 50.0, 50.0, 8.0),
    "06001": CrealityAdditonalData("PETG", ["CR"], 220.0, 270.0, 70.0, 60.0, 8.0),
    "07001": CrealityAdditonalData("ABS", ["CR"], 240.0, 280.0, 100.0, 80.0, 8.0),
    "08001": CrealityAdditonalData("PLA", ["Ender"], 190.0, 240.0, 50.0, 50.0, 8.0),
    "09001": CrealityAdditonalData("PLA", ["EN", "PLA+"], 190.0, 240.0, 50.0, 50.0, 8.0),
    "10001": CrealityAdditonalData("TPU", ["HP"], 190.0, 240.0, 40.0, 65.0, 8.0),
    "11001": CrealityAdditonalData("PA", ["CR", "Nylon"], 250.0, 270.0, 50.0, 80.0, 8.0),
    "13001": CrealityAdditonalData("PLA", ["CR", "Carbon"], 190.0, 240.0, 50.0, 50.0, 8.0),
    "14001": CrealityAdditonalData("PLA", ["CR", "Matte"], 190.0, 240.0, 50.0, 50.0, 8.0),
    "15001": CrealityAdditonalData("PLA", ["CR", "Fluo"], 190.0, 240.0, 50.0, 50.0, 8.0),
    "16001": CrealityAdditonalData("TPU", ["CR"], 210.0, 240.0, 40.0, 65.0, 8.0),
    "17001": CrealityAdditonalData("PLA", ["CR", "Wood"], 190.0, 240.0, 50.0, 50.0, 8.0),
    "18001": CrealityAdditonalData("PLA", ["HP", "Ultra"], 190.0, 240.0, 50.0, 50.0, 8.0),
    "19001": CrealityAdditonalData("ASA", ["HP"], 240.0, 280.0, 90.0, 80.0, 8.0),
    "12003": CrealityAdditonalData("PA-CF", ["Hyper", "PAHT"], 280.0, 320.0, 90.0, 80.0, 10.0),
    "12002": CrealityAdditonalData("PA-CF", ["Hyper", "PPA"], 280.0, 320.0, 100.0, 100.0, 8.0),
    "07002": CrealityAdditonalData("PC", ["Hyper"], 250.0, 270.0, 110.0, 80.0, 8.0),
    "01601": CrealityAdditonalData("PLA", ["Soleyin", "Ultra"], 190.0, 240.0, 50.0, 50.0, 8.0),
}

CREALITY_SALT_HASH = "e544d94feb16159bbd7bc227df1e283eca1f38f2bb2015dfcc6161b74473b5c2"
CREALITY_ENCRYPTION_KEY_HASH = "acec2106007458579ba522b25610b2cf509ae59d7879cb975f65c45228e5c9a1"