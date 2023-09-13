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


class WingardiumLeviosa(Spell):
    """
    A spell that inherits from the Spell class
    """

    def __init__(self):
        super().__init__()
        self.set_name("Wingardium Leviosa")
        self.set_attack(10)
        self.set_cost(5)
        self.set_description(
            f"Wingardium Leviosa is a magic spell that can make objects levitate\nDeals {self.get_attack()} damage\nCost {self.get_cost()} mana"
        )
        self.set_move(" used levitation")
        self.set_win_front(" levitated ")
        self.set_win_back(
            " so high that it breached the atmosphere and exploded")


class VengefulSpirit(Spell):
    """
    A spell that inherits from the Spell class
    """

    def __init__(self):
        super().__init__()
        self.set_name("Vengeful Spirit")
        self.set_attack(20)
        self.set_cost(10)
        self.set_description(
            f"Vengeful spirit is a spirit that will fly forward and burn foes in its path\nDeals {self.get_attack()} damage\nCost {self.get_cost()} mana"
        )
        self.set_move(" used Vengeful Spirit")
        self.set_win_front(
            " charged up all your soul and shot a massive vengeful spirit at ")
        self.set_win_back("")


class Megidolaon(Spell):
    """
    A spell that inherits from the Spell class
    """

    def __init__(self):
        super().__init__()
        self.set_name("Megidolaon")
        self.set_attack(30)
        self.set_cost(20)
        self.set_description(
            f"Megidolaon is a damage dealing almighty spell\nDeals {self.get_attack()} damage\nCost {self.get_cost()} mana"
        )
        self.set_move(" used Megidolaon")
        self.set_win_front(
            " summoned your persona Satanael and dealt massive almighty damage to "
        )
        self.set_win_back("")


class GlintstoneCometshard(Spell):
    """
    A spell that inherits from the Spell class
    """

    def __init__(self):
        super().__init__()
        self.set_name("Glintstone Cometshard")
        self.set_attack(40)
        self.set_cost(25)
        self.set_description(
            f"Glintstone Cometshard fires a comet that moves forward while leaving a trail\nDeals {self.get_attack()} damage\nCost {self.get_cost()} mana"
        )
        self.set_move(" shot a Glinstone Cometshard")
        self.set_win_front(" Shredded ")
        self.set_win_back(" into a million pieces")


class WillOTheWisp(Spell):
    """
    A spell that inherits from the Spell class
    """

    def __init__(self):
        super().__init__()
        self.set_name("Will O The Wisp")
        self.set_attack(50)
        self.set_cost(30)
        self.set_description(
            f"Will O The Wisp causes the enemy to explode\nDeals {self.get_attack()} damage\nCost {self.get_cost()} mana"
        )
        self.set_move(" exploded")
        self.set_win_front(" exploded ")
        self.set_win_back(" until it burnt to a crisp")
