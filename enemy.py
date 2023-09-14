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

    def is_dead(self) -> bool:
        return self.health <= 0

    def take_damage(self, damage: int) -> int:
        """Minimum damage that can be dealt is 1.
        Returns the damage dealt.
        """
        if damage < 1:
            damage = 1
        self.health -= damage
        return damage


_enemy = {
    "TheRadiance": Enemy(
            name="The Radiance",
            description="a higher being of light similar to Essence, and as such, opposed to the Void, her ancient enemy. The Moth Tribe is born from her light and in return revered her.",
            health=20,
            attack=2,
            move="Wall of Light",
            loot=VengefulSpirit()
        ),    
    "MrOshiro": Enemy(
            name="Mr Oshiro",
            description="a well-meaning but tormented ghostly hotel owner in Celeste, haunted by his past and struggling to maintain his crumbling establishment",
            health=80,
            attack=8,
            move="Charge",
            loot=GoldenFeather()
        ),
    "TheHighDragun": Enemy(
            name="The High Dragun",
            description="a powerful dragon armed to the teeth with an array of deadly attacks and a formidable challenge for any gungeoneer",
            health=80,
            attack=15,
            move="Bullet Stream",
            loot=MasterRound()
        ),
    "GodrickTheGrafted": Enemy(
            name="Godrick The Grafted",
            description="a grotesque and formidable boss, a creature amalgamation of flesh and metal that presents a formidable challenge to you with his overwhelming power and monstrous appearance",
            health=170,
            attack=25,
            move="Dragon Arm",
            loot=GlintstoneCometshard()
        ),
    "Glados": Enemy(
            name="Glados",
            description="a malevolent AI antagonist, known for her dark sense of humor and penchant for testing subjects with life-threatening puzzles",
            health=150,
            attack=20,
            move="Neurotoxin Gas",
            loot=PortalGun()
        ),
    "Yaldabaoth": Enemy(
            name="Yaldabaoth",
            description="an imposing and god-like antagonist, representing the oppressive control and distorted order imposed upon society",
            health=100,
            attack=15,
            move="Divine Punishment",
            loot=Megidolaon()
        ),
    "Ridley": Enemy(
            name="Ridley",
            description="a fearsome space pirate leader and recurring antagonist, known for his ruthless cruelty and iconic draconic appearance",
            health=500,
            attack=45,
            move="Fireball",
            loot=PowerSuit()
        ),
    "Emil": Enemy(
            name="Emil",
            description="a nightmarish and relentless foe, with multiple heads and powerful attacks",
            health=400,
            attack=40,
            move="Emil Clones",
            loot=VirtuousTreaty()
        ),
    "TheBoneHyrda": Enemy(
            name="The Bone Hydra",
            description="a fearsome and multi-headed boss, a relentless adversary that guards the underworld's entrance and challenges you with its deadly attacks.",
            health=150,
            attack=20,
            move="Ground Slam",
            loot=Coronacht()
        ),
    "GeneralMugen": Enemy(
            name="General Mugen",
            description="a formidable and ruthless military leader, known for his strategic prowess and unwavering dedication to his nation's conquest",
            health=350,
            attack=35,
            move="Ordained Punishment",
            loot=DragonMail()
        ),
    "DoctorEggman": Enemy(
            name="Doctor Eggman",
            description="a brilliant yet perpetually thwarted scientist with a penchant for constructing nefarious machines and plots to conquer the world",
            health=200,
            attack=20,
            move="his Robot Army",
            loot=ChaosEmerald()
        ),
    "TheMoonLord": Enemy(
            name="The Moon Lord",
            description="a towering eldritch entity with a menacing appearance and an array of devastating attacks that challenge you to your limits",
            health=300,
            attack=30,
            move="Phantasmal Eyes",
            loot=Zenith()
        ),
    "Mithrix": Enemy(
            name="Mithrix",
            description="a vengeful and godlike being with the power to manipulate time and space, posing a significant threat to whoever attempts to escape",
            health=120,
            attack=20,
            move="Lunar Hammer Smash",
            loot=WillOTheWisp()
        ),
    "Sephiroth": Enemy(
            name="Sephiroth",
            description="a brooding and immensely powerful warrior with a deep-seated desire to harness the destructive force of the planet for his own malevolent purposes",
            health=20,
            attack=10,
            move="Super Nova",
            loot=BusterSword()
        ),
    "Ganondorf": Enemy(
            name="Ganondorf",
            description="a malevolent Gerudo sorcerer who seeks to obtain the Triforce's power and plunge Hyrule into darkness and chaos",
            health=20,
            attack=10,
            move="Dark Magic",
            loot=MasterSword()
        ),
    "TheEnderDragon": Enemy(
            name="The Ender Dragon",
            description="a fearsome and colossal winged creature that challenges you with its destructive abilities and formidable strength",
            health=20,
            attack=10,
            move="Dragon's breath",
            loot=NetheriteArmour()
        ),
    "Shibusawa": Enemy(
            name="Shibusawa",
            description="a ruthless and power-hungry underworld figure who manipulates events to achieve his sinister goals within the criminal landscape of Kamurocho",
            health=20,
            attack=10,
            move="Beast Style",
            loot=DragonAmulet()
        ),
    "Enchantress": Enemy(
            name="Enchantress",
            description="a mastermind behind the Order of No Quarter, shrouded in mystery and wielding dark magic",
            health=20,
            attack=10,
            move="Pyrokinetic Flames",
            loot=OrnatePlate()
        ),
    "Freya": Enemy(
            name="Freya",
            description="a formidable and relentless adversary, harnessing her powerful magic and fierce determination to protect her son, Baldur",
            health=20,
            attack=10,
            move="Thamur",
            loot=LeviathanAxe()
        ),
    "Reyna": Enemy(
            name="Reyna",
            description="a deadly duelist agent with the ability to absorb the souls of defeated enemies, empowering herself to become an even more formidable threat on the battlefield",
            health=100,
            attack=10,
            move="Reaver Vandal",
            loot=RGXButterflyKnife()
        ),
    "Voldemort": Enemy(
            name="Voldemort",
            description="a malevolent dark wizard, seeking power and immortality while spreading fear and chaos throughout the wizarding world",
            health=1000,
            attack=60,
            move="Avada Kedavra",
            loot=ElderWand()
        ),
    "Gabriel": Enemy(
            name="Gabriel, Apostate of Hate",
            description="a seething red angelic crusader wielding twin swords, desperate to prove himself to the council",
            health=200,
            attack=20,
            move="Sword Throw",
            loot=MarksmanRevolver()
        ),
    "Flowey": Enemy(
            name="Flowey",
            description="a malevolent flower with a cunning and manipulative personality",
            health=350,
            attack=35,
            move="Flamethrower",
            loot=ToyKnife()
        ),
    "TheHeir": Enemy(
            name="The Heir",
            description="a formidable and relentless opponent, putting your combat skills to the test in a challenging battle within its enchanting yet treacherous world.",
            health=400,
            attack=40,
            move="Dark Energy",
            loot=HolyCross()
        ),
    "JenaAnderson": Enemy(
            name="Jena Anderson",
            description="a formidable and challenging adversary, wielding her scientific knowledge and powerful Legion to confront you in an intense battle.",
            health=400,
            attack=40,
            move="Legion",
            loot=XBaton()
        ),
    "TheKraken": Enemy(
            name="The Kraken",
            description="a massive tentacled sea monster that terrorized the ill-fated crew of the ship",
            health=300,
            attack=30,
            move="Tentacles",
            loot=MementoMortem()
        ),
    "Bowser": Enemy(
            name="Bowser",
            description="the king koopa with an imposing stature and fire-breathing abilities",
            health=300,
            attack=30,
            move="Koopa Army",
            loot=Cappy()
        )
    }

def get_enemy(name: str) -> Enemy | None:
    return _enemy.get(name)