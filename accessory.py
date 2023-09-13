class Accessory:
    """The parent class for an accessory

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
    None
    """

    def __init__(self,
                 name: str,
                 description: str,
                 *,  # all parameters below this line are keyword arguments
                 health_boost: int = 0,
                 attack_boost: int = 0,
                 mana_boost: int = 0,
                 defence_boost: int = 0) -> None:
        self.type = "accessory"
        self.name = name
        self.descripton = description
        self.health_boost = health_boost
        self.attack_boost = attack_boost
        self.mana_boost = mana_boost
        self.defence_boost = defence_boost


class GoldenFeather(Accessory):
    """
    An accessory that inherits from the Accessory class
    """

    def __init__(self):
        super().__init__()
        self.set_name("Golden Feather")
        self.set_mana_boost(30)
        self.set_description(f"The Golden Feather is a coveted and shimmering collectible that enhances your mobility. Its radiant appearance and unique functionality make it a symbol of progress and determination\nBoost mana by {self.get_mana_boost()} points")
        

class MasterRound(Accessory):
    """
    An accessory that inherits from the Accessory class
    """

    def __init__(self):
        super().__init__()
        self.set_name("Master Round")
        self.set_health_boost(30)
        self.set_description(f"The Master Round is a prestigious and rare item that boost the player's health and also serve as a symbol of their mastery of challenging battles\nBoost health by {self.get_health_boost()} points")

class DragonAmulet(Accessory):
    """
    An accessory that inherits from the Accessory class
    """

    def __init__(self):
        super().__init__()
        self.set_name("Dragon Amulet")
        self.set_attack_boost(20)
        self.set_description(f"The Dragon Amulet is a prized and ornate accessory and a symbol of membership in the Dojima Family. It features a dragon motif that represents a connection to the Yakuza world\nBoost attack by {self.get_attack_boost()} points")
        

class ChaosEmerald(Accessory):
    """
    An accessory that inherits from the Accessory class
    """

    def __init__(self):
        super().__init__()
        self.set_name("Chaos Emerald")
        self.set_health_boost(20)
        self.set_mana_boost(10)
        self.set_description(f"The Chaos Emerald is a mystical, multicolored gemstone of immense power. The gemstones is known for its ability to grant incredible abilities, including the power of super transformation\nBoost health by {self.get_health_boost()} points\nBoost mana by {self.get_mana_boost()} points")

class HolyCross(Accessory):
    """
    An accessory that inherits from the Accessory class
    """

    def __init__(self):
        super().__init__()
        self.set_name("Holy Cross")
        self.set_defence_boost(20)
        self.set_description(f"The Holy Cross powerful, sacred artifact that bestows unique abilities upon the player\nBoost defence by {self.get_defence_boost()} points")

class MementoMortem(Accessory):
    """
    An accessory that inherits from the Accessory class
    """

    def __init__(self):
        super().__init__()
        self.set_name("Memento Mortem")
        self.set_mana_boost(20)
        self.set_defence_boost(10)
        self.set_description(f"The Memento Mortem is a mystical pocket watch that allows the user to view the moment of a person's death\nBoost mana by {self.get_mana_boost()} points\nBoost defence by {self.get_defence_boost()} points")

