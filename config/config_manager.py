from .configurable_entity import ConfigurableEntity

LOADED_MODULES : list[ConfigurableEntity] = []

def register_configurable_entity(entity: ConfigurableEntity):
    LOADED_MODULES.append(entity)

def get_configurable_entity_by_name(name: str, type: str) -> ConfigurableEntity | None:
    for entity in LOADED_MODULES:
        if entity.name == name and entity.type == type:
            return entity
    return None

def get_required_configurable_entity_by_name(name: str, type: str) -> ConfigurableEntity:
    entity = get_configurable_entity_by_name(name, type)
    if entity is None:
        raise ValueError(f"Configurable entity with name '{name}' and type '{type}' not found")
    return entity

def get_entities_by_type(type: str) -> list[ConfigurableEntity]:
    return [entity for entity in LOADED_MODULES if entity.type == type]