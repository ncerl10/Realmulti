class Weapon:
    """The parent class for a weapon

    Attributes
    ----------
    - type : str
      Type of the item picked up
    - name : str
      Name of the weapon
    - description : str
      Description of the weapon
    - attack : int
      Numerical value added to the attack of the the character
    - move : str
      Name of the weapon's attack
    - win_front : str
      The front half of the weapon's killing message
    - win_back : str
      The back half of the weapon's killing message


    Methods
    -------
    None
    """

    def __init__(self,
                 name: str,
                 description: str,
                 attack: int,
                 move: str,
                 win_front: str,
                 win_back: str) -> None:
        self.type = "weapon"
        self.name = name
        self.description = description
        self.attack = attack
        self.move = move
        self.win_front = win_front
        self.win_back = win_back


class BusterSword(Weapon):
    """
    A weapon that inherits from the Weapon class
    """

    def __init__(self):
        super().__init__()
        self.set_name("Buster Sword")
        self.set_attack(10)
        self.set_description(
            f"The Buster Sword is an enormous broadsword. From tip to handle, it is approximately five to six feet long, with a single-edged large blade approximately one foot wide\nDeals {self.get_attack()} damage"
        )
        self.set_move(" used Focused Thrust")
        self.set_win_front(" used braver and smashed ")
        self.set_win_back(" into the ground")


class MasterSword(Weapon):
    """
    A weapon that inherits from the Weapon class
    """

    def __init__(self):
        super().__init__()
        self.set_name("Master Sword")
        self.set_attack(10)
        self.set_description(
            f"The Master Sword is a divine magic sword with the power to vanquish evil. Infused with the sacred flames provided by the Golden Goddesses and blessed with Hylia's power\nDeals {self.get_attack()} damage"
        )
        self.set_move(" used Sword beam")
        self.set_win_front(" used the power of the triforce to vanquish ")
        self.set_win_back(" from the face of the earth")


class LeviathanAxe(Weapon):
    """
    A weapon that inherits from the Weapon class
    """

    def __init__(self):
        super().__init__()
        self.set_name("Leviathan Axe")
        self.set_attack(40)
        self.set_description(
            f"The Leviathan axe legendary two-handed battle axe imbuded with elemental magic allowing it to return to the user\nDeals {self.get_attack()} damage"
        )
        self.set_move(" threw the Leviathan Axe")
        self.set_win_front(" lunged towards ")
        self.set_win_back(" and decapitated it")


class PortalGun(Weapon):
    """
    A weapon that inherits from the Weapon class
    """

    def __init__(self):
        super().__init__()
        self.set_name("Portal Gun")
        self.set_attack(40)
        self.set_description(
            f"The Portal Gun is a hand-held device which has the ability to manufacture two linked portals. No matter the distance between them, any object which passes through one portal will emerge from the other and vice versa instantaneously\nDeals {self.get_attack()} damage"
        )
        self.set_move(" used portals")
        self.set_win_front(" used a portal to send ")
        self.set_win_back(" to the moon")


class VirtuousTreaty(Weapon):
    """
    A weapon that inherits from the Weapon class
    """

    def __init__(self):
        super().__init__()
        self.set_name("Virtuous Treaty")
        self.set_attack(50)
        self.set_description(
            f"The Virtuous Treaty is a pure white samurai blade not sullied by a single drop of blood\nDeals {self.get_attack()} damage"
        )
        self.set_move(" used Virtuous Treaty")
        self.set_win_front(" struck ")
        self.set_win_back(" down in one clean slash")


class Coronacht(Weapon):
    """
    A weapon that inherits from the Weapon class
    """

    def __init__(self):
        super().__init__()
        self.set_name("Coronacht")
        self.set_attack(60)
        self.set_description(
            f"The Coronacht is an infernal arm, the finest bow ever concevied, once weilded by Mistress Hera\nDeals {self.get_attack()} damage"
        )
        self.set_move(" used power shot")
        self.set_win_front(
            " used the aspect of Hera to shoot a power shot right through ")
        self.set_win_back("")


class Zenith(Weapon):
    """
    A weapon that inherits from the Weapon class
    """

    def __init__(self):
        super().__init__()
        self.set_name("Zenith")
        self.set_attack(70)
        self.set_description(
            f"The Zenith is a legendary blade crafted using 10 different powerful swords\nDeals {self.get_attack()} damage"
        )
        self.set_move(" used The Zenith")
        self.set_win_front(" obliterated ")
        self.set_win_back(" using the power of 10 swords")


class RGXButterflyKnife(Weapon):
    """
    A weapon that inherits from the Weapon class
    """

    def __init__(self):
        super().__init__()
        self.set_name("RGX Butterfly Knife")
        self.set_attack(60)
        self.set_description(
            f"The RGX Butterfly Knife is the most powerful butterfly knife on earth due to its RGB\nDeals {self.get_attack()} damage"
        )
        self.set_move(" used behind the 8 ball")
        self.set_win_front(
            " performed the valorant inspect flawlessly causing ")
        self.set_win_back(" to self destruct")


class ElderWand(Weapon):
    """
    A weapon that inherits from the Weapon class
    """

    def __init__(self):
        super().__init__()
        self.set_name("Elder Wand")
        self.set_attack(10)
        self.set_description("The most powerful wand on earth")
        self.set_move("")
        self.set_win_front("")
        self.set_win_back("")


class Wand(Weapon):
    """
    A weapon that inherits from the Weapon class
    """

    def __init__(self):
        super().__init__()
        self.set_name("Wand")
        self.set_attack(5)
        self.set_description(
            f"A generic wand\nDeals {self.get_attack()} damage")
        self.set_move(" threw the wand")
        self.set_win_front(" poked ")
        self.set_win_back(" to death")


class MarksmanRevolver(Weapon):
    """
    A weapon that inherits from the Weapon class
    """

    def __init__(self):
        super().__init__()
        self.set_name("Marksman Revolver")
        self.set_attack(50)
        self.set_description(
            f"A revolver. Every few seconds a coin pops out of the bottom of the gun. The purpose of this function is lost on you\nDeals {self.get_attack()} damage"
        )
        self.set_move(" used +HEADSHOT")
        self.set_win_front(" threw $4.32 of change at ")
        self.set_win_back(", knocking it out")


class ToyKnife(Weapon):
    """
    A weapon that inherits from the Weapon class
    """

    def __init__(self):
        super().__init__()
        self.set_name("Toy Knife")
        self.set_attack(1)
        self.set_description(
            f"Made of plastic. A rarity nowadays\nDeals {self.get_attack()} damage"
        )
        self.set_move(" used stab")
        self.set_win_front(" stabbed ")
        self.set_win_back(" so much it died")


class XBaton(Weapon):
    """
    A weapon that inherits from the Weapon class
    """

    def __init__(self):
        super().__init__()
        self.set_name("X Baton")
        self.set_attack(100)
        self.set_description(
            f"The X Baton is a police baton capable of transforming between three different styles, each with their own unique abilities and merits\nDeals {self.get_attack()} damage"
        )
        self.set_move(" used blaster mode")
        self.set_win_front(" activated Gladius Mode and decimated ")
        self.set_win_back("")
