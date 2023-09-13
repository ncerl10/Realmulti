#importing from other files
from armour import *
from weapon import *
from accessory import *
from spell import *
from item import *


class Enemy:
    """The parent class for an enemy

    Attributes
    ----------
    - name : str
      Name of the enemy
    - health : int
      Amount of health the enemy has
    - attack : int
      Amount of damage the enemy deals
    - loot : Item
      The loot the enemy drops when killed
    - description : str
      Description of the enemy
    - move : str
      Description of the enemy's attack

    Methods
    -------
    None
    """

    def __init__(self,
                 name: str,
                 description: str,
                 health: int,
                 attack: int,
                 move: str,
                 loot) -> None:
        self.name = name
        self.description = description
        self.health = health
        self.attack = attack
        self.move = move
        self.loot = loot



class TheRadiance(Enemy):
    """
    An enemey that inherits from the Enemy class
    """

    def __init__(self):
        super().__init__()
        self.set_name("The Radiance")
        self.set_health(20)
        self.set_description(
            "a higher being of light similar to Essence, and as such, opposed to the Void, her ancient enemy. The Moth Tribe is born from her light and in return revered her."
        )
        self.set_attack(2)
        self.set_move("Wall of Light")
        self.set_loot(VengefulSpirit())


class MrOshiro(Enemy):
    """
    An enemey that inherits from the Enemy class
    """

    def __init__(self):
        super().__init__()
        self.set_name("Mr Oshiro")
        self.set_health(80)
        self.set_description(
            "a well-meaning but tormented ghostly hotel owner in Celeste, haunted by his past and struggling to maintain his crumbling establishment"
        )
        self.set_attack(8)
        self.set_move("Charge")
        self.set_loot(GoldenFeather())


class TheHighDragun(Enemy):
    """
    An enemey that inherits from the Enemy class
    """

    def __init__(self):
        super().__init__()
        self.set_name("The High Dragun")
        self.set_health(80)
        self.set_description(
            "a powerful dragon armed to the teeth with an array of deadly attacks and a formidable challenge for any gungeoneer"
        )
        self.set_attack(15)
        self.set_move("Bullet Stream")
        self.set_loot(MasterRound())


class GodrickTheGrafted(Enemy):
    """
    An enemey that inherits from the Enemy class
    """

    def __init__(self):
        super().__init__()
        self.set_name("Godrick The Grafted")
        self.set_health(170)
        self.set_description(
            "a grotesque and formidable boss, a creature amalgamation of flesh and metal that presents a formidable challenge to you with his overwhelming power and monstrous appearance"
        )
        self.set_attack(25)
        self.set_move("Dragon Arm")
        self.set_loot(GlintstoneCometshard())


class Glados(Enemy):
    """
    An enemey that inherits from the Enemy class
    """

    def __init__(self):
        super().__init__()
        self.set_name("Glados")
        self.set_health(150)
        self.set_description(
            "a malevolent AI antagonist, known for her dark sense of humor and penchant for testing subjects with life-threatening puzzles"
        )
        self.set_attack(20)
        self.set_move("Neurotoxin Gas")
        self.set_loot(PortalGun())


class Yaldabaoth(Enemy):
    """
    An enemey that inherits from the Enemy class
    """

    def __init__(self):
        super().__init__()
        self.set_name("Yaldabaoth")
        self.set_health(100)
        self.set_description(
            "an imposing and god-like antagonist, representing the oppressive control and distorted order imposed upon society"
        )
        self.set_attack(15)
        self.set_move("Divine Punishment")
        self.set_loot(Megidolaon())


class Ridley(Enemy):
    """
    An enemey that inherits from the Enemy class
    """

    def __init__(self):
        super().__init__()
        self.set_name("Ridley")
        self.set_health(500)
        self.set_description(
            "a fearsome space pirate leader and recurring antagonist, known for his ruthless cruelty and iconic draconic appearance"
        )
        self.set_attack(45)
        self.set_move("Fireball")
        self.set_loot(PowerSuit())


class Emil(Enemy):
    """
    An enemey that inherits from the Enemy class
    """

    def __init__(self):
        super().__init__()
        self.set_name("Emil")
        self.set_health(400)
        self.set_description(
            "a nightmarish and relentless foe, with multiple heads and powerful attacks"
        )
        self.set_attack(40)
        self.set_move("Emil Clones")
        self.set_loot(VirtuousTreaty())


class TheBoneHyrda(Enemy):
    """
    An enemey that inherits from the Enemy class
    """

    def __init__(self):
        super().__init__()
        self.set_name("The Bone Hydra")
        self.set_health(150)
        self.set_description(
            "a fearsome and multi-headed boss, a relentless adversary that guards the underworld's entrance and challenges you with its deadly attacks."
        )
        self.set_attack(20)
        self.set_move("Ground Slam")
        self.set_loot(Coronacht())


class GeneralMugen(Enemy):
    """
    An enemey that inherits from the Enemy class
    """

    def __init__(self):
        super().__init__()
        self.set_name("General Mugen")
        self.set_health(350)
        self.set_description(
            "a formidable and ruthless military leader, known for his strategic prowess and unwavering dedication to his nation's conquest"
        )
        self.set_attack(35)
        self.set_move("Ordained Punishment")
        self.set_loot(DragonMail())


class DoctorEggman(Enemy):
    """
    An enemey that inherits from the Enemy class
    """

    def __init__(self):
        super().__init__()
        self.set_name("Doctor Eggman")
        self.set_health(200)
        self.set_description(
            "a brilliant yet perpetually thwarted scientist with a penchant for constructing nefarious machines and plots to conquer the world"
        )
        self.set_attack(20)
        self.set_move("his Robot Army")
        self.set_loot(ChaosEmerald())


class TheMoonLord(Enemy):
    """
    An enemey that inherits from the Enemy class
    """

    def __init__(self):
        super().__init__()
        self.set_name("The Moon Lord")
        self.set_health(300)
        self.set_description(
            "a towering eldritch entity with a menacing appearance and an array of devastating attacks that challenge you to your limits"
        )
        self.set_attack(30)
        self.set_move("Phantasmal Eyes")
        self.set_loot(Zenith())


class Mithrix(Enemy):
    """
    An enemey that inherits from the Enemy class
    """

    def __init__(self):
        super().__init__()
        self.set_name("Mithrix")
        self.set_health(120)
        self.set_description(
            "a vengeful and godlike being with the power to manipulate time and space, posing a significant threat to whoever attempts to escape"
        )
        self.set_attack(20)
        self.set_move("Lunar Hammer Smash")
        self.set_loot(WillOTheWisp())


class Sephiroth(Enemy):
    """
    An enemey that inherits from the Enemy class
    """

    def __init__(self):
        super().__init__()
        self.set_name("Sephiroth")
        self.set_health(20)
        self.set_description(
            "a brooding and immensely powerful warrior with a deep-seated desire to harness the destructive force of the planet for his own malevolent purposes"
        )
        self.set_attack(10)
        self.set_move("Super Nova")
        self.set_loot(BusterSword())


class Ganondorf(Enemy):
    """
    An enemey that inherits from the Enemy class
    """

    def __init__(self):
        super().__init__()
        self.set_name("Ganondorf")
        self.set_health(20)
        self.set_description(
            "a malevolent Gerudo sorcerer who seeks to obtain the Triforce's power and plunge Hyrule into darkness and chaos"
        )
        self.set_attack(10)
        self.set_move("Dark Magic")
        self.set_loot(MasterSword())


class TheEnderDragon(Enemy):
    """
    An enemey that inherits from the Enemy class
    """

    def __init__(self):
        super().__init__()
        self.set_name("The Ender Dragon")
        self.set_health(20)
        self.set_description(
            "a fearsome and colossal winged creature that challenges you with its destructive abilities and formidable strength"
        )
        self.set_attack(10)
        self.set_move("Dragon's breath")
        self.set_loot(NetheriteArmour())


class Shibusawa(Enemy):
    """
    An enemey that inherits from the Enemy class
    """

    def __init__(self):
        super().__init__()
        self.set_name("Shibusawa")
        self.set_health(20)
        self.set_description(
            "a ruthless and power-hungry underworld figure who manipulates events to achieve his sinister goals within the criminal landscape of Kamurocho"
        )
        self.set_attack(10)
        self.set_move("Beast Style")
        self.set_loot(DragonAmulet())


class Enchantress(Enemy):
    """
    An enemey that inherits from the Enemy class
    """

    def __init__(self):
        super().__init__()
        self.set_name("Enchantress")
        self.set_health(20)
        self.set_description(
            "a mastermind behind the Order of No Quarter, shrouded in mystery and wielding dark magic"
        )
        self.set_attack(10)
        self.set_move("Pyrokinetic Flames")
        self.set_loot(OrnatePlate())


class Freya(Enemy):
    """
    An enemey that inherits from the Enemy class
    """

    def __init__(self):
        super().__init__()
        self.set_name("Freya")
        self.set_health(20)
        self.set_description(
            "a formidable and relentless adversary, harnessing her powerful magic and fierce determination to protect her son, Baldur"
        )
        self.set_attack(10)
        self.set_move("Thamur")
        self.set_loot(LeviathanAxe())


class Reyna(Enemy):
    """
    An enemey that inherits from the Enemy class
    """

    def __init__(self):
        super().__init__()
        self.set_name("Reyna")
        self.set_health(100)
        self.set_description(
            "a deadly duelist agent with the ability to absorb the souls of defeated enemies, empowering herself to become an even more formidable threat on the battlefield"
        )
        self.set_attack(10)
        self.set_move("Reaver Vandal")
        self.set_loot(RGXButterflyKnife())


class Voldemort(Enemy):
    """
    An enemey that inherits from the Enemy class
    """

    def __init__(self):
        super().__init__()
        self.set_name("Voldemort")
        self.set_health(1000)
        self.set_description(
            "a malevolent dark wizard, seeking power and immortality while spreading fear and chaos throughout the wizarding world"
        )
        self.set_attack(60)
        self.set_move("Avada Kedavra")
        self.set_loot(ElderWand())


class Gabriel(Enemy):
    """
    An enemey that inherits from the Enemy class
    """

    def __init__(self):
        super().__init__()
        self.set_name("Gabriel, Apostate of Hate")
        self.set_health(200)
        self.set_description(
            "a seething red angelic crusader wielding twin swords, desperate to prove himself to the council"
        )
        self.set_attack(20)
        self.set_move("Sword Throw")
        self.set_loot(MarksmanRevolver())


class Flowey(Enemy):
    """
    An enemey that inherits from the Enemy class
    """

    def __init__(self):
        super().__init__()
        self.set_name("Flowey")
        self.set_health(350)
        self.set_description(
            "a malevolent flower with a cunning and manipulative personality")
        self.set_attack(35)
        self.set_move("Flamethrower")
        self.set_loot(ToyKnife())


class TheHeir(Enemy):
    """
    An enemey that inherits from the Enemy class
    """

    def __init__(self):
        super().__init__()
        self.set_name("The Heir")
        self.set_health(400)
        self.set_description(
            "a formidable and relentless opponent, putting the your combat skills to the test in a challenging battle within its enchanting yet treacherous world."
        )
        self.set_attack(40)
        self.set_move("Dark Energy")
        self.set_loot(HolyCross())


class JenaAnderson(Enemy):
    """
    An enemey that inherits from the Enemy class
    """

    def __init__(self):
        super().__init__()
        self.set_name("Jena Anderson")
        self.set_health(400)
        self.set_description(
            "a formidable and challenging adversary, wielding her scientific knowledge and powerful Legion to confront you in an intense battle."
        )
        self.set_attack(40)
        self.set_move("Legion")
        self.set_loot(XBaton())


class TheKraken(Enemy):
    """
    An enemey that inherits from the Enemy class
    """

    def __init__(self):
        super().__init__()
        self.set_name("The Kraken")
        self.set_health(300)
        self.set_description(
            "a massive tentacled sea monster that terrorised the ill-fated crew of the ship"
        )
        self.set_attack(30)
        self.set_move("Tentacles")
        self.set_loot(MementoMortem())


class Bowser(Enemy):
    """
    An enemey that inherits from the Enemy class
    """

    def __init__(self):
        super().__init__()
        self.set_name("Bowser")
        self.set_health(300)
        self.set_description(
            "the king koopa with a imposing stature and fire-breathing abilities"
        )
        self.set_attack(30)
        self.set_move("Koopa Army")
        self.set_loot(Cappy())
