#importing from other files
from enemy import *
from weapon import *
from armour import *
from spell import *
from item import *


class Room:
    """Encapsulates data for a room.

    Attributes
    ----------
    - name : str
      Name of the room
    - enemy : Enemy
      The enemy that is in the room
    - description : str
      Description of the room
    - left : Room
      The room on the left
    - right : Room
      The room on the right
    - forward : Room
      The room in front
    - back : Room
      The room to the back
    - been_here : bool
      True if the player has entered the room before, False otherwise
    - loot : Item
      The loot that can be found in the room

    Methods
    -------
    None
    """

    def __init__(self,
                 name: str,
                 description: str,
                 enemy: Enemy):
        self.name = name
        self.description = description
        self.enemy = enemy
        self.been_here = False
        self.loot = None
        self.left = None
        self.right = None
        self.forward = None
        self.back = None

    def link_left(self, room: "Room") -> None:
        """updates the room to the left of the home room(self.name)"""
        temp = room
        temp.right = self
        self.left = temp

    def link_right(self, room: "Room") -> None:
        """updates the room to the right of the home room(self.name)"""
        temp = room
        temp.left = self
        self.right = temp

    def link_forward(self, room: "Room") -> None:
        """updates the room to the up of the home room(self.name)"""
        temp = room
        temp.back = self
        self.forward = temp

    def link_back(self, room: "Room") -> None:
        """updates the room to the down of the home room(self.name)"""
        temp = room
        temp.forward = self
        self.back = temp


class Dirtmouth(Room):
    """
    A room that inherits from the Room class
    """

    def __init__(self):
        super().__init__()
        self.set_enemy(TheRadiance())
        self.set_name("Dirtmouth")
        self.set_description(
            "You stepped into Dirtmouth, a haunting cliffside town in the depths of Hallownest, standing as a silent sentinel overlooking a dark and mysterious underground world. Its dilapidated buildings and eerie stillness set the tone for your perilous journey"
        )
        self.link_left(Midgar())
        self.link_right(HyruleKingdom())
        self.link_forward(TheEndDimension())
        self.set_loot(FlaskOfCrimsonTears())


class CelestialResort(Room):
    """
    A room that inherits from the Room class
    """

    def __init__(self):
        super().__init__()
        self.set_enemy(MrOshiro())
        self.set_name("Celestial Resort")
        self.set_description(
            "You stepped into a towering sanctuary of serenity nestled amidst the treacherous slopes of Celeste Mountain, a paradoxical challenge and a refuge for your weary soul. Its elegant halls and perilous puzzles mirrored your personal journey, a delicate dance between inner turmoil and newfound strength."
        )
        self.link_back(Ascent())
        self.set_loot(FlaskOfCeruleanTears())


class TheForge(Room):
    """
    A room that inherits from the Room class
    """

    def __init__(self):
        super().__init__()
        self.set_enemy(TheHighDragun())
        self.set_name("The Forge")
        self.set_description(
            "You stepped into a blistering hellscape deep within the Gungeon, a relentless crucible where you honed your combat skills to a razor's edge. Its molten rivers and infernal denizens pushed you to your limits, but you are determined to conquer it and uncover the ultimate weapon hidden within."
        )
        self.link_forward(Mementos())
        self.set_loot(FlaskOfCrimsonTears())


class StormveilCastle(Room):
    """
    A room that inherits from the Room class
    """

    def __init__(self):
        super().__init__()
        self.set_enemy(GodrickTheGrafted())
        self.set_name("Stormveil Castle")
        self.set_description(
            "You stepped into a legacy dungeon, a castle that lies on the cliff of stormveil, littered with hoards of enemies"
        )
        self.link_forward(Kamurocho())
        self.link_right(TheHallow())
        self.set_loot(FlaskOfCeruleanTears())


class ApertureLab(Room):
    """
    A room that inherits from the Room class
    """

    def __init__(self):
        super().__init__()
        self.set_enemy(Glados())
        self.set_name("Aperture Lab")
        self.set_description(
            "You stepped into a sprawling maze of test chambers filled with menacingly cheery robots and the enigmatic AI, GLaDOS. Your journey through this surreal laboratory is a relentless quest for answers, a desperate struggle to escape its surreal confines and unmask the secrets lurking within."
        )
        self.link_forward(StormveilCastle())
        self.link_back(TowerOfFate())
        self.set_loot(FlaskOfCrimsonTears())


class Zebes(Room):
    """
    A room that inherits from the Room class
    """

    def __init__(self):
        super().__init__()
        self.set_enemy(Ridley())
        self.set_name("Zebes")
        self.set_description(
            "You stepped into a hostile and alien world, where you face some of your most harrowing battles against the Space Pirates and their nefarious plans. Its treacherous landscapes, infested with hostile creatures, hide the secrets of the Chozo and your relentless pursuit of justice."
        )
        self.set_loot(DectusMedallionLeft())


class Bunker(Room):
    """
    A room that inherits from the Room class
    """

    def __init__(self):
        super().__init__()
        self.set_enemy(Emil())
        self.set_name("Bunker")
        self.set_description(
            "You stepped into a grim sanctuary suspended above the ravaged Earth, both a refuge and a reminder of the relentless war against the machines. you receive orders, grapple with the complexities of your existence, and prepare for the constant struggle to reclaim your planet from the alien invaders."
        )
        self.set_loot(FlaskOfCrimsonTears())


class Asphodel(Room):
    """
    A room that inherits from the Room class
    """

    def __init__(self):
        super().__init__()
        self.set_enemy(TheBoneHyrda())
        self.set_name("Asphodel")
        self.set_description(
            "You stepped into a desolate collection of rocky islands amidst a sea of fire beyond Tartarus. You travel between these islands through small bone rafts"
        )
        self.link_back(Commencement())
        self.link_forward(GreenhillZone())
        self.set_loot(FlaskOfCeruleanTears())


class KingdomOfKu(Room):
    """
    A room that inherits from the Room class
    """

    def __init__(self):
        super().__init__()
        self.set_enemy(GeneralMugen())
        self.set_name("Kingdom of Ku")
        self.set_description(
            "You stepped into a nation in Hinoeuma with a long and bloody history of conflict and war. Their enemies numbers many, one among several being the fallen nation of U. It was recently ruled by the aging King Jigo Ku, until a coup removed him from power"
        )
        self.link_right(Bunker())
        self.link_forward(Zebes())
        self.set_loot(FlaskOfCrimsonTears())


class GreenhillZone(Room):
    """
    A room that inherits from the Room class
    """

    def __init__(self):
        super().__init__()
        self.set_enemy(DoctorEggman())
        self.set_name("Greenhill Zone")
        self.set_description(
            "You stepped into a high-speed playground, a vibrant expanse of lush grass and rolling hills, where you feel most at home. Its loop-de-loops and buzzing animal friends provide the perfect backdrop for your never-ending quest to thwart Dr. Robotnik and collect the precious Chaos Emerald"
        )
        self.link_forward(KingdomOfKu())
        self.link_left(TheMushroomKingdom())
        self.set_loot(FlaskOfCeruleanTears())


class TheHallow(Room):
    """
    A room that inherits from the Room class
    """

    def __init__(self):
        super().__init__()
        self.set_enemy(TheMoonLord())
        self.set_name("The Hallow")
        self.set_description(
            "You stepped into a radiant but eerie biome, a stark contrast to the darkness that permeates the underground. It's a realm where fantastical creatures and rare resources await, but also a place where you must tread carefully to avoid its relentless and otherworldly foes."
        )
        self.link_back(TheObraDinn())
        self.set_loot(FlaskOfCrimsonTears())


class Commencement(Room):
    """
    A room that inherits from the Room class
    """

    def __init__(self):
        super().__init__()
        self.set_enemy(Mithrix())
        self.set_name("Commencement")
        self.set_description(
            "You stepped into a large domain located above the shattered breach of Petrichor V's moon. It is ostensibly the desolated seat of Mithrix's power, made up of the shattered remains of four individual sections, emblematic of Mithrix and Providence's tools of creation"
        )
        self.set_loot(FlaskOfCeruleanTears())


class Midgar(Room):
    """
    A room that inherits from the Room class
    """

    def __init__(self):
        super().__init__()
        self.set_enemy(Sephiroth())
        self.set_name("Midgar")
        self.set_description(
            "You stepped into the capital city and power base of the Shinra Electric Power Company in the world of Gaia. your memories of this metropolis are a tangled web of both longing and resentment, forever intertwined with your quest for justice and redemption."
        )
        self.link_forward(TheForge())
        self.set_loot(FlaskOfCrimsonTears())


class HyruleKingdom(Room):
    """
    A room that inherits from the Room class
    """

    def __init__(self):
        super().__init__()
        self.set_enemy(Ganondorf())
        self.set_name("Hyrule Kingdom")
        self.set_description(
            "You stepped into a land steeped in legend and mystique, it is your sacred duty to protect as the Hero of Time. Its vast, rolling landscapes and iconic landmarks are both your home and the canvas upon which your destiny is written as you battle the forces of darkness and seek to rescue Princess Zelda."
        )
        self.link_back(CelestialResort())
        self.set_loot(FlaskOfCeruleanTears())


class TheEndDimension(Room):
    """
    A room that inherits from the Room class
    """

    def __init__(self):
        super().__init__()
        self.set_enemy(TheEnderDragon())
        self.set_name("The End Dimension")
        self.set_description(
            "You stepped into a dark, space-like dimension consisting of separate islands in the void, made out of end stone. It is inhabited by endermen and shulkers."
        )
        self.link_forward(TheShriekingShack())
        self.set_loot(FlaskOfCrimsonTears())


class Kamurocho(Room):
    """
    A room that inherits from the Room class
    """

    def __init__(self):
        super().__init__()
        self.set_enemy(Shibusawa())
        self.set_name("Kamurocho")
        self.set_description(
            "You stepped into the nightlife capital of Japan. As Tojo Clan territory, the district is home to many yakuza and is often the setting of large and small-scale disputes between the Tojo Clan and their rivals such as the Omi Alliance, as well as intra-clan conflicts between Tojo subsidiaries"
        )
        self.link_forward(Snowdin())
        self.set_loot(FlaskOfCeruleanTears())


class TowerOfFate(Room):
    """
    A room that inherits from the Room class
    """

    def __init__(self):
        super().__init__()
        self.set_enemy(Enchantress())
        self.set_name("Tower of Fate")
        self.set_description(
            "You stepped in a looming bastion of darkness and danger, standing as the heart of your perilous journey to save your beloved Shield Knight and the realm from the Enchantress's curse. Its treacherous ascent tests your mettle and resolve, driving you to prove that you am truly a knight worthy of legend."
        )
        self.set_loot(FlaskOfCrimsonTears())


class ShoresOfNine(Room):
    """
    A room that inherits from the Room class
    """

    def __init__(self):
        super().__init__()
        self.set_enemy(Freya())
        self.set_name("Shores of Nine")
        self.set_description(
            "You stepped into a realm of Norse myth, it offers a temporary respite from the relentless chaos of your past. You navigate this strange land with your son, Atreus, in search of a new beginning, forging a path toward redemption while battling the threats lurking in these uncharted waters."
        )
        self.set_loot(FlaskOfCeruleanTears())


class Mementos(Room):
    """
    A room that inherits from the Room class
    """

    def __init__(self):
        super().__init__()
        self.set_enemy(Yaldabaoth())
        self.set_name("Mementos")
        self.set_description(
            "You stepped into a sprawling, ever-changing abyss beneath the city, is where you confront the twisted desires of society's heart. It's a labyrinthine reflection of the collective unconscious, where you as a Phantom Thief embark on a mission to change hearts and expose the hidden darkness that plagues Tokyo."
        )
        self.link_right(ShoresOfNine())
        self.link_left(Asphodel())
        self.set_loot(FlaskOfCrimsonTears())


class Ascent(Room):
    """
    A room that inherits from the Room class
    """

    def __init__(self):
        super().__init__()
        self.set_enemy(Reyna())
        self.set_name("Ascent")
        self.set_description(
            "You step into a clearing, in the middle of what seems to be a city. Surrounding you are buildings, their appearance reminding you of Ancient Roman Architecture. A skyscraper rises into the sky in the distance, its cold, geometric features clashing with the elegant, smooth lines of the buildings surrounding you. It is only when you turn around that you realise the entire city is several hundred metres above the ground."
        )
        self.link_right(ApertureLab())
        self.link_left(SixthCircleOfHell())
        self.set_loot(FlaskOfCeruleanTears())


class TheShriekingShack(Room):
    """
    A room that inherits from the Room class
    """

    def __init__(self):
        super().__init__()
        self.set_enemy(Voldemort())
        self.set_name("The Shrieking Shack")
        self.set_description(
            "You step into a notorious and allegedly haunted building near Hogwarts School, known for its eerie and unsettling reputation as the most haunted building in Britain"
        )
        self.set_loot(FlaskOfCrimsonTears())


class SixthCircleOfHell(Room):
    """
    A room that inherits from the Room class
    """

    def __init__(self):
        super().__init__()
        self.set_enemy(Gabriel())
        self.set_name("6th Circle of Hell")
        self.set_description(
            "You step into an abandoned church bathed in blood red light. The walls are patterned with the faces of the damned, their expressions contorted in agony, doomed to shriek silently for all eternity. On the far side of the room, a church organ looms over you, an eerie, melancholic melody flowing from its pipes. Its player, a lone figure clad in gold and silver armour"
        )
        self.set_loot(FlaskOfCeruleanTears())


class Snowdin(Room):
    """
    A room that inherits from the Room class
    """

    def __init__(self):
        super().__init__()
        self.set_enemy(Flowey())
        self.set_name("Snowdin")
        self.set_description(
            "You step into a quaint and snowy town nestled in the underground, itexudes a cozy charm with its warm, dimly lit shops and friendly monster residents. The gentle fall of snowflakes and the sound of crackling fires create a serene atmosphere that contrasts the rest of your journey"
        )
        self.link_left(TheAstralPlane())
        self.link_right(TheSealedTemple())
        self.set_loot(FlaskOfCrimsonTears())


class TheSealedTemple(Room):
    """
    A room that inherits from the Room class
    """

    def __init__(self):
        super().__init__()
        self.set_enemy(TheHeir())
        self.set_name("The Sealed Temple")
        self.set_description(
            "You step into a mysterious, ancient structure shrouded in secrecy, holding untold treasures and enigmatic relics waiting to be uncovered by the brave adventurer. Its imposing architecture and mystic aura make it a central point of intrigue and discovery"
        )
        self.set_loot(DectusMedallionRight())


class TheAstralPlane(Room):
    """
    A room that inherits from the Room class
    """

    def __init__(self):
        super().__init__()
        self.set_enemy(JenaAnderson())
        self.set_name("The Astral Plane")
        self.set_description(
            "You step into surreal and nightmarish realm that exists parallel to the human world, inhabited by grotesque and otherworldly creatures known as Chimeras"
        )
        self.set_loot(FlaskOfCrimsonTears())


class TheObraDinn(Room):
    """
    A room that inherits from the Room class
    """

    def __init__(self):
        super().__init__()
        self.set_enemy(TheKraken())
        self.set_name("The Obra Dinn")
        self.set_description(
            "You step onto a merchant vessel that mysteriously reappeared in 1807 after being lost at sea for five years, with all of its crew either dead or missing"
        )
        self.set_loot(FlaskOfCeruleanTears())


class TheMushroomKingdom(Room):
    """
    A room that inherits from the Room class
    """

    def __init__(self):
        super().__init__()
        self.set_enemy(Bowser())
        self.set_name("The Mushroom Kingdom")
        self.set_description(
            "You step into a colorful and enchanting land filled with lush forests, towering mountains, and cheerful inhabitants like Toads and Yoshis"
        )
        self.set_loot(FlaskOfCrimsonTears())
