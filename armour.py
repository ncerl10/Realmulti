import json

class Armour:
    """The parent class for an armour

    Attributes
    ----------
    - type : str
      Type of the item picked up
    - name : str
      Name of the armour
    - description : str
      Description of the armour
    - effect: str
      Description of the armour's effect
    - defence : int
      Numerical value added to the defence of the the character

    Methods
    -------
    None
    """

    def __init__(self,
                 name: str,
                 description: str,
                 effect: str,
                 *,  # all parameters below this line are keyword arguments
                 defence: int = 0) -> None:
        self.type = "armour"
        self.name = name
        self.description = description
        self.effect = effect
        self.defence = defence


# Read data from JSON file
_data = {}
with open("data/armour.json", "r") as f:
    for record in json.load(f):
        _data[record["name"]] = record


def create(name: str) -> Armour:
    record = _data[name]
    # The ** operator unpacks a dict as keyword arguments
    return Armour(**record)


def NetheriteArmour() -> Armour:
    return Armour(
        name="Netherite Armour",
        description="Netherite Armour is crafted by combining diamond armor with Netherite ingots, it offers increased damage resistance and durability",
        effect="Provides 10 defence",
        defence=10,
    )


def OrnatePlate() -> Armour:
    return Armour(
        name="Ornate Plate",
        description="Ornate Plate is a regal and decorative suit of armor that not only enhances the player's defense but also adds a touch of grandeur to their appearance",
        effect="Provides 15 defence",
        defence=15,
    )

def PowerSuit() -> Armour:
    return Armour(
        name="Power Suit",
        description="The Power Suit provides exceptional protection enabling you to navigate the treacherous alien landscapes and combat formidable foes encountered throughout your missions",
        effect="Provides 30 defence",
        defence=30,
    )

def DragonMail() -> Armour:
    return Armour(
        name="Dragon Mail",
        description="Dragon Mail is a legendary and formidable piece of armor that offers exceptional defense and protection for the wearer. It features dragon-scale motifs, reflecting its durability and resistance to various forms of damage",
        effect="Provides 20 defence",
        defence=20,
    )

def Cappy() -> Armour:
    return Armour(
        name="Cappy",
        description="Cappy is a sentient, shape-shifting hat with the ability to possess objects and enemies",
        effect="Provides 25 defence",
        defence=25,
    )
