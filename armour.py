class Armour:
    """The parent class for an armour

    Attributes
    ----------
    - type : str
      Type of the item picked up
    - name : str
      Name of the armour
    - description : str
      Description of the armour
    - defence : int
      Numerical value added to the defence of the the character

    Methods
    -------
    None
    """

    def __init__(self,
                 name: str,
                 description: str,
                 *,  # all parameters below this line are keyword arguments
                 defence: int = 0) -> None:
        self.type = "armour"
        self.name = name
        self.description = description
        self.defence = defence


class NetheriteArmour(Armour):
    """
    An armour that inherits from the Armour class
    """

    def __init__(self):
        super().__init__()
        self.set_defence(10)
        self.set_name("Netherite Armour")
        self.set_description(
            f"Netherite Armour is crafted by combining diamond armor with Netherite ingots, it offers increased damage resistance and durability\nProvides {self.get_defence()} defence"
        )


class OrnatePlate(Armour):
    """
    An armour that inherits from the Armour class
    """

    def __init__(self):
        super().__init__()
        self.set_defence(15)
        self.set_name("Ornate Plate")
        self.set_description(
            f"Ornate Plate is a regal and decorative suit of armor that not only enhances the player's defense but also adds a touch of grandeur to their appearance\nProvides {self.get_defence()} defence"
        )


class PowerSuit(Armour):
    """
    An armour that inherits from the Armour class
    """

    def __init__(self):
        super().__init__()
        self.set_defence(30)
        self.set_name("Power Suit")
        self.set_description(
            f"The Power Suit provides exceptional protection enabling you to navigate the treacherous alien landscapes and combat formidable foes encountered throughout your missions\nProvides {self.get_defence()} defence"
        )


class DragonMail(Armour):
    """
    An armour that inherits from the Armour class
    """

    def __init__(self):
        super().__init__()
        self.set_defence(20)
        self.set_name("Dragon Mail")
        self.set_description(
            f"Dragon Mail is a legendary and formidable piece of armor that offers exceptional defense and protection for the wearer. It features dragon-scale motifs, reflecting its durability and resistance to various forms of damage\nProvides {self.get_defence()} defence"
        )


class Cappy(Armour):
    """
    An armour that inherits from the Armour class
    """

    def __init__(self):
        super().__init__()
        self.set_defence(25)
        self.set_name("Cappy")
        self.set_description(
            f"Cappy is a sentient, shape-shifting hat with the ability to possess objects and enemies\nProvides {self.get_defence()} defence"
        )
