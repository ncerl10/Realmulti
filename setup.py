# importing from other files
import room
from character import *
import weapon
import spell


def setup() -> tuple[room.Room, Character]:
    """
    Generates the map and the character and returns it in a list
    """

    # Generates the starting room
    map = room.get("Dirtmouth")

    # Generates the character
    character = Character("")

    # Sets the default statistics of the character
    character.take_spell(spell.create("WingardiumLeviosa"))
    character.take_weapon(weapon.create("Wand"))
    character.health = 100
    character.max_health = 100
    character.mana = 100
    character.max_mana = 100
    character.take_health_flask(2)
    character.take_mana_flask(2)

    return map, character
