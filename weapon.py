import json

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

    def __str__(self) -> str:
        return self.name


# Read data from JSON file
_data = {}
with open("data/weapon.json", "r") as f:
    for record in json.load(f):
        _data[record["name"]] = record


def create(name: str) -> Weapon:
    record = _data[name]
    # The ** operator unpacks a dict as keyword arguments
    return Weapon(**record)
