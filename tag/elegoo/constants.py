class ElegooMaterial:
    def __init__(self, material_type: str, material_id: int, material_modifier: list[str], modifier_id: int):
        self.material_type = material_type
        self.material_modifier = material_modifier
        self.material_id = material_id
        self.modifier_id = modifier_id

        if '6' in material_modifier:
            self.material_type += "6"
            self.material_modifier.remove('6')

        if '12' in material_modifier:
            self.material_type += "12"
            self.material_modifier.remove('12')

PLA = {
    0x00: [],
    0x01: ['+'],
    0x02: ['Pro'],
    0x03: ['Silk'],
    0x04: ['CF'],
    0x05: ['Carbon'],
    0x06: ['Matte'],
    0x07: ['Fluo'],
    0x08: ['Wood'],
    0x09: ['Basic'],
    0x0A: ['RAPID', '+'],
    0x0B: ['Marble'],
    0x0C: ['Galaxy'],
    0x0D: ['Red', 'Copper'],
    0x0E: ['Sparkle'],
}

PETG = {
    0x00: [],
    0x01: ['CF'],
    0x02: ['GF'],
    0x03: ['Pro'],
    0x04: ['Translucent'],
    0x05: ['RAPID'],
}

ABS = {
    0x00: [],
    0x01: ['GF'],
}

TPU = {
    0x00: [],
    0x01: ['95A'],
    0x02: ['RAPID', '95A'],
}

PA = {
    0x00: [],
    0x01: ['CF'],
    0x03: ['HT', 'CF'],
    0x04: ['6'],
    0x05: ['6', 'CF'],
    0x06: ['12'],
    0x07: ['12', 'CF'],
}

CPE = {
    0x00: [],
}

PC = {
    0x00: [],
    0x01: ['TG'],
    0x02: ['FR'],
}

PVA = {
    0x00: [],
}

ASA = {
    0x00: [],
}

BVOH = {
    0x00: [],
}

EVA = {
    0x00: [],
}

HIPS = {
    0x00: [],
}

PP = {
    0x00: [],
    0x01: ['CF'],
    0x02: ['GF'],
}

PPA = {
    0x00: [],
    0x01: ['CF'],
    0x02: ['GF'],
}

PPS = {
    0x00: [],
    0x02: ['CF'],
}


ELEGOO_MATERIALS = {}

def get_elegoo_material(material_id: int, modifier_id: int) -> ElegooMaterial | None:
    if material_id not in ELEGOO_MATERIALS:
        return None
    
    if modifier_id not in ELEGOO_MATERIALS[material_id]:
        return None
    
    return ELEGOO_MATERIALS[material_id][modifier_id]

def __add_to_materials(material_id: int, material_type: str, ids: dict[int, list[str]]):
    if material_id not in ELEGOO_MATERIALS:
        ELEGOO_MATERIALS[material_id] = {}
    
    for modifier_id, modifier_list in ids.items():
        ELEGOO_MATERIALS[material_id][modifier_id] = ElegooMaterial(material_type, material_id, modifier_list, modifier_id)

__add_to_materials(0x00, "PLA", PLA)
__add_to_materials(0x01, "PETG", PETG)
__add_to_materials(0x02, "ABS", ABS)
__add_to_materials(0x03, "TPU", TPU)
__add_to_materials(0x04, "PA", PA)
__add_to_materials(0x05, "CPE", CPE)
__add_to_materials(0x06, "PC", PC)
__add_to_materials(0x07, "PVA", PVA)
__add_to_materials(0x08, "ASA", ASA)
__add_to_materials(0x09, "BVOH", BVOH)
__add_to_materials(0x0A, "EVA", EVA)
__add_to_materials(0x0B, "HIPS", HIPS)
__add_to_materials(0x0C, "PP", PP)
__add_to_materials(0x0D, "PPA", PPA)
__add_to_materials(0x0E, "PPS", PPS)

