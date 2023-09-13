class Item:
    """    The parent class for an item

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
                 description: str,
                 health: int,
                 mana: int):
        self.name = name
        self.description = description
        self.health = health
        self.mana = mana


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
