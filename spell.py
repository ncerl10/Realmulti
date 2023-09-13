class Spell:
    """
    The parent class for a spell

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
    + get_type(self) -> str
    + set_name(self, name : str) -> None
    + get_name(self) -> str
    + set_description(self, description : str) -> None
    + get_description(self) -> str
    + set_attack(self, attack : int) -> None
    + get_attack(self) -> int
    + set_cost(self, cost : int) -> None
    + get_cost(self) -> int
    + set_move(self, move : str) -> None
    + get_move(self) -> str
    + set_win_front(self, win_front : str) -> None
    + get_win_front(self) -> str
    + set_win_back(self, win_back : str) -> None
    + get_win_back(self) -> str
    """

    def __init__(self) -> None:
        self.type = "spell"
        self.name = ""
        self.description = ""
        self.attack = 0
        self.cost = 0
        self.move = ""
        self.win_front = ""
        self.win_back = ""

    def get_type(self) -> str:
        """gets the type of the spell"""
        return self.type

    def set_name(self, name: str) -> None:
        """updates the name of the spell"""
        self.name = name

    def get_name(self) -> str:
        """gets the name of the spell"""
        return self.name

    def set_description(self, description: str) -> None:
        """updates the description of the spell"""
        self.description = description

    def get_description(self) -> str:
        """gets the description of the spell"""
        return self.description

    def set_attack(self, attack: int) -> None:
        """updates the amount of damage the spell does"""
        self.attack = attack

    def get_attack(self) -> int:
        """gets the amount of damage the spell does"""
        return self.attack

    def set_cost(self, cost: int) -> None:
        """updates the the amount of mana the spell uses"""
        self.cost = cost

    def get_cost(self) -> int:
        """gets the the amount of mana the spell uses"""
        return self.cost

    def set_move(self, move: str) -> None:
        """updates the name of the attack of the spell"""
        self.move = move

    def get_move(self) -> str:
        """gets the name of the attack of the spell"""
        return self.move

    def set_win_front(self, win_front: str) -> None:
        """updates the the front half of the spell's killing message"""
        self.win_front = win_front

    def get_win_front(self) -> str:
        """gets the the front half of the spell's killing message"""
        return self.win_front

    def set_win_back(self, win_back: str) -> None:
        """updates the the back half of the spell's killing message"""
        self.win_back = win_back

    def get_win_back(self) -> str:
        """gets the the back half of the spell's killing message"""
        return self.win_back


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
