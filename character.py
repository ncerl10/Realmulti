#importing from other files
from armour import *
from weapon import *
from accessory import *
from spell import *
from item import *


class Character:
    """A class that creates an instance of the game

    Attributes
    ----------
    - name : str
      Name of the player
    - health : int
      Amount of health the player has
    - max_health : int
      Maximum health of the player
    - spells : list[Spell]
      List of spells the player knows
    - attack : int
      Amount of extra damage the player deals
    - mana: int
      Amount of mana the player has
    - max_mana : int
      Maximum mana of the player
    - defence : int
      Amount of damage the player resists
    - armour : Armour
      The armour the player is wearing
    - armours : list[Armour]
      List of armours the player owns
    - weapon : Weapon
      The weapon the player is using
    - weapons : list[Weapon]
      List of weapons the player owns
    - accessory : Accessory
      The accessory the player is using
    - accessories : list[Accessory]
      List of accessories the player owns
    - health_flask : int
      Number of Flask of Crimson Tears the player owns
    - mana_flask : int
      Number of Flask of Cerulean Tears the player owns
    - items : list[Item]
      List of items the player owns


    Methods
    -------
    None
    """

    def __init__(self, name: str) -> None:
        self.name = name
        # Stats
        self.health = 0
        self.max_health = 0
        self.mana = 0
        self.max_mana = 0
        self.attack = 0
        self.defence = 0
        # Equipment
        self.health_flask = 0
        self.mana_flask = 0
        self.armour = None
        self.weapon = None
        self.accessory = None
        # Inventory
        self.spells: list[Spell] = []
        self.armours: list[Armour] = []
        self.weapons: list[Weapon] = []
        self.accessories: list[Accessory] = []
        self.items: list[Item] = []

    def set_spells(self, spell: Spell) -> None:
        """updates the list of spells of the character"""
        self.spells.append(spell)

    def set_weapons(self, weapon: Weapon) -> None:
        """updates the list of weapons of the character"""
        self.weapons.append(weapon)

    def set_armours(self, armour: Armour) -> None:
        """updates the list of armours of the character"""
        self.armours.append(armour)

    def set_accessories(self, accessory: Accessory) -> None:
        """updates the equipped accessory of the character"""
        self.accessories.append(accessory)

    def set_health_flask(self, number: int) -> None:
        """updates the number of health flask of the character"""
        self.health_flask += number

    def set_mana_flask(self, number: int) -> None:
        """updates the number of mana flask of the character"""
        self.mana_flask += number

    def set_items(self, item: Item) -> None:
        """updates the list of items of the character"""
        self.items.append(item)
