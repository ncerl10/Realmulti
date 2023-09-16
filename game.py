#import from python built in libraries
import time
import random

#import from other files
from character import Character
from data import text
from enemy import Enemy
from room import Room
from setup import *


PAUSE_TIME = 1


def pause(n: int=1) -> None:
    time.sleep(n * PAUSE_TIME)


def show_text(text: str, *, break_before: bool=True, break_after: bool=True) -> None:
    if break_before:
        print()
    print(text)
    if break_after:
        print()
    pause()


def dice_roll(n: int, m: int) -> bool:
    """Roll a die with n sides, of which m are considered successful"""
    assert n > 1, f"Dice cannot have {n} sides"
    assert m > 0, f"Success chance cannot be {m}/{n}"
    assert n >= m, f"Success chance cannot be {m}/{n}"
    return 0 <= random.randint(0, n) < m


def get_valid_choice(choices: list, prompt: str, error_callback) -> str:
    """Helper function to prompt the player with a list of choices, validate the
    player's choice, and return it.
    
    1. Display choices to the player
    2. Prompt the player for a choice
    3. Validate the player's choice (is in the list of choices)
    4. Display an error message if invalid

    The error message is displayed with a callback function that takes in the choice as
    a str and returns the error message as a str.
    """
    choices_lower = [choice.lower() for choice in choices]
    for choice in choices:
        print(f"- {choice}")
    choice = None
    while not choice:
        choice = input(prompt).lower()
        if choice not in choices_lower:
            print(error_callback(choice))
            choice = None
        pause()
    return choice


class Game:
    """
    A class that creates an instance of the game

    Attributes
    ----------
    - end : bool
      True when game ends, False otherwise
    - room : Room
      Class for the room the player is in
    - character : Character
      Class of the character
    - actions : list[str]
      List of possible actions
    - description : list[str]
      List of description of possible actions

    Methods
    -------
    + intro(self) -> None
    + run(self) -> None
    - help(self) -> None
    - look(self, room : Room) -> None
    - move(self, room : Room) -> None
    - loot(self, user : Character, loot : item.Item) -> None
    - flask(self, user : Character) -> None
    - attack(self, attacker : Character , victim: Enemy) -> None
    - get_choice(self, user : Character) -> str
    - get_attack(self, user : Character, decision : str) -> [int, Weapon]
    - use_flask(self, user : Character) -> None
    - equip(self, user) -> None
    - display_equipment(self, user : Character) -> None
    - equip_armour(self, user : Character) -> None
    - equip_weapon(self, user : Character) -> None
    - equip_accessory(self, user : Character) -> None
    - status(self, user : Character) -> None
    - info(self, user : Character) -> None
    - weapon_info(self, user : Character) -> None
    - spell_info(self, user : Character) -> None
    - armour_info(self, user : Character) -> None
    - accessory_info(self, user : Character) -> None
    - flask_info(self) -> None
    - item_info(self, user : Character) -> None
    - display_room_name(self) -> None
    - display_room_description(self) -> None
    - get_action(self) -> str
    - collect_loot(self, attacker : Character, loot : item.Item) -> None
    - end_game(self) -> None
    - win(self, weapon) -> None
    - die(self) -> None
    - meow(self) -> None
    - secret(self) -> None
    """

    def __init__(self) -> None:
        temp = setup()
        self.end = False
        self.room = temp[0]
        self.character = temp[1]
        self.actions = [
            "help", "look", "move", "loot", "flask", "attack", "equip",
            "status", "info", "die", "meow"
        ]
        self.description = [
            "Gets the list of possible actions", "Looks around the room",
            "Move to another room", "Search the room for loot",
            "Drink your flasks", "Attack the enemny", "Change your equipment",
            "See your statistics", "Find out more about your items",
            "Ends the game", "meow"
        ]

    def intro(self) -> None:
        """print introduction for the start of the game """

        # Displays the introduction messages
        for line in text.WELCOME:
            show_text(line)

        decision = input('Do you wish to enter the school? ( yes / no ): ').lower()

        if decision == "yes":
            print()
            name = input('Tarnished, key in your name: ')
            self.character.name = name
            # Check if the user used the secret easter egg name
            if name == "meow":
                self.secret()
            else:
                show_text(text.WELCOME_YES)
        elif decision == "no":
            show_text(text.WELCOME_NO)
            self.end = True
            self.end_game()
            return
        else:
            show_text(text.WELCOME_OTHER)
            self.end = True
            self.end_game()
            return

    def run(self) -> None:
        """to be run in a loop to prompt user's action"""
        self.display_room_name()
        # Checks if the player has entered the room before
        if not self.room.been_here:
            self.display_room_description()

        decision = self.get_action()
        # Does the action the user selected
        if decision == "help":
            self.help()
        elif decision == "look":
            self.look(self.room)
        elif decision == "move":
            self.move(self.room)
        elif decision == "attack":
            self.attack(self.character, self.room.enemy)
        elif decision == "loot":
            self.loot(self.character, self.room.loot)
        elif decision == "flask":
            self.flask(self.character)
        elif decision == "equip":
            self.equip(self.character)
        elif decision == "status":
            self.status(self.character)
        elif decision == "info":
            self.info(self.character)
        elif decision == "die":
            self.die()
        elif decision == "meow":
            self.meow()

    def help(self) -> None:
        """main action for user to get the list of possible actions"""
        # Displays the list of actions the user can do
        print("\nYou are able to:")
        for i, action in enumerate(self.actions):
            print(f"- {action} ({self.description[i]})")
        pause()

    def look(self, room: Room) -> None:
        """main action to look around the room including rooms linked to the room and enemies in the room"""
        # Displays the connected rooms
        if room.left:
            print(f"To the left is {room.left}")
        if room.right:
            print(f"To the right is {room.right}")
        if room.front:
            print(f"In front of you is {room.front}")
        if room.back:
            print(f"Behind you is {room.back}")
        pause()

        # Displays the enemy in the room
        if room.enemy:
            show_text(
                f"In the middle of the room is {room.enemy}, {room.enemy.description}"
            )

    def move(self, room: Room) -> None:
        """main action for user to traverse from one room to another"""
        choice = get_valid_choice(
            ["left", "right", "forward", "back"],
            prompt="Which direction do you wish to move in?",
            error_callback=text.move_fail,
        )

        # Generate a random number to see if you managed to sneak past the enemy
        caught = False if not room.enemy else dice_roll(3, 1)

        if not caught:
            show_text(text.sneak_success(room.enemy.name))
            if choice == "left":
                if room.left is None:
                    show_text(text.hit_wall(choice))
                else:
                    self.room = room.left
            if choice == "right":
                if room.right is None:
                    show_text(text.hit_wall(choice))
                else:
                    self.room = room.right
            if choice == "forward":
                if room.front is None:
                    show_text(text.hit_wall(choice))
                # Check if you are going to the final boss room
                elif room.front.name == "The Shrieking Shack":
                    # Checks if you have the required items to enter the final boss room
                    if "Dectus Medallion (right)" in self.character.items and "Dectus Medallion (left)" in self.character.items:
                        show_text(text.BREAK_SPELL)
                        self.room = room.front
                    else:
                        show_text(text.DOOR_LOCKED)
                        show_text(text.DOOR_LOCKED_HINT)
                else:
                    self.room = room.front

            if choice == "back":
                if room.back is None:
                    show_text(text.hit_wall(choice))
                else:
                    self.room = room.back

        else:
            show_text(text.sneak_fail(room.enemy.name))
            self.attack(self.character, room.enemy)

    def loot(self, user: Character, loot: item.Item) -> None:
        """main action for user to search the room for loot"""

        # Generate a random number to see if you successfully loot the room whithout the enemy noticing
        caught = False if not self.room.enemy else dice_roll(3, 2)
        if not caught:
            show_text(text. loot_success(self.room.enemy))
            # Allow the user to loot the room
            if loot is None:
                show_text(text.loot_none(loot))
            elif isinstance(loot, item.Flask):
                show_text(text.obtain_thing(loot, loot.type))
                if isinstance(loot, item.HealthFlask):
                    user.take_health_flask(1)
                elif isinstance(loot, item.ManaFlask):
                    user.take_mana_flask(1)
                self.room.loot = None
            elif isinstance(loot, item.QuestItem):
                show_text(text.obtain_thing(loot, loot.type))
                user.take_item(loot)
                self.room.loot = None

        else:
            show_text(text. loot_fail(self.room.enemy))
            self.attack(user, self.room.enemy)

    def flask(self, user: Character) -> None:
        """main action for user to drink their flasks"""
        # Check if the user still has available flasks
        if (user.health_flask.count + user.mana_flask.count == 0):
            show_text(text.out_of_item("flasks"))
        else:
            self.use_flask(user)

    def attack(self, attacker: Character, victim: Enemy) -> None:
        """main action for user to attack the enemy in the room"""
        # Check if there is an enemy in the room
        if victim is None:
            show_text(text.attack_none(victim))
        else:
            while not attacker.is_dead():
                # Display users health and mana
                print(f"\n{'-'*50}\n")
                print(f"{attacker} has {attacker.health} health")
                print(f"{attacker} has {attacker.mana} mana")
                print(
                    f"{attacker} has {attacker.health_flask.count} {attacker.health_flask}"
                )
                print(
                    f"{attacker} has {attacker.mana_flask.count} {attacker.mana_flask}"
                )
                pause()
                # Display enemy's health
                show_text(f"{victim} has {victim.health} health")

                decision = self.get_choice(attacker)
                if decision == "flask":
                    self.use_flask(attacker, cancel=False)
                    if not victim.is_dead():
                        damage = attacker.take_damage(victim.attack - attacker.get_defence())
                        show_text(
                            f"{victim} used {victim.move}, dealing {damage} damage to {attacker}"
                        )
                else:
                    damage, weapon = self.get_attack(attacker, decision)

                    victim.take_damage(damage + attacker.get_attack())
                    if not victim.is_dead():
                        show_text(
                            f"{attacker}{weapon.move}, dealing {damage} damage to {victim}"
                        )
                    # Allow enemy to attack if it didn't die yet
                    if not victim.is_dead():
                        damage = attacker.take_damage(victim.attack - attacker.get_defence())
                        show_text(
                            f"{victim} used {victim.move}, dealing {damage} damage to {attacker}"
                        )
                    else:
                        # Check if dead enemy is the final boss
                        if victim.name == "Voldemort":
                            self.win(weapon)
                            return
                        show_text(
                            f"{attacker}{weapon.win_front}{victim}{weapon.win_back}"
                        )
                        show_text(f"{victim} dropped a {victim.loot}")
                        choice = input(
                            f"\nDo you want to pick {victim.loot}? ( yes / no ): "
                        ).lower()
                        if choice == "yes":
                            self.collect_loot(attacker, victim.loot)
                            show_text(victim.loot.description)
                        elif choice == "no":
                            show_text(text.loot_no(victim.loot))
                        else:
                            show_text(text.loot_other(victim.loot))
                        # Removes the enemy from the room
                        self.room.enemy = None
                        break
            # Check if the user died
            if attacker.is_dead():
                self.end_game()

    def get_choice(self, user: Character) -> str:
        """sub action from attack() to prompt user for attack methods or use of flask"""
        choices = [str(user.weapon), "Spell", "Flask"]
        while True:
            choice = get_valid_choice(
                choices,
                prompt="What do you want to use?",
                error_callback=text.use_fail
            )
            if choice == "spell" and user.mana < min(user.spells, key=lambda s: s.cost, default=0).cost:
                show_text(text.OUT_OF_MANA)
            # Check if user has any flask to drink
            elif choice == "flask" and (user.health_flask.count + user.mana_flask.count == 0):
                show_text(text.OUT_OF_FLASKS)
            else:
                break
        return choice

    def get_attack(self, user: Character, decision: str) -> tuple[int, Spell]:
        """sub action from attack() to get total damage done to victim"""

        # Check if user used his weapon
        if decision.lower() == str(user.weapon).lower():
            return user.weapon.attack, user.weapon

        # check if user used spells
        elif decision.lower() == "spell":
            print("\nSpells:")
            time.sleep(1)
            choice = get_valid_choice(
                list(user.spells.keys()),
                prompt="Which spell would you like to cast",
                error_callback=text.spell_fail
            )
            cost = user.spells[choice].cost
            show_text(f"You used up {cost} mana points")
            user.use_mana(cost)
            return user.spells[choice].attack, user.spells[choice]

    def use_flask(self, user: Character, cancel: bool=True) -> None:
        """Function to allow the user to use flask, with option to cancel the action"""
        user.display_flask()
        choices = [
            str(user.health_flask),
            str(user.mana_flask),
        ]
        if cancel:
            choices.append("cancel")
        while True:
            choice = get_valid_choice(
                choices,
                prompt="Which flask would you like to drink?",
                error_callback=text.flask_fail
            )
            if choice == "cancel":
                return
            # Checks if the user has enough flask of crimson tears
            if choice == str(user.health_flask).lower() and user.health_flask.count == 0:
                show_text(text.out_of_item(user.health_flask))
            # Checks if the user has enough flask of cerulean tears
            elif choice == str(user.mana_flask).lower() and user.mana_flask.count == 0:
                show_text(text.out_of_item(user.mana_flask))

        if choice == str(user.health_flask).lower():
            # Makes sure the health healed does not exceed the maximum health
            healing = user.add_health(user.health_flask.health)
            show_text(text.flask_success(user.health_flask, f"{healing} health"))
            user.consume_health_flask(1)

        elif choice == str(user.mana_flask).lower():
            # Makes sure the mana gained does not exceed the maximum mana
            healing = user.add_mana(user.mana_flask.mana)
            show_text(text.flask_success(user.mana_flask, f"{healing} mana"))
            user.consume_mana_flask(1)

    def equip(self, user: Character) -> None:
        """main action for user to equip various items"""

        self.display_equipment(user)
        choice = get_valid_choice(
            ["yes", "no"],
            prompt="do you want to change your equipment?",
            error_callback=lambda _: "Please answer yes or no",
        )
        if choice == "no":
            return
        choices = ["armour", "weapon", "accessory", "finish"]
        choice = None
        while choice != "finish":
            choice = get_valid_choice(
                choices,
                prompt="what do you want to change? (type finish to quit):",
                error_callback=text.equip_fail,
            )
        if choice == "armour":
            self.equip_armour(user)
        elif choice == "weapon":
            self.equip_weapon(user)
        elif choice == "accessory":
            self.equip_accessory(user)

    def display_equipment(self, user: Character) -> None:
        """sub action for equip() to display equipments that the user have"""
        print()
        print(f"Armour : {user.armour or 'Empty'}")
        print(f"Weapon : {user.weapon or 'Empty'}")
        print(f"Accessory : {user.accessory or 'Empty'}")
        pause()

    def equip_armour(self, user: Character) -> None:
        """sub action from equip() for user to choose an armour to equip"""
        if not user.armours:
            show_text(text.NO_ARMOUR)
            return
        # Displays the armours the user owns
        print("\nIn your inventory you have: ")
        choice = get_valid_choice(
            list(user.armours.keys()),
            prompt="Which armour do you want to equip?",
            error_callback=text.equip_nonexistent,
        )
        show_text(text.equip_succeed(choice))
        armour = user.armours[choice]
        user.armour = armour
        self.display_equipment(user)

    def equip_weapon(self, user: Character) -> None:
        """sub action from equip() for user to choose a weapon to equip"""
        if not user.weapons:
            show_text(text.NO_WEAPON)
            return
        # Displays the weapons the user owns
        print("\nIn your inventory you have: ")
        choice = get_valid_choice(
            list(user.weapons.keys()),
            prompt="Which weapon do you want to equip?",
            error_callback=text.equip_nonexistent,
        )
        print(text.equip_succeed(choice))
        user.weapon = user.weapons[choice]
        self.display_equipment(user)

    def equip_accessory(self, user: Character) -> None:
        """sub action from equip() for user to choose an accessory to equip"""
        if not user.accessories:
            show_text(text.NO_ACCESSORIES)
            return
        print("\nIn your inventory you have: ")
        choice = get_valid_choice(
            list(user.accessories.keys()),
            prompt="Which accessory do you want to equip?",
            error_callback=text.equip_nonexistent,
        )
        print(text.equip_succeed(choice))

        # Undo stat boost from the previous accessory
        if user.accessory:
            user.take_damage(user.accessory.health_boost)
            user.use_mana(user.accessory.mana_boost)

        # Adds the stat boost from the new accessory
        accessory = user.accessories[choice]
        user.accessory = accessory
        user.add_health(user.accessory.health_boost)
        user.add_mana(user.accessory.mana_boost)
        self.display_equipment(user)

    def status(self, user: Character) -> None:
        """main action that prints user's status"""
        # Displays the users statistics
        print(f"\nName: {user.name}")
        print(f"Health: {user.health} / {user.get_max_health()}")
        print(f"Mana: {user.mana} / {user.get_max_mana()}")
        print(f"Defence: {user.get_defence()}")
        print(f"Strength: {user.get_attack()}")
        pause()

    def info(self, user: Character) -> None:
        """main action that prompts user for the type of item to find out more information about"""
        choices = [
            "weapons", "spells", "armours",
            "accessories", "flasks", "items"
        ]
        choice = get_valid_choice(
            choices,
            prompt="What do you want to find out more about?",
            error_callback=text.do_not_have,
        )
        if choice == "weapons":
            self.weapon_info(user)
        elif choice == "spells":
            self.spell_info(user)
        elif choice == "armours":
            self.armour_info(user)
        elif choice == "accessories":
            self.accessory_info(user)
        elif choice == "flasks":
            self.flask_info(user)
        elif choice == "items":
            self.item_info(user)

    def weapon_info(self, user: Character) -> None:
        """sub action from equip() that prompts user for specific weapon to find out more about"""
        # Check if the user owns any weapons
        if not user.weapons:
            show_text(text.do_not_have("weapons"))
            return
        # Displays the weapons the user owns
        print("\nIn your inventory you have: ")
        choice = get_valid_choice(
            list(user.weapons.keys()),
            prompt="Which weapon do you want to find out more about?",
            error_callback=text.do_not_have,
        )
        # Displays the description of the weapon
        show_text(user.weapons[choice].description)

    def spell_info(self, user: Character) -> None:
        """sub action from equip() that prompts user for specific spell to find out more about"""
        # Check if the user knows any spells
        if not user.spells:
            show_text(text.do_not_have("spells"))
            return
        # Displays the spells the user knows
        print("\nIn your inventory you have: ")
        choice = get_valid_choice(
            list(user.spells.keys()),
            prompt="Which spell do you want to find out more about?",
            error_callback=text.do_not_have,
        )
        # Displays the description of the spell
        show_text(user.spells[choice].description)

    def armour_info(self, user: Character) -> None:
        """sub action from equip() that prompts user for specific armour to find out more about"""
        # Check if the user owns any armours
        if not user.armours:
            show_text(text.do_not_have("armour"))
            return
        # Displays the armours the user owns
        print("\nIn your inventory you have: ")
        choice = get_valid_choice(
            list(user.armours.keys()),
            prompt="Which armour do you want to find out more about?",
            error_callback=text.do_not_have,
        )
        # Displays the description of the armour
        show_text(user.armours[choice].description)

    def accessory_info(self, user: Character) -> None:
        """sub action from equip() that prompts user for specific accessory to find out more about"""
        # Checks if the user owns any accessories
        if not user.accessories:
            show_text(text.do_not_have("accessories"))
            return
        # Displays the accessories the user owns
        print("\nIn your inventory you have: ")
        choice = get_valid_choice(
            list(user.accessories.keys()),
            prompt="Which accessory do you want to find out more about?",
            error_callback=text.do_not_have,
        )
        # Displays the description of the accessory
        show_text(user.accessories[choice].description)

    def flask_info(self, user: Character) -> None:
        """sub action from equip() that prompts user for specific flask to find out more about"""
        choices = [
            str(user.health_flask),
            str(user.mana_flask),
        ]
        print("\nIn your inventory you have: ")
        choice = get_valid_choice(
            choices,
            prompt="Which flask do you want to find out more about?",
            error_callback=text.do_not_have,
        )
        if choice == str(user.health_flask).lower():
            show_text(self.health_flask.description)
        elif choice == str(user.health_flask).lower():
            show_text(self.mana_flask.description)
        else:
            show_text(text.do_not_have(choice))

    def item_info(self, user: Character) -> None:
        """sub action from equip() that prompts user for specific special item to find out more about"""
        # Check if the user owns any items
        if not user.items:
            show_text(text.do_not_have("items"))
            return
        # Displays the items the user owns
        print("\nIn your inventory you have: ")
        choice = get_valid_choice(
            list(user.items.keys()),
            prompt="Which item do you want to find out more about?",
            error_callback=text.do_not_have,
        )
        # Displays the description of the items
        show_text(user.items[choice].description)

    def display_room_name(self) -> None:
        """prints the room's name in a cool way"""
        print("=" * 25)
        space = " " * int((25 - len(str(self.room))) / 2)
        print(f"{space}{self.room}{space}")
        print("=" * 25)
        pause()

    def display_room_description(self) -> None:
        """prints the room's description"""
        show_text(self.room.description)
        pause()  # extra pause
        self.look(self.room)
        self.room.been_here = True

    def get_action(self) -> str:
        """sub action for run() that prompts user for a main action"""
        choice = get_valid_choice(
            self.actions,
            prompt="What do you wish to do? (type help for list of actions)",
            error_callback=text.action_fail,
        )
        return choice

    def collect_loot(self, attacker: Character, loot: item.Item) -> None:
        """sub method from attack() to collect loot of defeated monster"""
        if loot.type == "weapon":
            attacker.take_weapon(loot)
            show_text(text.obtain_thing(loot, loot.type))
        elif loot.type == "spell":
            attacker.take_spell(loot)
            show_text(text.obtain_thing(loot, loot.type))
        elif loot.type == "armour":
            attacker.take_armour(loot)
            show_text(text.obtain_thing(loot, loot.type))
        elif loot.type == "accessory":
            attacker.take_accessory(loot)
            show_text(text.obtain_thing(loot, loot.type))

    def end_game(self) -> None:
        """displays scenario when user dies"""
        print(text.YOU_DIED)
        self.end = True

    def win(self, weapon) -> None:
        """displays scenario when user wins"""
        show_text(text.win_game(weapon))
        print(text.GOD_SLAIN)
        self.end = True

    def die(self) -> None:
        """to end the game"""
        self.end_game()
        self.end = True

    def secret(self) -> None:
        """secret account that gives God like stats by setting name as meow"""
        print(
            "\nWelcome chosen one, the Gods smile upon you and have rained down their blessing\n"
        )
        time.sleep(1)
        self.character.health = 999
        self.character.max_health = 999
        self.character.mana = 999
        self.character.max_mana = 999
        self.character.attack = 999
        self.character.defence = 999
        self.character.health_flask.count = 997
        self.character.mana_flask.count = 997

    def meow(self) -> None:
        choices = [
            text.MEOW_1,
            text.MEOW_2,
            text.MEOW_3,
            text.MEOW_4,
            text.MEOW_5,
            text.MEOW_6,
            text.MEOW_7,
            text.MEOW_8,
            text.MEOW_9,
            text.MEOW_10,
        ]
        print(random.choice(choices))
