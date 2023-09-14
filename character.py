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
        self.health_flask = FlaskOfCrimsonTears()
        self.mana_flask = FlaskOfCeruleanTears()
        self.armour = None
        self.weapon = None
        self.accessory = None
        # Inventory
        self.spells: list[Spell] = []
        self.armours: list[Armour] = []
        self.weapons: list[Weapon] = []
        self.accessories: list[Accessory] = []
        self.items: list[Item] = []

    def get_attack(self) -> int:
        attack = self.attack
        if self.weapon:
            attack += self.weapon.attack
        if self.accessory:
            attack += self.accessory.attack_boost
        return attack
        
    def get_defence(self) -> int:
        defence = self.defence
        if self.armour:
            defence += self.armour.defence
        if self.accessory:
            defence += self.accessory.defence_boost
        return defence

    def get_max_health(self) -> int:
        max_health = self.max_health
        if self.accessory:
            max_health += self.accessory.health_boost
        return max_health

    def get_max_mana(self) -> int:
        max_mana = self.max_mana
        if self.accessory:
            max_mana += self.accessory.mana_boost
        return max_mana

    def add_health(self, amt: int) -> int:
        """Adds amt to health, without exceeding the maximum.
        Returns the amt of health added.
        """
        boost = min(amt, self.max_health - self.health)
        self.health += boost
        return boost

    def add_mana(self, amt: int) -> int:
        """Adds amt to mana, without exceeding the maximum
        Returns the amt of mana added.
        """
        boost = min(amt, self.max_mana - self.mana)
        self.mana += boost
        return boost

    def display_flask(self) -> None:
        print()  # line break
        print(self.health_flask.report())
        print(self.mana_flask.report())
        print()  # line break

    def take_spell(self, spell: Spell) -> None:
        """updates the list of spells of the character"""
        self.spells.append(spell)

    def take_weapon(self, weapon: Weapon) -> None:
        """updates the list of weapons of the character"""
        self.weapons.append(weapon)

    def take_armour(self, armour: Armour) -> None:
        """updates the list of armours of the character"""
        self.armours.append(armour)

    def take_accessory(self, accessory: Accessory) -> None:
        """updates the equipped accessory of the character"""
        self.accessories.append(accessory)

    def consume_health_flask(self, number: int = 1) -> None:
        self.health_flask.count -= number

    def consume_mana_flask(self, number: int = 1) -> None:
        self.mana_flask.count -= number

    def take_health_flask(self, number: int = 1) -> None:
        self.health_flask.count += number

    def take_mana_flask(self, number: int = 1) -> None:
        self.mana_flask.count += number

    def take_item(self, item: Item) -> None:
        """updates the list of items of the character"""
        self.items.append(item)
