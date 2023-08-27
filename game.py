#import from python built in libraries
import time
import random

#import from other files
from setup import *

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
    - loot(self, user : Character, loot : Item) -> None
    - flask(self, user : Character) -> None
    - attack(self, attacker : Character , victim: Enemy) -> None
    - get_choice(self, user : Character) -> str
    - get_attack(self, user : Character, decision : str) -> [int, Weapon]
    - use_flask_battle(self, user : Character) -> None
    - use_flask(self, user : Character) -> None
    - display_flask(self, user : Character) -> None
    - equip(self, user) -> None
    - display_equipment(self, user : Character) -> None
    - display_spells(self, user : Character) -> None
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
    - collect_loot(self, attacker : Character, loot : Item) -> None
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
        self.actions = ["help", "look", "move", "loot", "flask", "attack", "equip", "status", "info", "die", "meow"]
        self.description = ["Gets the list of possible actions", "Looks around the room","Move to another room", "Search the room for loot", "Drink your flasks", "Attack the enemny", "Change your equipment", "See your statistics", "Find out more about your items", "Ends the game", "meow"]
    
    def intro(self) -> None:
        """print introduction for the start of the game """
        
        # Displays the introduction messages
        print('Welcome to Hogwarts School of Witchcraft and Wizardry')
        time.sleep(1)
        print("\nThe Dark Lord Voldemort has taken over Hogwarts School and opened multiple interdimensional gates, bringing hoards of enemies into the school. Your job as the chosen one is to traverse the school in order to locate The Shrieking Shack and thwart Voldemort's evil plan to take over the world\n")
        time.sleep(2)

        decision = input('Do you wish to enter the school? ( yes / no ): ')
        
        if decision.lower() == "yes":
            name = input('\nTarnished, key in your name: ')
            self.character.set_name(name)
            # Check if the user used the secret easter egg name
            if name == "meow":
                self.secret()
            else:
                print("\nYou boldly opened the front gates of the school and made your way into the first room\n")
                time.sleep(1)
        elif decision.lower() == "no":
            print("\nDue to your utter cowardice, voldemort continued gaining power, spreading his control and chaos all over the world, leading to the complete annihlation of the human race")
            self.end = True
            time.sleep(1)
            self.end_game()
            return
        else:
            print("\nDue to your indecision, voldemort continued gaining power, spreading his control and chaos all over the world, leading to the complete annihlation of the human race")
            self.end = True
            time.sleep(1)
            self.end_game()
            return
        
    def run(self) -> None:
        """to be run in a loop to prompt user's action"""
        self.display_room_name()

        # Checks if the player has entered the room before
        if not self.room.get_been_here():
            # Displays a description of the room if the player has not been there before
            self.display_room_description()
        
        decision = self.get_action()

        # Does the action the user selected
        
        if decision.lower() == "help":
            self.help()

        elif decision.lower() == "look":
            self.look(self.room)
            
        elif decision.lower() == "move":
            self.move(self.room)
            
        elif decision.lower() == "attack":
            self.attack(self.character, self.room.get_enemy())

        elif decision.lower() == "loot":
            self.loot(self.character, self.room.get_loot())

        elif decision.lower() == "flask":
            self.flask(self.character)

        elif decision.lower() == "equip":
            self.equip(self.character)

        elif decision.lower() == "status":
            self.status(self.character)

        elif decision.lower() == "info":
            self.info(self.character)

        elif decision.lower() == "die":
            self.die()

        elif decision.lower() == "meow":
            self.meow()
        
    def help(self) -> None:
        """main action for user to get the list of possible actions"""
        # Displays the list of actions the user can do
        print("\nYou are able to:")
        for i, action in enumerate(self.actions):
            print(f"- {action} ({self.description[i]})")
        time.sleep(1)
        
    def look(self, room : Room) -> None:
        """main action to look around the room including rooms linked to the room and enemies in the room"""
        print("\n", end="")

        # Displays the connected rooms
        if room.get_left() != None:
            print(f"To the left is {room.get_left().get_name()}")
            
        if room.get_right() != None:
            print(f"To the right is {room.get_right().get_name()}")
            
        if room.get_forward() != None:
            print(f"In front of you is {room.get_forward().get_name()}")
            
        if room.get_back() != None:
            print(f"Behind you is {room.get_back().get_name()}")

        time.sleep(1)

        # Displays the enemy in the room
        if room.get_enemy() != None:
            print(f"\nIn the middle of the room is {room.get_enemy().get_name()}, {room.get_enemy().get_description()}")

        time.sleep(1)

    def move(self, room : Room) -> None:
        """main action for user to traverse from one room to another"""
        movement = input('\nWhich direction do you wish to move in? (left, right, forward, back): ')

        # Validates the users choice
        if movement.lower() not in ["left", "right", "forward", "back"]:
            print(f"\nYou do not know what direction {movement} is and got confused")
            time.sleep(1)

        # Generate a random number to see if you managed to sneak past the enemy
        chance = random.randint(1, 3)
        caught = False
        
        if room.get_enemy() != None:
            if chance == 1:
                caught = True
            else:
                print(f"\nYou managed to sneak past {room.get_enemy().get_name()}")
                time.sleep(1)

        if not caught:
            if movement.lower() == "left":
                if room.get_left() == None:
                    print("\nYou walked to the left and smashed into a wall")
                    time.sleep(1)
    
                else:
                    self.room = room.get_left()
    
            if movement.lower() == "right":
                if room.get_right() == None:
                    print("\nYou walked to the right and smashed into a wall")
                    time.sleep(1)
                else:
                    self.room = room.get_right()
    
            if movement.lower() == "forward":
                if room.get_forward() == None:
                    print("\nYou walked forward and smashed into a wall")
                    time.sleep(1)
                # Check if you are going to the final boss room
                elif room.get_forward().get_name() == "The Shrieking Shack":
                    items = []
                    for item in self.character.get_items():
                        items.append(item.get_name())
                    # Checks if you have the required items to enter the final boss room
                    if "Dectus Medallion (right)" in items and "Dectus Medallion (left)" in items:
                        print("\nCongratulations, you placed the two Dectus Medallions together releasing trememndous amounts of energy, breaking the powerful spell on the door")
                        time.sleep(1)
                        self.room = room.get_forward()
                    else:
                        print("\nYou tried entering the The Shrieking Shack but the door was locked by a powerful spell")
                        time.sleep(1)
                        print("\nYou probably need to find a special item to break the spell (remember to loot all the rooms)")
                        time.sleep(1)
                else:
                    self.room = room.get_forward()
    
            if movement.lower() == "back":
                if room.get_back() == None:
                    print("\nYou turned back and smashed into a wall")
                    time.sleep(1)
                else:
                    self.room = room.get_back()

        else:
            print(f"\nYou tried to sneak to another room but {room.get_enemy().get_name()} noticed you")
            time.sleep(1)
            self.attack(self.character, room.get_enemy())

    def loot(self, user : Character, loot : Item) -> None:
        """main action for user to search the room for loot"""

        # Generate a random number to see if you successfully loot the room whithout the enemy noticing
        chance = random.randint(1, 3)
        caught = False

        if self.room.get_enemy() != None:
            if chance != 1:
                caught = True
            else:
                print(f"\nBy some miracle you managed to loot the room without {self.room.get_enemy().get_name()} noticing")
                time.sleep(1)

        if not caught:
            # Allow the user to loot the room
            if loot == None:
                print("\nYou searched every nook and cranny but there was nothing to be found")
                time.sleep(1)
            
            elif loot.get_name() == "Flask of Crimson Tears":
                print(f"\nYou found a {loot.get_name()}, a powerful flask")
                time.sleep(1)
                user.set_health_flask(1)
                self.room.set_loot(None)
    
            elif loot.get_name() == "Flask of Cerulean Tears":
                print(f"\nYou found a {loot.get_name()}, a powerful flask")
                time.sleep(1)
                user.set_mana_flask(1)
                self.room.set_loot(None)
                
            elif loot.get_name() == "Dectus Medallion (right)":
                print(f"\nYou found a {loot.get_name()}, a powerful item")
                time.sleep(1)
                user.set_items(loot)
                self.room.set_loot(None)
    
            elif loot.get_name() == "Dectus Medallion (left)":
                print(f"\nYou found a {loot.get_name()}, a powerful item")
                time.sleep(1)
                user.set_items(loot)
                self.room.set_loot(None)

        else:
            print(f"\n{self.room.get_enemy().get_name()} noticed you while you tried to loot the room")
            time.sleep(1)
            self.attack(user, self.room.get_enemy())

    def flask(self, user : Character) -> None:
        """main action for user to drink their flasks"""
        # Check if the user still has available flasks
        if (user.get_health_flask() + user.get_mana_flask()) == 0:
            print("\nYou ran out of flasks\n")
            time.sleep(1)
        else:
            self.use_flask(user)

    def attack(self, attacker : Character , victim: Enemy) -> None:
        """main action for user to attack the enemy in the room"""
        # Check if there is an enemy in the room
        if victim == None:
            print("\nYou attacked the air and realised how insane you looked")
            time.sleep(1)
        else:
            while attacker.get_health() > 0:
                # Display users health and mana
                print(f"\n{'-'*50}\n")
                print(f"{attacker.get_name()} has {attacker.get_health()} health")
                print(f"{attacker.get_name()} has {attacker.get_mana()} mana")
                print(f"{attacker.get_name()} has {attacker.get_health_flask()} Flask of Crimson Tears")
                print(f"{attacker.get_name()} has {attacker.get_mana_flask()} Flask of Cerulean Tears")
                time.sleep(1)
                # Display enemy's health
                print(f"\n{victim.get_name()} has {victim.get_health()} health\n")
                time.sleep(1)

                decision = self.get_choice(attacker)
                
                if decision == "flask":
                    self.use_flask_battle(attacker)
                    if victim.get_health() > 0:
                        damage = max(1, victim.get_attack() - attacker.get_defence())
                        attacker.set_health(attacker.get_health() - damage)
                        print(f"\n{victim.get_name()} used {victim.get_move()}, dealing {damage} damage to {attacker.get_name()}")
                        time.sleep(1)
                    
                else:
                    damage, weapon = self.get_attack(attacker, decision)

                    # Deal damage to enemy
                    victim.set_health(victim.get_health() - (damage + attacker.get_attack()))
                    # Check if enemy died
                    if victim.get_health() > 0:
                        print(f"\n{attacker.get_name()}{weapon.get_move()}, dealing {damage} damage to {victim.get_name()}")
                        time.sleep(1)
                    # Allow enemy to attack if it didn't die yet
                    if victim.get_health() > 0:
                        damage = max(1, victim.get_attack() - attacker.get_defence())
                        attacker.set_health(attacker.get_health() - damage)
                        print(f"\n{victim.get_name()} used {victim.get_move()}, dealing {damage} damage to {attacker.get_name()}")
                        time.sleep(1)
    
                    else:
                        # Check if dead enemy is the final boss
                        if victim.get_name() == "Voldemort":
                            self.win(weapon)
                            return
                        print(f"\n{attacker.get_name()}{weapon.get_win_front()}{victim.get_name()}{weapon.get_win_back()}")
                        time.sleep(1)
                        print(f"\n{victim.get_name()} dropped a {victim.get_loot().get_name()}")
                        time.sleep(1)
                        choice = input(f"\nDo you want to pick {victim.get_loot().get_name()}? ( yes / no ): ")
                        if choice.lower() == "yes":
                            self.collect_loot(attacker, victim.get_loot())
                            time.sleep(1)
                            print()
                            print(victim.get_loot().get_description())
                            print()
                            time.sleep(1)

                        elif choice.lower() == "no":
                            print(f"\nYou left {victim.get_loot().get_name()} on the ground and allowed the resourceful rat to steal it")
                            time.sleep(1)
                        else:
                            print(f"\nYour indecisiveness allowed the resourceful rat to steal the {victim.get_loot().get_name()} when you weren't looking")
                            time.sleep(1)
                        # Removes the enemy from the room
                        self.room.set_enemy(None)
                        break
            # Check if the user died
            if attacker.get_health() <= 0:
                self.end_game()

    def get_choice(self, user : Character) -> str:
        """sub action from attack() to prompt user for attack methods or use of flask"""
        decision = input(f"What do you want to use? ({user.get_weapon().get_name()} / Spell / Flask): ")

        # Get a list of spell cost
        cost = []
        for spell in user.get_spells():
            cost.append(spell.get_cost())

        valid = False
        while not valid:
            valid = True
            if decision.lower() not in [user.get_weapon().get_name().lower(), "spell", "flask"]:
                print(f"\nYou tried to use {decision} but nothing happened")
                time.sleep(1)
                decision = input(f"\nWhat do you want to use? ({user.get_weapon().get_name()} / Spell / Flask): ")
                valid = False
            # Check if user has enough mana to cast spells
            elif decision.lower() == "spell" and user.get_mana() < min(cost):
                print("\nYou do not have enough mana to cast spells\n")
                time.sleep(1)
                decision = input(f"What do you want to use? ({user.get_weapon().get_name()} / Spell / Flask): ")
                valid = False
            # Check if user has any flask to drink
            elif decision.lower() == "flask" and (user.get_health_flask() + user.get_mana_flask()) == 0:
                print("\nYou ran out of flasks\n")
                time.sleep(1)
                decision = input(f"What do you want to use? ({user.get_weapon().get_name()} / Spell / Flask): ")    
                valid = False

        return decision
    
    def get_attack(self, user : Character, decision : str) -> [int, Weapon]:
        """sub action from attack() to get total damage done to victim"""

        # Check if user used his weapon
        if decision.lower() == user.get_weapon().get_name().lower():
            return user.get_weapon().get_attack(), user.get_weapon()

        # check if user used spells
        elif decision.lower() == "spell":
            self.display_spells(user)
            time.sleep(1)
            spells = []
            for spell in user.spells:
                spells.append(spell.get_name().lower())
            choice = input("\nWhich spell would you like to cast?: ")
            while choice.lower() not in spells:
                print(f"\nYou tried to cast {choice} but it blew up in your face")
                time.sleep(1)
                choice = input("\nWhich spell would you like to cast?: ")
            cost = user.get_spells()[spells.index(choice.lower())].get_cost()
            print(f"\nYou used up {cost} mana points")
            time.sleep(1)
            user.set_mana(user.get_mana() - cost)
            return user.get_spells()[spells.index(choice.lower())].get_attack(), user.get_spells()[spells.index(choice)]

    def use_flask_battle(self, user : Character) -> None:
        """sub action from get_choice() to prompt user for the flask to drink"""
        self.display_flask(user)
        selection = input("Which flask would you like to drink?: ")
        valid = False
        while not valid:
            valid = True
            # Validates user selection
            if selection.lower() not in ["flask of crimson tears", "flask of cerulean tears"]:
                print(f"\nYou tried drinking {selection} but nothing happened\n")
                time.sleep(1)
                selection = input("Which flask would you like to drink?: ")
                valid = False
            # Checks if the user has enough flask of crimson tears
            elif selection.lower() == "flask of crimson tears" and user.get_health_flask() == 0:
                print("\nYou ran out of Flask of Crimson Tears\n")
                time.sleep(1)
                selection = input("Which flask would you like to drink?: ")
                valid = False
            # Checks if the user has enough flask of cerulean tears
            elif selection.lower() == "flask of cerulean tears" and user.get_mana_flask() == 0:
                print("\nYou ran out of Flask of Cerulean Tears\n")
                time.sleep(1)
                selection = input("Which flask would you like to drink?: ")
                valid = False

        if selection.lower() == "flask of crimson tears":
            # Makes sure the health healed does not exceed the maximum health
            final_health = min(user.get_max_health(), user.get_health() + FlaskOfCrimsonTears().get_health())
            healing = final_health - user.get_health()
            print(f"\nYou drank a Flask of Crimson Tears and gained {healing} health")
            time.sleep(1)
            user.set_health(final_health)
            user.set_health_flask(-1)
            
        elif selection.lower() == "flask of cerulean tears":
            # Makes sure the mana gained does not exceed the maximum mana
            final_mana = min(user.get_max_mana(), user.get_mana() + FlaskOfCeruleanTears().get_mana())
            healing = final_mana - user.get_mana()
            print(f"\nYou drank a Flask of Cerulean Tears and gained {healing} mana")
            time.sleep(1)
            user.set_mana(final_mana)
            user.set_mana_flask(-1)
                
    def use_flask(self, user : Character) -> None:
        """Function to allow the user to use flask but also allows them to cancel the action"""
        self.display_flask(user)
        selection = input("Which flask would you like to drink? (type cancel to quit): ")
        valid = False
        while not valid:
            valid = True
            # Validates user selection
            if selection.lower() not in ["flask of crimson tears", "flask of cerulean tears", "cancel"]:
                print(f"\nYou tried drinking {selection} but nothing happened\n")
                time.sleep(1)
                selection = input("Which flask would you like to drink?: ")
                valid = False
            # Checks if the user has enough flask of crimson tears
            elif selection.lower() == "flask of crimson tears" and user.get_health_flask() == 0:
                print("\nYou ran out of Flask of Crimson Tears\n")
                time.sleep(1)
                selection = input("Which flask would you like to drink?: ")
                valid = False
            # Checks if the user has enough flask of cerulean tears
            elif selection.lower() == "flask of cerulean tears" and user.get_mana_flask() == 0:
                print("\nYou ran out of Flask of Cerulean Tears\n")
                time.sleep(1)
                selection = input("Which flask would you like to drink?: ")
                valid = False

            elif selection.lower() == "cancel":
                return

        if selection.lower() == "flask of crimson tears":
            # Makes sure the health healed does not exceed the maximum health
            final_health = min(user.get_max_health(), user.get_health() + FlaskOfCrimsonTears().get_health())
            healing = final_health - user.get_health()
            print(f"\nYou drank a Flask of Crimson Tears and gained {healing} health")
            time.sleep(1)
            user.set_health(final_health)
            user.set_health_flask(-1)
            
        elif selection.lower() == "flask of cerulean tears":
            # Makes sure the mana gained does not exceed the maximum mana
            final_mana = min(user.get_max_mana(), user.get_mana() + FlaskOfCeruleanTears().get_mana())
            healing = final_mana - user.get_mana()
            print(f"\nYou drank a Flask of Cerulean Tears and gained {healing} mana")
            time.sleep(1)
            user.set_mana(final_mana)
            user.set_mana_flask(-1)
    
    def display_flask(self, user : Character) -> None:
        """sub action from use_flask to display flask in inventory"""
        print(f"\nNumber of Flask of Crimson Tears in inventory : {user.get_health_flask()} (restores {FlaskOfCrimsonTears().get_health()} health)")
        print(f"Number of Flask of Cerulean Tears in inventory: {user.get_mana_flask()} (restores {FlaskOfCeruleanTears().get_mana()} mana)\n")
        time.sleep(1)
        
    def equip(self, user) -> None:
        """main action for user to equip various items"""

        self.display_equipment(user)

        decision = input("\ndo you want to change your equipment? ( yes / no ): ")

        if decision.lower() == "no":
            return

        elif decision.lower() == "yes":
            choice = ""
            while choice != "finish":
                choice = input("\nwhat do you want to change? (type finish to quit): ")
                while choice.lower() not in ["armour", "weapon", "accessory", "finish"]:
                    print(f"\nYou tried changing your {choice} but nothing happened")
                    choice = input("\nwhat do you want to change? (type finish to quit): ")
    
                if choice.lower() == "armour":
                    self.equip_armour(user)

                elif choice.lower() == "weapon":
                    self.equip_weapon(user)

                elif choice.lower() == "accessory":
                    self.equip_accessory(user)
    
    def display_equipment(self, user : Character) -> None:
        """sub action for equip() to display equipments that the user have"""
        
        if user.armour == None:
            print("\nArmour : Empty")
        else:
            print(f"\nArmour : {user.armour.get_name()}")

        if user.weapon == None:
            print("Weapon : Empty")
        else:
            print(f"Weapon : {user.weapon.get_name()}")

        if user.accessory == None:
            print("Accessory : Empty")
        else:
            print(f"Accessory : {user.accessory.get_name()}")
        time.sleep(1)

    def display_spells(self, user : Character) -> None:
        """sub action from get_attack() to display spells that the user have"""
        # Displays all spells owned
        print("\nSpells:")
        for i, spell in enumerate(user.spells):
            print(f"- {spell.get_name()} ({spell.get_cost()} mana)")

    def equip_armour(self, user : Character) -> None:
        """sub action from equip() for user to choose an armour to equip"""
        if len(user.get_armours()) == 0:
            print("\nYou do not have any armour to equip")
            time.sleep(1)
        else:
            # Displays the armours the user owns
            print("\nIn your inventory you have: ")
            items = []
            for armour in user.get_armours():
                print(f"- {armour.get_name()}")
                items.append(armour.get_name().lower())
            time.sleep(1)
            option = input("\nWhich armour do you want to equip?: ")
            # Validates the users choice
            if option.lower() not in items:
                print(f"\nYou tried equipping {option} but realised you cant create things out of thin air")
                time.sleep(1)
            else:
                print(f"\nYou equipped {option}")
                time.sleep(1)
                # Removes the defence increase of the previous armour
                if user.get_armour() != None:
                    user.set_defence(user.get_defence() - user.get_armour().get_defence())
                armour = user.get_armours()[items.index(option.lower())]
                # Adds the defence of the new armour
                user.set_defence(user.get_defence() + armour.get_defence())
                user.set_armour(armour)
                self.display_equipment(user)

    def equip_weapon(self, user : Character) -> None:
        """sub action from equip() for user to choose a weapon to equip"""
        if len(user.get_weapons()) == 0:
            print("\nYou do not have any weapon to equip")
            time.sleep(1)
        else:
            # Displays the weapons the user owns
            print("\nIn your inventory you have: ")
            items = []
            for weapon in user.get_weapons():
                print(f"- {weapon.get_name()}")
                items.append(weapon.get_name().lower())
            time.sleep(1)
            # Validates the user's choice
            option = input("\nWhich weapon do you want to equip?: ")
            if option.lower() not in items:
                print(f"\nYou tried equipping {option} but realised you cant create things out of thin air")
            else:
                print(f"\nYou equipped {option}")
                time.sleep(1)
                user.set_weapon(user.get_weapons()[items.index(option.lower())])
                self.display_equipment(user)

    def equip_accessory(self, user : Character) -> None:
        """sub action from equip() for user to choose an accessory to equip"""
        if len(user.accessories) == 0:
            print("\nYou do not have any accessories to equip")
            time.sleep(1)
        else:
            print("\nIn your inventory you have: ")
            items = []
            for accessory in user.get_accessories():
                print(f"- {accessory.get_name()}")
                items.append(accessory.get_name().lower())
            time.sleep(1)
            option = input("\nWhich accessory do you want to equip?: ")
            if option.lower() not in items:
                print(f"\nYou tried equipping {option} but realised you cant create things out of thin air")
            else:
                print(f"\nYou equipped {option}")
                time.sleep(1)

                # Removes the stat boost from the previous accessory
                if user.get_accessory() != None:
                    user.set_max_health(user.get_max_health() - user.get_accessory().get_health_boost())

                    new_health = min(max(1, user.get_health() - user.get_accessory().get_health_boost()), user.get_max_health())
                    user.set_health(new_health)
                    
                    user.set_max_mana(user.get_max_mana() - user.get_accessory().get_mana_boost())

                    new_mana = min(max(0, user.get_mana() - user.get_accessory().get_mana_boost()), user.get_max_mana())
                    user.set_mana(new_mana)

                    user.set_attack(user.get_attack() - user.get_accessory().get_attack_boost())

                    user.set_defence(user.get_defence() - user.get_accessory().get_defence_boost())

                # Adds the stat boost from the new accessory
                accessory = user.get_accessories()[items.index(option.lower())]
                user.set_health(user.get_health() + accessory.get_health_boost())
                user.set_max_health(user.get_max_health() + accessory.get_health_boost())
                user.set_attack(user.get_attack() + accessory.get_attack_boost())
                user.set_mana(user.get_mana() + accessory.get_mana_boost())
                user.set_max_mana(user.get_max_mana() + accessory.get_mana_boost())
                user.set_accessory(accessory)
                user.set_defence(user.get_defence() + user.get_accessory().get_defence_boost())
                self.display_equipment(user)

    def status(self, user : Character) -> None:
        """main action that prints user's status"""
        # Displays the users statistics
        print(f"\nName: {user.get_name()}")
        print(f"Health: {user.get_health()} / {user.get_max_health()}")
        print(f"Mana: {user.get_mana()} / {user.get_max_mana()}")
        print(f"Defence: {user.get_defence()}")
        print(f"Strength: {user.get_attack()}")
        time.sleep(1)

    def info(self, user : Character) -> None:
        """main action that prompts user for the type of item to find out more information about"""
        choice = input("\nWhat do you want to find out more about? (weapons, spells, armours, accessories, flasks, items): ")
        
        if choice.lower() not in ["weapons", "spells", "armours", "accessories", "flasks", "items"]:
            print(f"\nYou do not own any {choice}")

        elif choice == "weapons":
            self.weapon_info(user)

        elif choice == "spells":
            self.spell_info(user)

        elif choice == "armours":
            self.armour_info(user)

        elif choice == "accessories":
            self.accessory_info(user)

        elif choice == "flasks":
            self.flask_info()

        elif choice == "items":
            self.item_info(user)
                
    def weapon_info(self, user : Character) -> None:
        """sub action from equip() that prompts user for specific weapon to find out more about"""
        # Check if the user owns any weapons
        if len(user.get_weapons()) == 0:
            print("\nYou do not own any weapons yet")

        else:
            # Displays the weapons the user owns
            weapons = []
            print("\nIn your inventory you have: ")
            for weapon in user.get_weapons():
                print(f"- {weapon.get_name()}")
                weapons.append(weapon.get_name().lower())
            time.sleep(1)

            decision = input("\nWhich weapon do you want to find out more about? : ")
            if decision.lower() not in weapons:
                print(f"You do not own {decision}")

            else:
                # Displays the description of the weapon
                print("\n", end="")
                print(user.get_weapons()[weapons.index(decision)].get_description())
                time.sleep(1)

    def spell_info(self, user : Character) -> None:
        """sub action from equip() that prompts user for specific spell to find out more about"""
        # Check if the user knows any spells
        if len(user.get_spells()) == 0:
            print("\nYou do not own any spells yet")

        else:
            # Displays the spells the user knows
            spells = []
            print("\nIn your inventory you have: ")
            for spell in user.get_spells():
                print(f"- {spell.get_name()}")
                spells.append(spell.get_name().lower())
            time.sleep(1)

            decision = input("\nWhich spell do you want to find out more about? : ")
            if decision.lower() not in spells:
                print(f"You do not own {decision}")

            else:
                # Displays the description of the spell
                print("\n", end="")
                print(user.get_spells()[spells.index(decision)].get_description())
                time.sleep(1)

    def armour_info(self, user : Character) -> None:
        """sub action from equip() that prompts user for specific armour to find out more about"""
        # Check if the user owns any armours
        if len(user.get_armours()) == 0:
            print("\nYou do not own any amours yet")

        else:
            # Displays the armours the user owns
            armours = []
            print("\nIn your inventory you have: ")
            for armour in user.get_armours():
                print(f"- {armour.get_name()}")
                armours.append(armour.get_name().lower())
            time.sleep(1)

            decision = input("\nWhich armour do you want to find out more about? : ")
            if decision.lower() not in armours:
                print(f"You do not own {decision}")

            else:
                # Displays the description of the armour
                print("\n", end="")
                print(user.get_armours()[armours.index(decision)].get_description())
                time.sleep(1)

    def accessory_info(self, user : Character) -> None:
        """sub action from equip() that prompts user for specific accessory to find out more about"""
        # Checks if the user owns any accessories
        if len(user.get_accessories()) == 0:
            print("\nYou do not own any accessories yet")

        else:
            # Displays the accessories the user owns
            accessories = []
            print("\nIn your inventory you have: ")
            for accessory in user.get_accessories():
                print(f"- {accessory.get_name()}")
                accessories.append(accessory.get_name().lower())
            time.sleep(1)

            decision = input("\nWhich accesssory do you want to find out more about? : ")
            if decision.lower() not in accessories:
                print(f"You do not own {decision}")

            else:
                # Displays the description of the accessory
                print("\n", end="")
                print(user.get_accessories()[accessories.index(decision)].get_description())
                time.sleep(1)

    def flask_info(self) -> None:
        """sub action from equip() that prompts user for specific flask to find out more about"""
        print("\nIn your inventory you have: ")
        print("- Flask of Crimson Tears")
        print("- Flask of Cerulean Tears")

        decision = input("\nWhich accesssory do you want to find out more about? : ")
        if decision.lower() == "flask of crimson tears":
            print("\n", end ="")
            print(FlaskOfCrimsonTears().get_description())
            time.sleep(1)
        elif decision.lower() == "flask of cerulean tears":
            print("\n", end ="")
            print(FlaskOfCecruleanTears().get_description())
            time.sleep(1)
        else:
            print(f"You do not own {decision}")

    def item_info(self, user : Character) -> None:
        """sub action from equip() that prompts user for specific special item to find out more about"""
        # Check if the user owns any items
        if len(user.get_items()) == 0:
            print("\nYou do not own any items yet")
        else:
            # Displays the items the user owns
            items = []
            print("\nIn your inventory you have: ")
            for item in user.get_items():
                print(f"- {item.get_name()}")
                items.append(item.get_name().lower())
            time.sleep(1)
    
            decision = input("\nWhich item do you want to find out more about? : ")
            if decision.lower() not in items:
                print(f"You do not own {decision}")
    
            else:
                # Displays the description of the items
                print()
                print(user.get_items()[items.index(decision)].get_description())
                time.sleep(1)
                
    def display_room_name(self) -> None:
        """prints the room's name in a cool way"""
        print("="*25)
        space = " "*int((25-len(self.room.get_name()))/2)
        print(f"{space}{self.room.get_name()}{space}")
        print("="*25)
        time.sleep(1)

    def display_room_description(self) -> None:
        """prints the room's description"""
        print()
        print(self.room.description)
        time.sleep(2)
        self.look(self.room)
        self.room.set_been_here(True)

    def get_action(self) -> str:
        """sub action for run() that prompts user for a main action"""
        decision = input("\nWhat do you wish to do? (type help for list of actions): ")

        # Validate the users decision
        while decision not in self.actions:
            print(f"\nYou do not have the physical and mental capability to {decision}")
            time.sleep(1)
            decision = input("\nWhat do you wish to do? (type help for list of actions): ")

        return decision

    def collect_loot(self, attacker : Character, loot : Item) -> None:
        """sub method from attack() to collect loot of defeated monster"""
        if loot.get_type() == "weapon":
            attacker.set_weapons(loot)
            print(f"\nYou obtained a {loot.get_name()}, a powerful weapon")
            time.sleep(1)
            
        elif loot.get_type() == "spell":
            attacker.set_spells(loot)
            print(f"\nYou obtained a {loot.get_name()}, a powerful spell")
            time.sleep(1)

        elif loot.get_type() == "armour":
            attacker.set_armours(loot)
            print(f"\nYou obtained a {loot.get_name()}, a powerful armour")
            time.sleep(1)

        elif loot.get_type() == "accessory":
            attacker.set_accessories(loot)
            print(f"\nYou obtained a {loot.get_name()}, a powerful accessory")
            time.sleep(1)

    def end_game(self) -> None:
        """displays scenario when user dies"""
        print("__   _______ _   _  ______ _____ ___________")
        print("\ \ / /  _  | | | | |  _  \_   _|  ___|  _  \\")
        print(" \ V /| | | | | | | | | | | | | | |__ | | | |")
        print("  \ / | | | | | | | | | | | | | |  __|| | | |")
        print("  | | \ \_/ / |_| | | |/ / _| |_| |___| |/ /")
        print("  \_/  \___/ \___/  |___/  \___/\____/|___/ ")
        self.end = True

    def win(self, weapon) -> None:
        """displays scenario when user wins"""
        print(f"\nUsing the almighty {weapon.get_name()}, you struck the Dark Lord Voldemort down, crippling him of all his powers and stop his evil tyranny over the school")
        time.sleep(1)
        print(" _____ ___________   _____ _       ___  _____ _   _ ")
        print("|  __ \  _  |  _  \ /  ___| |     / _ \|_   _| \ | |")
        print("| |  \/ | | | | | | \ `--.| |    / /_\ \ | | |  \| |")
        print("| | __| | | | | | |  `--. \ |    |  _  | | | | . ` |")
        print("| |_\ \ \_/ / |/ /  /\__/ / |____| | | |_| |_| |\  |")
        print(" \____/\___/|___/   \____/\_____/\_| |_/\___/\_| \_/")
        self.end = True

    def die(self) -> None:
        """to end the game"""
        self.end_game()
        self.end = True
           
    def secret(self) -> None:
        """secret account that gives God like stats by setting name as meow"""
        print("\nWelcome chosen one, the Gods smile upon you and have rained down their blessing\n")
        time.sleep(1)
        self.character.set_health(999)
        self.character.set_max_health(999)
        self.character.set_mana(999)
        self.character.set_max_mana(999)
        self.character.set_attack(999)
        self.character.set_defence(999)
        self.character.set_health_flask(997)
        self.character.set_mana_flask(997)

    def meow(self) -> None:
        choice = random.randint(1, 10)
        if choice == 1:
            print("""  
  __  __  U _____ u U  ___ u             
U|' \/ '|u\| ___"|/  \/"_ \/__        __ 
\| |\/| |/ |  _|"    | | | |\"\      /"/ 
 | |  | |  | |___.-,_| |_| |/\ \ /\ / /\ 
 |_|  |_|  |_____|\_)-\___/U  \ V  V /  U
<<,-,,-.   <<   >>     \\  .-,_\ /\ /_,-.
 (./  \.) (__) (__)   (__)  \_)-'  '-(_/ """)
        elif choice == 2:
            print("""                                
   ____ ___  ___  ____ _      __
  / __ `__ \/ _ \/ __ \ | /| / /
 / / / / / /  __/ /_/ / |/ |/ / 
/_/ /_/ /_/\___/\____/|__/|__/  
                                """)
        elif choice == 3:
            print(""" 
 .----------------.  .----------------.  .----------------.  .----------------. 
| .--------------. || .--------------. || .--------------. || .--------------. |
| | ____    ____ | || |  _________   | || |     ____     | || | _____  _____ | |
| ||_   \  /   _|| || | |_   ___  |  | || |   .'    `.   | || ||_   _||_   _|| |
| |  |   \/   |  | || |   | |_  \_|  | || |  /  .--.  \  | || |  | | /\ | |  | |
| |  | |\  /| |  | || |   |  _|  _   | || |  | |    | |  | || |  | |/  \| |  | |
| | _| |_\/_| |_ | || |  _| |___/ |  | || |  \  `--'  /  | || |  |   /\   |  | |
| ||_____||_____|| || | |_________|  | || |   `.____.'   | || |  |__/  \__|  | |
| |              | || |              | || |              | || |              | |
| '--------------' || '--------------' || '--------------' || '--------------' |
 '----------------'  '----------------'  '----------------'  '----------------' """)

        elif choice == 4:
            print("""                              
                              
 _ __ ___   ___  _____      __
| '_ ` _ \ / _ \/ _ \ \ /\ / /
| | | | | |  __/ (_) \ V  V / 
|_| |_| |_|\___|\___/ \_/\_/  
                              
                              """)

        elif choice == 5:
            print(""" 
 _  _  ____  __   _  _ 
( \/ )(  __)/  \ / )( \
/ \/ \ ) _)(  O )\ /\ /
\_)(_/(____)\__/ (_/\_)""")

        elif choice == 6:
            print("""                              
 _ __ ___   ___  _____      __
| '_ ` _ \ / _ \/ _ \ \ /\ / /
| | | | | |  __/ (_) \ V  V / 
|_| |_| |_|\___|\___/ \_/\_/  
                              """)

        elif choice == 7:
            print("""                                    
                                    
,--,--,--. ,---.  ,---. ,--.   ,--. 
|        || .-. :| .-. ||  |.'.|  | 
|  |  |  |\   --.' '-' '|   .'.   | 
`--`--`--' `----' `---' '--'   '--' 
                                    """)

        elif choice == 8:
            print(""" 
 __    __     ______     ______     __     __    
/\ "-./  \   /\  ___\   /\  __ \   /\ \  _ \ \   
\ \ \-./\ \  \ \  __\   \ \ \/\ \  \ \ \/ ".\ \  
 \ \_\ \ \_\  \ \_____\  \ \_____\  \ \__/".~\_\ 
  \/_/  \/_/   \/_____/   \/_____/   \/_/   \/_/ 
                                                 """)

        elif choice == 9:
            print("""                                        
                                        
 _ .--..--.  .---.   .--.   _   _   __  
[ `.-. .-. |/ /__\\/ .'`\ \[ \ [ \ [  ] 
 | | | | | || \__.,| \__. | \ \/\ \/ /  
[___||__||__]'.__.' '.__.'   \__/\__/   
                                        """)

        elif choice == 10:
            print(""" 
_      _____ ____  _     
/ \__/|/  __//  _ \/ \  /|
| |\/|||  \  | / \|| |  ||
| |  |||  /_ | \_/|| |/\||
\_/  \|\____\\____/\_/  \|
                          """)