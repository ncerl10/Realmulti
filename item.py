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


def health_flask(count: int = 0) -> HealthFlask:
    return HealthFlask(
        name="Flask of Crimson Tears",
        description="A sacred flask modelled after a golden holy chalice that was once graced by a tear of life.",
        count=count,
        health=50,
    )


def mana_flask(count: int = 0) -> ManaFlask:
    return ManaFlask(
        name="Flask of Cerulean Tears",
        description="A sacred flask modelled after a golden holy chalice that was once graced by a tear of life.",
        count=count,
        mana=50,
    )


_quest_items = {
    "DectusMedallionRight": QuestItem(
        name="Dectus Medallion (right)",
        description="The right half of a medallion with the power to break a powerful spell",
    ),
    "DectusMedallionLeft": QuestItem(
        name="Dectus Medallion (left)",
        description="The left half of a medallion with the power to break a powerful spell",
    ),
}

def get_quest_item(name: str) -> QuestItem:
    return _quest_items[name]