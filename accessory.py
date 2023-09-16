import json

class Accessory:
    """The parent class for an accessory

    Attributes
    ----------
    - type : str
      Type of the item picked up
    - name : str
      Name of the accessory
    - description : str
      Description of the accessory
    - health_boost : int
      Numerical value added to the health of the the character
    - attack_boost : int
      Numerical value added to the attack of the the character
    - mana_boost : int
      Numerical value added to the mana of the the character
    - defence_boost : int
      Numerical value added to the defence of the the character
    - effect: str
      The effect that the item has
      
    Methods
    -------
    - effect() -> str
      Describes the effect of the item
        """

    def __init__(self,
                 name: str,
                 description: str,
                 effect: str,
                 *,  # all parameters below this line are keyword arguments
                 health_boost: int = 0,
                 attack_boost: int = 0,
                 mana_boost: int = 0,
                 defence_boost: int = 0) -> None:
        self.type = "accessory"
        self.name = name
        self.description = description
        self.effect = effect
        self.health_boost = health_boost
        self.attack_boost = attack_boost
        self.mana_boost = mana_boost
        self.defence_boost = defence_boost

    def __str__(self) -> str:
        return self.name


# Read data from JSON file
_data = {}
with open("data/accessory.json", "r") as f:
    for record in json.load(f):
        _data[record["name"]] = record


def create(name: str) -> Accessory:
    record = _data[name]
    # The ** operator unpacks a dict as keyword arguments
    return Accessory(**record)
