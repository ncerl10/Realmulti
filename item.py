import json

class Item:
    """The parent class for an item

    Attributes
    ----------
    - name : str
      Name of the item
    - description : str
      Description of the item
    - health : int
      Numerical value added to the health of the the character
    - mana : int
      Numerical value added to the mana of the the character

    Methods
    -------
    None
    """

    def __init__(self,
                 name: str,
                 description: str):
        self.name = name
        self.description = description


class Flask(Item):
    """A flask that provides a boost to one or more stats.

    Attributes
    ----------
    - count: int
      The number of flasks held

    Methods
    -------
    - effect() -> str
      Describes the effect of the item
    - report() -> str
      Reports the name, count, and effect of each item
    """
    def __init__(self,
                 name: str,
                 description: str,
                 count: int):
        super().__init__(name, description)
        self.count = count

    def effect(self) -> str:
        raise NotImplementedError

    def report(self) -> str:
        return f"Number of {self.name} in inventory: {self.count} ({self.effect()})"

class HealthFlask(Flask):
    """A flask that provides a boost to health"""
    def __init__(self,
                 name: str,
                 description: str,
                 count: int,
                 health: int):
        super().__init__(name, description, count)
        self.health = health

    def effect(self) -> str:
        return f"restores {self.health} health"
    

class ManaFlask(Flask):
    """A flask that provides a boost to mana"""
    def __init__(self,
                 name: str,
                 description: str,
                 count: int,
                 mana: int):
        super().__init__(name, description, count)
        self.mana = mana

    def effect(self) -> str:
        return f"restores {self.mana} mana"
    


class QuestItem(Item):
    """An item required to complete the quest or win the game"""


# Read data from JSON file
with open("data/item.json", "r") as f:
    record = json.load(f)
_flask = {
    "health_flask": record["health_flask"],
    "mana_flask": record["mana_flask"]
}
_quest = record["quest_items"]


def create(name: str) -> Flask | QuestItem:
    if name == "health_flask":
        return HealthFlask(**_flask[name])
    elif name == "mana_flask":
        return ManaFlask(**_flask[name])
    else:
        return QuestItem(**_quest[name])
