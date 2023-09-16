import json

#importing from other files
from enemy import Enemy
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
                 loot=None,
                 *,  # all subsequent parameters are keyword arguments
                 left=None,
                 right=None,
                 front=None,
                 back=None):
        self.name = name
        self.description = description
        self.enemy = enemy
        self.loot = loot
        self.been_here = False
        self.left = left
        self.right = right
        self.front = front
        self.back = back

    def __str__(self) -> str:
        return self.name

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
        self.front = temp

    def link_back(self, room: "Room") -> None:
        """updates the room to the down of the home room(self.name)"""
        temp = room
        temp.front = self
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
    elif room.loot in item._flask:
        loot = item.create(room.loot)
    elif room.loot in item._quest:
        loot = item.create(room.loot)
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
