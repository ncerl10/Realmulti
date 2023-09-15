import json

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


# Read data from JSON file
_data = {}
with open("data/spell.json", "r") as f:
    for record in json.load(f):
        _data[record["name"]] = record


def create(name: str) -> Spell:
    record = _data[name]
    # The ** operator unpacks a dict as keyword arguments
    return Spell(**record)
