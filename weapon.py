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


def BusterSword() -> Weapon:
    return Weapon(
        name="Buster Sword",
        description="The Buster Sword is an enormous broadsword. From tip to handle, it is approximately five to six feet long, with a single-edged large blade approximately one foot wide\nDeals 10 damage",
        attack=10,
        move=" used Focused Thrust",
        win_front=" used braver and smashed ",
        win_back=" into the ground"
    )

def MasterSword() -> Weapon:
    return Weapon(
        name="Master Sword",
        description="The Master Sword is a divine magic sword with the power to vanquish evil. Infused with the sacred flames provided by the Golden Goddesses and blessed with Hylia's power\nDeals 10 damage",
        attack=10,
        move=" used Sword beam",
        win_front=" used the power of the triforce to vanquish ",
        win_back=" from the face of the earth"
    )

def LeviathanAxe() -> Weapon:
    return Weapon(
        name="Leviathan Axe",
        description="The Leviathan axe legendary two-handed battle axe imbuded with elemental magic allowing it to return to the user\nDeals 40 damage",
        attack=40,
        move=" threw the Leviathan Axe",
        win_front=" lunged towards ",
        win_back=" and decapitated it"
    )

def PortalGun() -> Weapon:
    return Weapon(
        name="Portal Gun",
        description="The Portal Gun is a hand-held device which has the ability to manufacture two linked portals. No matter the distance between them, any object which passes through one portal will emerge from the other and vice versa instantaneously\nDeals 40 damage",
        attack=40,
        move=" used portals",
        win_front=" used a portal to send ",
        win_back=" to the moon"
    )

def VirtuousTreaty() -> Weapon:
    return Weapon(
        name="Virtuous Treaty",
        description="The Virtuous Treaty is a pure white samurai blade not sullied by a single drop of blood\nDeals 50 damage",
        attack=50,
        move=" used Virtuous Treaty",
        win_front=" struck ",
        win_back=" down in one clean slash"
    )

def Coronacht() -> Weapon:
    return Weapon(
        name="Coronacht",
        description="The Coronacht is an infernal arm, the finest bow ever concevied, once weilded by Mistress Hera\nDeals 60 damage",
        attack=60,
        move=" used power shot",
        win_front=" used the aspect of Hera to shoot a power shot right through ",
        win_back=""
    )

def Zenith() -> Weapon:
    return Weapon(
        name="Zenith",
        description="The Zenith is a legendary blade crafted using 10 different powerful swords\nDeals 70 damage",
        attack=70,
        move=" used The Zenith",
        win_front=" obliterated ",
        win_back=" using the power of 10 swords"
    )

def RGXButterflyKnife() -> Weapon:
    return Weapon(
        name="RGX Butterfly Knife",
        description="The RGX Butterfly Knife is the most powerful butterfly knife on earth due to its RGB\nDeals 60 damage",
        attack=60,
        move=" used behind the 8 ball",
        win_front=" performed the valorant inspect flawlessly causing ",
        win_back=" to self destruct"
    )

def ElderWand() -> Weapon:
    return Weapon(
        name="Elder Wand",
        description="The most powerful wand on earth",
        attack=10,
        move="",
        win_front="",
        win_back=""
    )

def Wand() -> Weapon:
    return Weapon(
        name="Wand",
        description="A generic wand\nDeals 5 damage",
        attack=5,
        move=" threw the wand",
        win_front=" poked ",
        win_back=" to death"
    )

def MarksmanRevolver() -> Weapon:
    return Weapon(
        name="Marksman Revolver",
        description="A revolver. Every few seconds a coin pops out of the bottom of the gun. The purpose of this function is lost on you\nDeals 50 damage",
        attack=50,
        move=" used +HEADSHOT",
        win_front=" threw $4.32 of change at ",
        win_back=", knocking it out"
    )

def ToyKnife() -> Weapon:
    return Weapon(
        name="Toy Knife",
        description="Made of plastic. A rarity nowadays\nDeals 1 damage",
        attack=1,
        move=" used stab",
        win_front=" stabbed ",
        win_back=" so much it died"
    )

def XBaton() -> Weapon:
    return Weapon(
        name="X Baton",
        description="The X Baton is a police baton capable of transforming between three different styles, each with their own unique abilities and merits\nDeals 100 damage",
        attack=100,
        move=" used blaster mode",
        win_front=" activated Gladius Mode and decimated ",
        win_back=""
    )
