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
    """
    def __init__(self,
                 name: str,
                 description: str,
                 count: int):
        super().__init__(name, description)
        self.count = count    


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


class FlaskOfCrimsonTears(Item):
    """
    An item that inherits from the Item class
    """

    def __init__(self):
        super().__init__()
        self.set_name("Flask of Crimson Tears")
        self.set_health(50)
        self.set_description(
            f"The Flask of Crimson Tears is a sacred flask modelled after a golden holy chalice that was once graced by a tear of life\nHeals {self.get_health()} health"
        )


class FlaskOfCeruleanTears(Item):
    """
    An item that inherits from the Item class
    """

    def __init__(self):
        super().__init__()
        self.set_name("Flask of Cerulean Tears")
        self.set_mana(50)
        self.set_description(
            f"The Flask of Cerulean Tears is a sacred flask modelled after a golden holy chalice that was once graced by a tear of life\nHeals {self.get_mana()} mana"
        )


class DectusMedallionRight(Item):
    """
    An item that inherits from the Item class
    """

    def __init__(self):
        super().__init__()
        self.set_name("Dectus Medallion (right)")
        self.set_description(
            "The right half of a medallion with the power to break a powerful spell"
        )


class DectusMedallionLeft(Item):
    """
    An item that inherits from the Item class
    """

    def __init__(self):
        super().__init__()
        self.set_name("Dectus Medallion (left)")
        self.set_description(
            "The left half of a medallion with the power to break a powerful spell"
        )
