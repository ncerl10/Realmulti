class Accessory:
    """
    The parent class for an accessory

    Attributes
    ----------
    - type : str
      Type of the item picked up
    - name : str
      Name of the accessory
    - description : str
      Description of the accessory
    - health_boost : int
      Numerical value added to the health of the the character
    - attack_boost : int
      Numerical value added to the attack of the the character
    - mana_boost : int
      Numerical value added to the mana of the the character
    - defence_boost : int
      Numerical value added to the defence of the the character
      
    Methods
    -------
    + get_type(self) -> str
    + set_name(self, name : str) -> None
    + get_name(self) -> str
    + set_description(self) -> None
    + get_description(self, description : str) -> str
    + set_health_boost(self) -> None
    + get_health_boost(self, health_boost : int) -> int
    + set_attack_boost(self) -> None
    + get_attack_boost(self, attack_boost : int) -> int
    + set_mana_boost(self) -> None
    + get_mana_boost(self, mana_boost : int) -> int
    + set_defence_boost(self) -> None
    + get_defence_boost(self, defence_boost : int) -> int
    """

    def __init__(self) -> None:
        self.type = "accessory"
        self.name = ""
        self.descripton = ""
        self.health_boost = 0
        self.attack_boost = 0
        self.mana_boost = 0
        self.defence_boost = 0

    def get_type(self) -> str:
        """gets the type of the accessory"""
        return self.type

    def set_name(self, name: str) -> None:
        """updates the name of the accessory"""
        self.name = name

    def get_name(self) -> str:
        """gets the name of the accessory"""
        return self.name

    def set_description(self, description: str) -> None:
        """updates the description of the accessory"""
        self.description = description

    def get_description(self) -> str:
        """gets the description of the accessory"""
        return self.description

    def set_health_boost(self, health_boost: int) -> None:
        """updates the health_boost of the accessory"""
        self.health_boost = health_boost

    def get_health_boost(self) -> int:
        """gets the health_boost of the accessory"""
        return self.health_boost

    def set_attack_boost(self, attack_boost: int) -> None:
        """updates the attack_boost of the accessory"""
        self.attack_boost = attack_boost

    def get_attack_boost(self) -> int:
        """gets the attack_boost of the accessory"""
        return self.attack_boost

    def set_mana_boost(self, mana_boost: int) -> None:
        """updates the mana_boost of the accessory"""
        self.mana_boost = mana_boost

    def get_mana_boost(self) -> int:
        """gets the mana_boost of the accessory"""
        return self.mana_boost

    def set_defence_boost(self, defence_boost: int) -> None:
        """updates the defence_boost of the accessory"""
        self.defence_boost = defence_boost

    def get_defence_boost(self) -> int:
        """gets the defence_boost of the accessory"""
        return self.defence_boost


class GoldenFeather(Accessory):
    """
    An accessory that inherits from the Accessory class
    """

    def __init__(self):
        super().__init__()
        self.set_name("Golden Feather")
        self.set_mana_boost(30)
        self.set_description(
            f"The Golden Feather is a coveted and shimmering collectible that enhances your mobility. Its radiant appearance and unique functionality make it a symbol of progress and determination\nBoost mana by {self.get_mana_boost()} points"
        )


class MasterRound(Accessory):
    """
    An accessory that inherits from the Accessory class
    """

    def __init__(self):
        super().__init__()
        self.set_name("Master Round")
        self.set_health_boost(30)
        self.set_description(
            f"The Master Round is a prestigious and rare item that boost the player's health and also serve as a symbol of their mastery of challenging battles\nBoost health by {self.get_health_boost()} points"
        )


class DragonAmulet(Accessory):
    """
    An accessory that inherits from the Accessory class
    """

    def __init__(self):
        super().__init__()
        self.set_name("Dragon Amulet")
        self.set_attack_boost(20)
        self.set_description(
            f"The Dragon Amulet is a prized and ornate accessory and a symbol of membership in the Dojima Family. It features a dragon motif that represents a connection to the Yakuza world\nBoost attack by {self.get_attack_boost()} points"
        )


class ChaosEmerald(Accessory):
    """
    An accessory that inherits from the Accessory class
    """

    def __init__(self):
        super().__init__()
        self.set_name("Chaos Emerald")
        self.set_health_boost(20)
        self.set_mana_boost(10)
        self.set_description(
            f"The Chaos Emerald is a mystical, multicolored gemstone of immense power. The gemstones is known for its ability to grant incredible abilities, including the power of super transformation\nBoost health by {self.get_health_boost()} points\nBoost mana by {self.get_mana_boost()} points"
        )


class HolyCross(Accessory):
    """
    An accessory that inherits from the Accessory class
    """

    def __init__(self):
        super().__init__()
        self.set_name("Holy Cross")
        self.set_defence_boost(20)
        self.set_description(
            f"The Holy Cross powerful, sacred artifact that bestows unique abilities upon the player\nBoost defence by {self.get_defence_boost()} points"
        )


class MementoMortem(Accessory):
    """
    An accessory that inherits from the Accessory class
    """

    def __init__(self):
        super().__init__()
        self.set_name("Memento Mortem")
        self.set_mana_boost(20)
        self.set_defence_boost(10)
        self.set_description(
            f"The Memento Mortem is a mystical pocket watch that allows the user to view the moment of a person's death\nBoost mana by {self.get_mana_boost()} points\nBoost defence by {self.get_defence_boost()} points"
        )
