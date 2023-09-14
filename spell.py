class Spell:
    """The parent class for a spell

    Attributes
    ----------
    - type : str
      The type of spell it is
    - name : str
      Name of the spell
    - description : str
      Description of the spell
    - attack : int
      The amount of damage the spell does
    - cost : int
      The amount of mana the spell uses
    - move : str
      The name of the spell's attack
    - win_front : str
      The front half of the spell's killing message
    - win_back : str
      The back half of the spell's killing message

    Methods
    -------
    None
    """

    def __init__(self,
                 name: str,
                 description: str,
                 attack: int,
                 cost: int,
                 move: str,
                 win_front: str,
                 win_back: str) -> None:
        self.type = "spell"
        self.name = name
        self.description = description
        self.attack = attack
        self.cost = cost
        self.move = move
        self.win_front = win_front
        self.win_back = win_back


def WingardiumLeviosa() -> Spell:
    return Spell(
        name="Wingardium Leviosa",
        description="Wingardium Leviosa is a magic spell that can make objects levitate\nDeals 10 damage\nCost 5 mana",
        attack=10,
        cost=5,
        move=" used levitation",
        win_front=" levitated ",
        win_back=" so high that it breached the atmosphere and exploded"
    )

def VengefulSpirit() -> Spell:
    return Spell(
        name="Vengeful Spirit",
        description="Vengeful spirit is a spirit that will fly forward and burn foes in its path\nDeals 20 damage\nCost 10 mana",
        attack=20,
        cost=10,
        move=" used Vengeful Spirit",
        win_front=" charged up all your soul and shot a massive vengeful spirit at ",
        win_back=""
    )

def Megidolaon() -> Spell:
    return Spell(
        name="Megidolaon",
        description="Megidolaon is a damage dealing almighty spell\nDeals 30 damage\nCost 20 mana",
        attack=30,
        cost=20,
        move=" used Megidolaon",
        win_front=" summoned your persona Satanael and dealt massive almighty damage to ",
        win_back=""
    )

def GlintstoneCometshard() -> Spell:
    return Spell(
        name="Glintstone Cometshard",
        description="Glintstone Cometshard fires a comet that moves forward while leaving a trail\nDeals 40 damage\nCost 25 mana",
        attack=40,
        cost=25,
        move=" shot a Glinstone Cometshard",
        win_front=" Shredded ",
        win_back=" into a million pieces"
    )

def WillOTheWisp() -> Spell:
    return Spell(
        name="Will O The Wisp",
        description="Will O The Wisp causes the enemy to explode\nDeals 50 damage\nCost 30 mana",
        attack=50,
        cost=30,
        move=" exploded",
        win_front=" exploded ",
        win_back=" until it burnt to a crisp"
    )
