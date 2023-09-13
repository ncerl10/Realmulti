class Item:
    """
    The parent class for an item

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
    + set_name(self, name : str) -> None
    + get_name(self) -> str
    + set_description(self) -> None
    + get_description(self, description : str) -> str
    + set_health(self, health : int) -> None
    + get_health(self, health : int) -> int
    + set_mana(self, mana : int) -> None
    + get_mana(self, mana : int) -> int
    """

    def __init__(self):
        self.name = ""
        self.description = ""
        self.health = 0
        self.mana = 0

    def set_name(self, name: str) -> None:
        """updates the name of the item"""
        self.name = name

    def get_name(self):
        """gets the name of the item"""
        return self.name

    def set_description(self, description):
        """updates the description of the item"""
        self.description = description

    def get_description(self):
        """gets the description of the item"""
        return self.description

    def set_health(self, health):
        """updates the health of the item"""
        self.health = health

    def get_health(self):
        """gets the health of the item"""
        return self.health

    def set_mana(self, mana):
        """updates the mana of the item"""
        self.mana = mana

    def get_mana(self):
        """gets the mana of the item"""
        return self.mana


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
