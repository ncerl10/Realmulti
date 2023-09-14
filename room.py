import json

#importing from other files
from enemy import Enemy, get_enemy
from weapon import *
from armour import *
from spell import *
import enemy
import item
import armour
import weapon
import spell


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
                 enemy,
                 loot):
        self.name = name
        self.description = description
        self.enemy = enemy
        self.loot = loot
        self.been_here = False
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


_data = {}
_rooms = {}


def create(name: str) -> Room:
    record = _data[name]
    # The ** operator unpacks a dict as keyword arguments
    room = Room(**record)
    if room.loot in armour._data:
        loot = armour.create(room.loot)
    elif room.loot in weapon._data:
        loot = weapon.create(room.loot)
    elif room.loot in spell._data:
        loot = spell.create(room.loot)
    room.loot = loot
    room.enemy = enemy.create(room.enemy)
    return room

def get(name: str) -> Room:
    return _rooms[name]


with open("data/room.json", "r") as f:
    for record in json.load(f):
        _data[record["name"]] = record
# Instantiate rooms
for name in _data:
    _rooms[name] = create(name)
# Link rooms to instantiated rooms
for room in _rooms.values():
    if room.left:
        room.left = get(room.left)
    if room.right:
        room.right = get(room.right)
    if room.front:
        room.front = get(room.front)
    if room.back:
        room.back = get(room.back)


class Dirtmouth(Room):
    """
    A room that inherits from the Room class
    """

    def __init__(self):
        super().__init__(
            name="Dirtmouth",
            description="You stepped into Dirtmouth, a haunting cliffside town in the depths of Hallownest, standing as a silent sentinel overlooking a dark and mysterious underground world. Its dilapidated buildings and eerie stillness set the tone for your perilous journey",
            enemy=get_enemy("TheRadiance"),
            loot=item.health_flask(1)
        )
        self.link_left(Midgar())
        self.link_right(HyruleKingdom())
        self.link_forward(TheEndDimension())


class CelestialResort(Room):
    """
    A room that inherits from the Room class
    """

    def __init__(self):
        super().__init__(
            name="Celestial Resort",
            description="You stepped into a towering sanctuary of serenity nestled amidst the treacherous slopes of Celeste Mountain, a paradoxical challenge and a refuge for your weary soul. Its elegant halls and perilous puzzles mirrored your personal journey, a delicate dance between inner turmoil and newfound strength.",
            enemy=get_enemy("MrOshiro"),
            loot=item.mana_flask(1),
        )
        self.link_back(Ascent())


class TheForge(Room):
    """
    A room that inherits from the Room class
    """

    def __init__(self):
        super().__init__(
            name="The Forge",
            description=(
                "You stepped into a blistering hellscape deep within the Gungeon, "
                "a relentless crucible where you honed your combat skills to a razor's edge. "
                "Its molten rivers and infernal denizens pushed you to your limits, but you are determined "
                "to conquer it and uncover the ultimate weapon hidden within."
            ),
            enemy=get_enemy("TheHighDragun"),
            loot=item.health_flask(1)
        )
        self.link_forward(Mementos())


class StormveilCastle(Room):
    """
    A room that inherits from the Room class
    """

    def __init__(self):
        super().__init__(
            name="Stormveil Castle",
            description=(
                "You stepped into a legacy dungeon, a castle that lies on the cliff of stormveil, "
                "littered with hoards of enemies."
            ),
            enemy=get_enemy("GodrickTheGrafted"),
            loot=item.mana_flask(1)
        )
        self.link_forward(Kamurocho())
        self.link_right(TheHallow())


class ApertureLab(Room):
    """
    A room that inherits from the Room class
    """

    def __init__(self):
        super().__init__(
            name="Aperture Lab",
            description=(
                "You stepped into a sprawling maze of test chambers filled with menacingly cheery robots "
                "and the enigmatic AI, GLaDOS. Your journey through this surreal laboratory is a relentless quest "
                "for answers, a desperate struggle to escape its surreal confines and unmask the secrets lurking within."
            ),
            enemy=get_enemy("Glados"),
            loot=item.health_flask(1)
        )
        self.link_forward(StormveilCastle())
        self.link_back(TowerOfFate())


class Zebes(Room):
    """
    A room that inherits from the Room class
    """

    def __init__(self):
        super().__init__(
            name="Zebes",
            description=(
                "You stepped into a hostile and alien world, where you face some of your most harrowing battles against "
                "the Space Pirates and their nefarious plans. Its treacherous landscapes, infested with hostile creatures, "
                "hide the secrets of the Chozo and your relentless pursuit of justice."
            ),
            enemy=get_enemy("Ridley"),
            loot=item.get_quest_item("DectusMedallionLeft")
        )


class Bunker(Room):
    """
    A room that inherits from the Room class
    """

    def __init__(self):
        super().__init__(
            name="Bunker",
            description=(
                "You stepped into a grim sanctuary suspended above the ravaged Earth, "
                "both a refuge and a reminder of the relentless war against the machines. "
                "You receive orders, grapple with the complexities of your existence, "
                "and prepare for the constant struggle to reclaim your planet from the alien invaders."
            ),
            enemy=get_enemy("Emil"),
            loot=item.health_flask(1)
        )


class Asphodel(Room):
    """
    A room that inherits from the Room class
    """

    def __init__(self):
        super().__init__(
            name="Asphodel",
            description=(
                "You stepped into a desolate collection of rocky islands amidst a sea of fire beyond Tartarus. "
                "You travel between these islands through small bone rafts."
            ),
            enemy=get_enemy("TheBoneHyrda"),
            loot=item.mana_flask(1)
        )
        self.link_back(Commencement())
        self.link_forward(GreenhillZone())


class KingdomOfKu(Room):
    """
    A room that inherits from the Room class
    """

    def __init__(self):
        super().__init__(
            name="Kingdom of Ku",
            description=(
                "You stepped into a nation in Hinoeuma with a long and bloody history of conflict and war. "
                "Their enemies numbers many, one among several being the fallen nation of U. It was recently ruled "
                "by the aging King Jigo Ku, until a coup removed him from power."
            ),
            enemy=get_enemy("GeneralMugen"),
            loot=item.health_flask(1)
        )
        self.link_right(Bunker())
        self.link_forward(Zebes())


class GreenhillZone(Room):
    """
    A room that inherits from the Room class
    """

    def __init__(self):
        super().__init__(
            name="Greenhill Zone",
            description=(
                "You stepped into a high-speed playground, a vibrant expanse of lush grass and rolling hills, "
                "where you feel most at home. Its loop-de-loops and buzzing animal friends provide the perfect backdrop "
                "for your never-ending quest to thwart Dr. Robotnik and collect the precious Chaos Emerald."
            ),
            enemy=get_enemy("DoctorEggman"),
            loot=item.mana_flask(1)
        )
        self.link_forward(KingdomOfKu())
        self.link_left(TheMushroomKingdom())


class TheHallow(Room):
    """
    A room that inherits from the Room class
    """

    def __init__(self):
        super().__init__(
            name="The Hallow",
            description=(
                "You stepped into a radiant but eerie biome, a stark contrast to the darkness that permeates the underground. "
                "It's a realm where fantastical creatures and rare resources await, but also a place where you must tread carefully "
                "to avoid its relentless and otherworldly foes."
            ),
            enemy=get_enemy("TheMoonLord"),
            loot=item.health_flask(1)
        )
        self.link_back(TheObraDinn())


class Commencement(Room):
    """
    A room that inherits from the Room class
    """

    def __init__(self):
        super().__init__(
            name="Commencement",
            description=(
                "You stepped into a large domain located above the shattered breach of Petrichor V's moon. "
                "It is ostensibly the desolated seat of Mithrix's power, made up of the shattered remains of four individual "
                "sections, emblematic of Mithrix and Providence's tools of creation."
            ),
            enemy=get_enemy("Mithrix"),
            loot=item.mana_flask(1)
        )


class Midgar(Room):
    """
    A room that inherits from the Room class
    """

    def __init__(self):
        super().__init__(
            name="Midgar",
            description=(
                "You stepped into the capital city and power base of the Shinra Electric Power Company in the world of Gaia. "
                "Your memories of this metropolis are a tangled web of both longing and resentment, forever intertwined with your "
                "quest for justice and redemption."
            ),
            enemy=get_enemy("Sephiroth"),
            loot=item.health_flask(1)
        )
        self.link_forward(TheForge())


class HyruleKingdom(Room):
    """
    A room that inherits from the Room class
    """

    def __init__(self):
        super().__init__(
            name="Hyrule Kingdom",
            description=(
                "You stepped into a land steeped in legend and mystique, it is your sacred duty to protect as the Hero of Time. "
                "Its vast, rolling landscapes and iconic landmarks are both your home and the canvas upon which your destiny is written "
                "as you battle the forces of darkness and seek to rescue Princess Zelda."
            ),
            enemy=get_enemy("Ganondorf"),
            loot=item.mana_flask(1)
        )
        self.link_back(CelestialResort())


class TheEndDimension(Room):
    """
    A room that inherits from the Room class
    """

    def __init__(self):
        super().__init__(
            name="The End Dimension",
            description=(
                "You stepped into a dark, space-like dimension consisting of separate islands in the void, made out of end stone. "
                "It is inhabited by endermen and shulkers."
            ),
            enemy=get_enemy("TheEnderDragon"),
            loot=item.health_flask(1)
        )
        self.link_forward(TheShriekingShack())


class Kamurocho(Room):
    """
    A room that inherits from the Room class
    """

    def __init__(self):
        super().__init__(
            name="Kamurocho",
            description=(
                "You stepped into the nightlife capital of Japan. As Tojo Clan territory, the district is home to many yakuza and is "
                "often the setting of large and small-scale disputes between the Tojo Clan and their rivals such as the Omi Alliance, "
                "as well as intra-clan conflicts between Tojo subsidiaries."
            ),
            enemy=get_enemy("Shibusawa"),
            loot=item.mana_flask(1)
        )
        self.link_forward(Snowdin())


class TowerOfFate(Room):
    """
    A room that inherits from the Room class
    """

    def __init__(self):
        super().__init__(
            name="Tower of Fate",
            description=(
                "You stepped in a looming bastion of darkness and danger, standing as the heart of your perilous journey to save your "
                "beloved Shield Knight and the realm from the Enchantress's curse. Its treacherous ascent tests your mettle and resolve, "
                "driving you to prove that you am truly a knight worthy of legend."
            ),
            enemy=get_enemy("Enchantress"),
            loot=item.health_flask(1)
        )


class ShoresOfNine(Room):
    """
    A room that inherits from the Room class
    """

    def __init__(self):
        super().__init__(
            name="Shores of Nine",
            description=(
                "You stepped into a realm of Norse myth, it offers a temporary respite from the relentless chaos of your past. "
                "You navigate this strange land with your son, Atreus, in search of a new beginning, forging a path toward redemption "
                "while battling the threats lurking in these uncharted waters."
            ),
            enemy=get_enemy("Freya"),
            loot=item.mana_flask(1)
        )


class Mementos(Room):
    """
    A room that inherits from the Room class
    """

    def __init__(self):
        super().__init__(
            name="Mementos",
            description=(
                "You stepped into a sprawling, ever-changing abyss beneath the city, is where you confront the twisted desires of "
                "society's heart. It's a labyrinthine reflection of the collective unconscious, where you as a Phantom Thief embark on "
                "a mission to change hearts and expose the hidden darkness that plagues Tokyo."
            ),
            enemy=get_enemy("Yaldabaoth"),
            loot=item.health_flask(1)
        )
        self.link_right(ShoresOfNine())
        self.link_left(Asphodel())


class Ascent(Room):
    """
    A room that inherits from the Room class
    """

    def __init__(self):
        super().__init__(
            name="Ascent",
            description=(
                "You step into a clearing, in the middle of what seems to be a city. Surrounding you are buildings, "
                "their appearance reminding you of Ancient Roman Architecture. A skyscraper rises into the sky in the distance, "
                "its cold, geometric features clashing with the elegant, smooth lines of the buildings surrounding you. "
                "It is only when you turn around that you realise the entire city is several hundred metres above the ground."
            ),
            enemy=get_enemy("Reyna"),
            loot=item.mana_flask(1)
        )
        self.link_right(ApertureLab())
        self.link_left(SixthCircleOfHell())


class TheShriekingShack(Room):
    """
    A room that inherits from the Room class
    """

    def __init__(self):
        super().__init__(
            name="The Shrieking Shack",
            description=(
                "You step into a notorious and allegedly haunted building near Hogwarts School, known for its eerie and unsettling "
                "reputation as the most haunted building in Britain."
            ),
            enemy=get_enemy("Voldemort"),
            loot=item.health_flask(1)
        )


class SixthCircleOfHell(Room):
    """
    A room that inherits from the Room class
    """

    def __init__(self):
        super().__init__(
            name="6th Circle of Hell",
            description=(
                "You step into an abandoned church bathed in blood red light. The walls are patterned with the faces of the damned, "
                "their expressions contorted in agony, doomed to shriek silently for all eternity. On the far side of the room, a church "
                "organ looms over you, an eerie, melancholic melody flowing from its pipes. Its player, a lone figure clad in gold and silver armour."
            ),
            enemy=get_enemy("Gabriel"),
            loot=item.mana_flask(1)
        )


class Snowdin(Room):
    """
    A room that inherits from the Room class
    """

    def __init__(self):
        super().__init__(
            name="Snowdin",
            description=(
                "You step into a quaint and snowy town nestled in the underground, it exudes a cozy charm with its warm, dimly lit shops "
                "and friendly monster residents. The gentle fall of snowflakes and the sound of crackling fires create a serene atmosphere "
                "that contrasts the rest of your journey."
            ),
            enemy=get_enemy("Flowey"),
            loot=item.health_flask(1)
        )
        self.link_left(TheAstralPlane())
        self.link_right(TheSealedTemple())


class TheSealedTemple(Room):
    """
    A room that inherits from the Room class
    """

    def __init__(self):
        super().__init__(
            name="The Sealed Temple",
            description=(
                "You step into a mysterious, ancient structure shrouded in secrecy, holding untold treasures and enigmatic relics "
                "waiting to be uncovered by the brave adventurer. Its imposing architecture and mystic aura make it a central point "
                "of intrigue and discovery."
            ),
            enemy=get_enemy("TheHeir"),
            loot=item.get_quest_item("DectusMedallionRight")
        )


class TheAstralPlane(Room):
    """
    A room that inherits from the Room class
    """

    def __init__(self):
        super().__init__(
            name="The Astral Plane",
            description=(
                "You step into surreal and nightmarish realm that exists parallel to the human world, inhabited by grotesque and "
                "otherworldly creatures known as Chimeras."
            ),
            enemy=get_enemy("JenaAnderson"),
            loot=item.health_flask(1)
        )


class TheObraDinn(Room):
    """
    A room that inherits from the Room class
    """

    def __init__(self):
        super().__init__(
            name="The Obra Dinn",
            description=(
                "You step onto a merchant vessel that mysteriously reappeared in 1807 after being lost at sea for five years, with "
                "all of its crew either dead or missing."
            ),
            enemy=get_enemy("TheKraken"),
            loot=item.mana_flask(1)
        )


class TheMushroomKingdom(Room):
    """
    A room that inherits from the Room class
    """

    def __init__(self):
        super().__init__(
            name="The Mushroom Kingdom",
            description=(
                "You step into a colorful and enchanting land filled with lush forests, towering mountains, and cheerful inhabitants "
                "like Toads and Yoshis."
            ),
            enemy=get_enemy("Bowser"),
            loot=item.health_flask(1)
        )
