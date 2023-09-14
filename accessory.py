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
    - effect: str
      The effect that the item has
      
    Methods
    -------
    - effect() -> str
      Describes the effect of the item
        """

    def __init__(self,
                 name: str,
                 description: str,
                 effect: str,
                 *,  # all parameters below this line are keyword arguments
                 health_boost: int = 0,
                 attack_boost: int = 0,
                 mana_boost: int = 0,
                 defence_boost: int = 0) -> None:
        self.type = "accessory"
        self.name = name
        self.description = description
        self.effect = effect
        self.health_boost = health_boost
        self.attack_boost = attack_boost
        self.mana_boost = mana_boost
        self.defence_boost = defence_boost
        

    def effect(self) -> str:
        raise NotImplementedError


def GoldenFeather() -> Accessory:
    return Accessory(
            name="Golden Feather",
            description="The Golden Feather is a coveted and shimmering collectible that enhances your mobility. Its radiant appearance and unique functionality make it a symbol of progress and determination",
        effect="Boost mana by 30 points",
        mana_boost=30,        
    )
        

def MasterRound() -> Accessory:
    return Accessory(
        name="Master Round",
        description="The Master Round is a prestigious and rare item that boost the player's health and also serve as a symbol of their mastery of challenging battles",
        effect="Boost health by 30 points",
        health_boost=30,
    )


def DragonAmulet() -> Accessory:
    return Accessory(
        name="Dragon Amulet",
        description="The Dragon Amulet is a prized and ornate accessory and a symbol of membership in the Dojima Family. It features a dragon motif that represents a connection to the Yakuza world",
        effect="Boost attack by 20 points",
        attack_boost=20,
    )
        

def ChaosEmerald() -> Accessory:
    return Accessory(
        name="Chaos Emerald",
        description="The Chaos Emerald is a mystical, multicolored gemstone of immense power. The gemstones is known for its ability to grant incredible abilities, including the power of super transformation",
        effect="Boost health by 20 points\nBoost mana by 10 points",
        health_boost=20,
        mana_boost=10,
    )


def HolyCross() -> Accessory:
    return Accessory(
        name="Holy Cross",
        description="The Holy Cross powerful, sacred artifact that bestows unique abilities upon the player",
        effect="Boost defence by 20 points",
        defence_boost=20,
    )


def MementoMortem() -> Accessory:
    return Accessory(
        name="Memento Mortem",
        description="The Memento Mortem is a mystical pocket watch that allows the user to view the moment of a person's death",
        effect="Boost mana by 20 points\nBoost defence by 10 points",
        mana_boost=20,
        defence_boost=10,
    )
