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
