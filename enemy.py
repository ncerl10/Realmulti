import json

#importing from other files
from armour import *
from weapon import *
from accessory import *
from spell import *
from item import *
import armour
import weapon
import accessory
import spell
import item


class Enemy:
    """The parent class for an enemy

    Attributes
    ----------
    - name : str
      Name of the enemy
    - health : int
      Amount of health the enemy has
    - attack : int
      Amount of damage the enemy deals
    - loot : Item
      The loot the enemy drops when killed
    - description : str
      Description of the enemy
    - move : str
      Description of the enemy's attack

    Methods
    -------
    None
    """

    def __init__(self,
                 name: str,
                 description: str,
                 health: int,
                 attack: int,
                 move: str,
                 loot: str) -> None:
        self.name = name
        self.description = description
        self.health = health
        self.attack = attack
        self.move = move
        self.loot = loot

    def __str__(self) -> str:
        return self.name

    def is_dead(self) -> bool:
        return self.health <= 0

    def take_damage(self, damage: int) -> int:
        """Minimum damage that can be dealt is 1.
        Returns the damage dealt.
        """
        if damage < 1:
            damage = 1
        self.health -= damage
        return damage


# Read data from JSON file
_data = {}
with open("data/enemy.json", "r") as f:
    for record in json.load(f):
        _data[record["name"]] = record


def create(name: str) -> Enemy:
    record = _data[name]
    # The ** operator unpacks a dict as keyword arguments
    enemy = Enemy(**record)
    if enemy.loot in accessory._data:
        loot = accessory.create(enemy.loot)
    elif enemy.loot in armour._data:
        loot = armour.create(enemy.loot)
    elif enemy.loot in weapon._data:
        loot = weapon.create(enemy.loot)
    elif enemy.loot in spell._data:
        loot = spell.create(enemy.loot)
    elif enemy.loot in item._flask:
        loot = item.create(enemy.loot)
    elif enemy.loot in item._quest:
        loot = item.create(enemy.loot)
    enemy.loot = loot
    return enemy
