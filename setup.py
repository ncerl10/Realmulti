# importing from other files
from room import *
from character import *
from weapon import *
from spell import *


def setup() -> [Room, Character]:
    """
    Generates the map and the character and returns it in a list
    """

    # Generates the starting room
    map = Dirtmouth()

    # Generates the character
    character = Character()

    # Sets the default statistics of the character
    character.set_spells(WingardiumLeviosa())
    character.set_weapon(Wand())
    character.set_weapons(character.get_weapon())
    character.set_health(100)
    character.set_max_health(100)
    character.set_mana(100)
    character.set_max_mana(100)
    character.set_health_flask(2)
    character.set_mana_flask(2)

    return [map, character]
