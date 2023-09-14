# importing from other files
from room import *
from character import *
from weapon import *
from spell import *


def setup() -> tuple[Room, Character]:
    """
    Generates the map and the character and returns it in a list
    """

    # Generates the starting room
    map = Dirtmouth()

    # Generates the character
    character = Character("")

    # Sets the default statistics of the character
    character.take_spell(WingardiumLeviosa())
    character.take_weapon(Wand())
    character.take_weapon(character.weapon)
    character.health = 100
    character.max_health = 100
    character.mana = 100
    character.max_mana = 100
    character.take_health_flask(2)
    character.take_mana_flask(2)

    return map, character
