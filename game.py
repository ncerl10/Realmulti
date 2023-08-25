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
    """
    
    def __init__(self) -> None:
        temp = setup()
        self.end = False
        self.room = temp[0]
        self.character = temp[1]
        self.actions = ["help", "look", "move", "loot", "flask", "attack", "equip", "status", "info", "die"]
        self.description = ["Gets the list of possible actions", "Looks around the room","Move to another room", "Search the room for loot", "Drink your flasks", "Attack the enemny", "Change your equipment", "See your statistics", "Find out more about your items", "Ends the game"]
    
    def intro(self) -> None:
        # start of the game
        print('Welcome to Hogwarts School of Witchcraft and Wizardry')
        time.sleep(1)
        print("\nThe Dark Lord Voldemort has taken over Hogwarts School and opened multiple interdimensional gates, bringing hoards of enemies into the school. Your job as the chosen one is to traverse the school in order to locate the Principal's Office and thwart Voldemort's evil plan to take over the world\n")
        time.sleep(2)

        decision = input('Do you wish to enter the school? ( yes / no ): ')
        
        if decision.lower() == "yes":
            name = input('\nTarnished, key in your name: ')
            self.character.set_name(name)
            if name == "meow":
                self.meow()
            else:
                print("\nYou boldly opened the front gates of the school and made your way into the first room")
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
        self.display_room_name()

        # Checks if the player has entered the room before
        if not self.room.get_been_here():
            # Displays a description of the room if the player has not been there before
            self.display_room_description()
        
        decision = self.get_action()
        
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
        
    def help(self) -> None:
        print("\nYou are able to:")
        for i, action in enumerate(self.actions):
            print(f"- {action} ({self.description[i]})")
        time.sleep(1)
        
    def look(self, room : Room) -> None:
        print("\n", end="")
        
        if room.get_left() != None:
            print(f"To the left is {room.get_left().get_name()}")
            
        if room.get_right() != None:
            print(f"To the right is {room.get_right().get_name()}")
            
        if room.get_forward() != None:
            print(f"In front of you is {room.get_forward().get_name()}")
            
        if room.get_back() != None:
            print(f"Behind you is {room.get_back().get_name()}")

        time.sleep(1)
        if room.get_enemy() != None:
            print(f"\nIn the middle of the room is {room.get_enemy().get_name()}, {room.get_enemy().get_description()}")

        time.sleep(1)

    def move(self, room : Room) -> None:
        movement = input('\nWhich direction do you wish to move in? (left, right, forward, back): ')
        
        if movement.lower() not in ["left", "right", "forward", "back"]:
            print(f"\nYou do not know what direction {movement} is and got confused")
            time.sleep(1)

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
                elif room.get_forward().get_name() == "Principal's Office":
                    items = []
                    for item in self.character.get_items():
                        items.append(item.get_name())
                    if "Dectus Medallion (right)" in items and "Dectus Medallion (left)" in items:
                        print("\nCongratulations, you placed the two Dectus Medallions together releasing trememndous amounts of energy, breaking the powerful spell on the door")
                        time.sleep(1)
                        self.room = room.get_forward()
                    else:
                        print("\nYou tried entering the Principal's Office but the door was locked by a powerful spell")
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

        chance = random.randint(1, 3)
        caught = False

        if self.room.get_enemy() != None:
            if chance != 1:
                caught = True
            else:
                print(f"\nBy some miracle you managed to loot the room without {self.room.get_enemy().get_name()} noticing")
                time.sleep(1)

        if not caught:
            if loot == None:
                print("\nYou searched every nook and cranny but there was nothing to be found")
                time.sleep(1)
            
            elif loot.get_name() == "Flask of Crimson Tears":
                print(f"\nYou found a {loot.get_name()}, a powerful flask")
                time.sleep(1)
                user.set_health_flask(1)
                self.set_loot(None)
    
            elif loot.get_name() == "Flask of Cerulean Tears":
                print(f"\nYou found a {loot.get_name()}, a powerful flask")
                time.sleep(1)
                user.set_mana_flask(1)
                self.set_loot(None)
                
            elif loot.get_name() == "Dectus Medallion (right)":
                print(f"\nYou found a {loot.get_name()}, a powerful item")
                time.sleep(1)
                user.set_items(loot)
                self.set_loot(None)
    
            elif loot.get_name() == "Dectus Medallion (left)":
                print(f"\nYou found a {loot.get_name()}, a powerful item")
                time.sleep(1)
                user.set_items(loot)
                self.set_loot(None)

        else:
            print(f"\n{self.room.get_enemy().get_name()} noticed you while you tried to loot the room")
            time.sleep(1)
            self.attack(user, self.room.get_enemy())

    def flask(self, user : Character) -> None:
        if (user.get_health_flask() + user.get_mana_flask()) == 0:
            print("\nYou ran out of flasks\n")
            time.sleep(1)
        else:
            self.use_flask(user)

    def attack(self, attacker : Character , victim: Enemy) -> None:
        if victim == None:
            print("\nYou attacked the air and realised how insane you looked")
            time.sleep(1)
        else:
            while attacker.get_health() > 0:
                print(f"\n{'-'*50}\n")
                print(f"{attacker.get_name()} has {attacker.get_health()} health")
                print(f"{attacker.get_name()} has {attacker.get_mana()} mana")
                time.sleep(1)
                print(f"\n{victim.get_name()} has {victim.get_health()} health\n")
                time.sleep(1)

                decision = self.get_choice(attacker)
                
                if decision == "flask":
                    self.use_flask(attacker)
                    if victim.get_health() > 0:
                        damage = max(1, victim.get_attack() - attacker.get_defence())
                        attacker.set_health(attacker.get_health() - damage)
                        print(f"\n{victim.get_name()} used {victim.get_move()}, dealing {damage} damage to {attacker.get_name()}")
                        time.sleep(1)
                    
                else:
                    damage, weapon = self.get_attack(attacker, decision)
                    
                    victim.set_health(victim.get_health() - (damage + attacker.get_attack()))
                    if victim.get_health() > 0:
                        print(f"\n{attacker.get_name()}{weapon.get_move()}, dealing {damage} damage to {victim.get_name()}")
                        time.sleep(1)
                    
                    if victim.get_health() > 0:
                        damage = max(1, victim.get_attack() - attacker.get_defence())
                        attacker.set_health(attacker.get_health() - damage)
                        print(f"\n{victim.get_name()} used {victim.get_move()}, dealing {damage} damage to {attacker.get_name()}")
                        time.sleep(1)
    
                    else:
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

                        elif choice.lower() == "no":
                            print(f"\nYou left {victim.get_loot().get_name()} on the ground and allowed the resourceful rat to steal it")
                            time.sleep(1)
                        else:
                            print(f"\nYour indecisiveness allowed the resourceful rat to steal the {victim.get_loot().get_name()} when you weren't looking")
                            time.sleep(1)
                        self.room.set_enemy(None)
                        break

            if attacker.get_health() <= 0:
                self.end_game()

        return None

    def get_choice(self, user : Character) -> str:
        decision = input(f"What do you want to use? ({user.get_weapon().get_name()} / Spell / Flask): ")
        
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
            elif decision.lower() == "spell" and user.get_mana() < min(cost):
                print("\nYou do not have enough mana to cast spells\n")
                time.sleep(1)
                decision = input(f"What do you want to use? ({user.get_weapon().get_name()} / Spell / Flask): ")
                valid = False
            elif decision.lower() == "flask" and (user.get_health_flask() + user.get_mana_flask()) == 0:
                print("\nYou ran out of flasks\n")
                time.sleep(1)
                decision = input(f"What do you want to use? ({user.get_weapon().get_name()} / Spell / Flask): ")    
                valid = False

        return decision
    
    def get_attack(self, user : Character, decision : str) -> [int, Weapon]:
        
        if decision.lower() == user.get_weapon().get_name().lower():
            return user.get_weapon().get_attack(), user.get_weapon()

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
            cost = user.get_spells()[spells.index(choice)].get_cost()
            print(f"\nYou used up {cost} mana points")
            time.sleep(1)
            user.set_mana(user.get_mana() - cost)
            return user.get_spells()[spells.index(choice)].get_attack(), user.get_spells()[spells.index(choice)]

    def use_flask(self, user : Character) -> None:
        self.display_flask(user)
        selection = input("Which flask would you like to drink?: ")
        valid = False
        while not valid:
            valid = True
            if selection.lower() not in ["flask of crimson tears", "flask of cerulean tears"]:
                print(f"\nYou tried drinking {selection} but nothing happened\n")
                time.sleep(1)
                selection = input("Which flask would you like to drink?: ")
                valid = False
            elif selection.lower() == "flask of crimson tears" and user.get_health_flask() == 0:
                print("\nYou ran out of Flask of Crimson Tears\n")
                time.sleep(1)
                selection = input("Which flask would you like to drink?: ")
                valid = False
            elif selection.lower() == "flask of cerulean tears" and user.get_mana_flask() == 0:
                print("\nYou ran out of Flask of Cerulean Tears\n")
                time.sleep(1)
                selection = input("Which flask would you like to drink?: ")
                valid = False

        if selection.lower() == "flask of crimson tears":
            final_health = min(user.get_max_health(), user.get_health() + FlaskOfCrimsonTears().get_health())
            healing = final_health - user.get_health()
            print(f"\nYou drank a Flask of Crimson Tears and gained {healing} health")
            time.sleep(1)
            user.set_health(final_health)
            user.set_health_flask(-1)
            
        elif selection.lower() == "flask of cerulean tears":
            final_mana = min(user.get_max_mana(), user.get_mana() + FlaskOfCeruleanTears().get_mana())
            healing = final_mana - user.get_mana()
            print(f"\nYou drank a Flask of Cerulean Tears and gained {healing} mana")
            time.sleep(1)
            user.set_mana(final_mana)
            user.set_mana_flask(-1)
    
    def display_flask(self, user : Character) -> None:
        print(f"\nNumber of Flask of Crimson Tears in inventory : {user.get_health_flask()} (restores {FlaskOfCrimsonTears().get_health()} health)")
        print(f"Number of Flask of Cerulean Tears in inventory: {user.get_mana_flask()} (restores {FlaskOfCeruleanTears().get_mana()} mana)\n")
        time.sleep(1)
        
    def equip(self, user) -> None:

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
        print("\nSpells:")
        for i, spell in enumerate(user.spells):
            print(f"- {spell.get_name()} ({spell.get_cost()} mana)")

    def equip_armour(self, user : Character) -> None:
        if len(user.get_armours()) == 0:
            print("\nYou do not have any armour to equip")
            time.sleep(1)
        else:
            print("\nIn your inventory you have: ")
            items = []
            for armour in user.get_armours():
                print(f"- {armour.get_name()}")
                items.append(armour.get_name().lower())
            time.sleep(1)
            option = input("\nWhich armour do you want to equip?: ")
            if option.lower() not in items:
                print(f"\nYou tried equipping {option} but realised you cant create things out of thin air")
                time.sleep(1)
            else:
                print(f"\nYou equipped {option}")
                time.sleep(1)
                if user.get_armour() != None:
                    user.set_defence(user.get_defence() - user.get_armour().get_defence())
                armour = user.get_armours()[items.index(option.lower())]
                user.set_defence(user.get_defence() + armour.get_defence())
                user.set_armour(armour)
                self.display_equipment(user)

    def equip_weapon(self, user : Character) -> None:
        if len(user.get_weapons()) == 0:
            print("\nYou do not have any weapon to equip")
            time.sleep(1)
        else:
            print("\nIn your inventory you have: ")
            items = []
            for weapon in user.get_weapons():
                print(f"- {weapon.get_name()}")
                items.append(weapon.get_name().lower())
            time.sleep(1)
            option = input("\nWhich weapon do you want to equip?: ")
            if option.lower() not in items:
                print(f"\nYou tried equipping {option} but realised you cant create things out of thin air")
            else:
                print(f"\nYou equipped {option}")
                time.sleep(1)
                user.set_weapon(user.get_weapons()[items.index(option.lower())])
                self.display_equipment(user)

    def equip_accessory(self, user : Character) -> None:
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
                
                if user.get_accessory() != None:
                    user.set_max_health(user.get_max_health() - user.get_accessory().get_health_boost())

                    new_health = min(max(1, user.get_health() - user.get_accessory().get_health_boost()), user.get_max_health())
                    user.set_health(new_health)
                    
                    user.set_max_mana(user.get_max_mana() - user.get_accessory().get_mana_boost())

                    new_mana = min(max(0, user.get_mana() - user.get_accessory().get_mana_boost()), user.get_max_mana())
                    user.set_mana(new_mana)

                    user.set_attack(user.get_attack() - user.get_accessory().get_attack_boost())

                    user.set_defence(user.get_defence() - user.get_accessory().get_defence_boost())
                    
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
        print(f"\nName: {user.get_name()}")
        print(f"Health: {user.get_health()} / {user.get_max_health()}")
        print(f"Mana: {user.get_mana()} / {user.get_max_mana()}")
        print(f"Defence: {user.get_defence()}")
        print(f"Strength: {user.get_attack()}")
        time.sleep(1)

    def info(self, user : Character) -> None:
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
        if len(user.get_weapons()) == 0:
            print("\nYou do not own any weapons yet")

        else:
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
                print("\n", end="")
                print(user.get_weapons()[weapons.index(decision)].get_description())
                time.sleep(1)

    def spell_info(self, user : Character) -> None:
        if len(user.get_spells()) == 0:
            print("\nYou do not own any spells yet")

        else:
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
                print("\n", end="")
                print(user.get_spells()[spells.index(decision)].get_description())
                time.sleep(1)

    def armour_info(self, user : Character) -> None:
        if len(user.get_armours()) == 0:
            print("\nYou do not own any amours yet")

        else:
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
                print("\n", end="")
                print(user.get_armours()[armours.index(decision)].get_description())
                time.sleep(1)

    def accessory_info(self, user : Character) -> None:
        if len(user.get_accessories()) == 0:
            print("\nYou do not own any accessories yet")

        else:
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
                print("\n", end="")
                print(user.get_accessories()[accessories.index(decision)].get_description())
                time.sleep(1)

    def flask_info(self) -> None:
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
        if len(user.get_items()) == 0:
            print("\nYou do not own any items yet")
        else:
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
                print("\n", end="")
                print(user.get_items()[items.index(decision)].get_description())
                time.sleep(1)
                
    def display_room_name(self) -> None:
        print("\n=========================")
        space = " "*int((25-len(self.room.get_name()))/2)
        print(f"{space}{self.room.get_name()}{space}")
        print("=========================")
        time.sleep(1)

    def display_room_description(self) -> None:
        print("\n", end="")
        print(self.room.description)
        time.sleep(2)
        self.look(self.room)
        self.room.set_been_here(True)

    def get_action(self) -> str:
        
        decision = input("\nWhat do you wish to do? (type help for list of actions): ")
        
        while decision not in self.actions:
            print(f"\nYou do not have the physical and mental capability to {decision}")
            time.sleep(1)
            decision = input("\nWhat do you wish to do? (type help for list of actions): ")

        return decision

    def collect_loot(self, attacker : Character, loot : Item) -> None:
        
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
        print("__   _______ _   _  ______ _____ ___________")
        print("\ \ / /  _  | | | | |  _  \_   _|  ___|  _  \\")
        print(" \ V /| | | | | | | | | | | | | | |__ | | | |")
        print("  \ / | | | | | | | | | | | | | |  __|| | | |")
        print("  | | \ \_/ / |_| | | |/ / _| |_| |___| |/ /")
        print("  \_/  \___/ \___/  |___/  \___/\____/|___/ ")
        self.end = True

    def win(self, weapon) -> None:
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
        self.end_game()
        self.end = True

    def use_item(self):
        # change available items when needed
        available_items = ['weapon', 'potion']
        decision = input('\nWhich of the following item do you wish to use? (weapon, potion):')
        while decision not in available_items:
                   decision = input('\nWhich of the following item do you wish to use? (weapon, potion):')
            
        if decision == 'weapon':
            self.use_weapon()

        elif decision == 'potion':
            self.use_potion()

        else:
            raise ValueError(f'{decision}')
            
    def use_weapon(self) -> None:
        choice = self.prompt_user_choice(self.character.weapon, '\nChoose a weapon to equip: ')
        
        # remove battle points from weapon currently
        if self.character.equip != None:
            self.character.battle_points -= self.character.equip.attack
        # add battle points from new weapon
        self.character.equip = self.character.weapon[choice]
        self.character.battle_points += self.character.weapon[choice].attack

    def use_potion(self) -> None:
        choice = self.prompt_user_choice(self.character.potion, "\nChoose a potion to consume: ")

        # add effects from consumable
        if self.character.potion[choice].attack != 0:
            self.character.battle_points += self.character.potion[choice].attack
        if self.character.potion[choice].heal != 0:
            self.character.set_health(self.character.potion[choice].heal)

        # remove potion from list of potion available
        self.character.potion.pop(choice)

    def prompt_user_choice(self, items: list, question: str) -> int:        
        for i, item in enumerate(items):
            print(f"[{i}]: {item}")
        choice = None
        while not choice:
            choice = input(question + " ")
            if not choice.isdecimal():
                print("Invalid choice")
                continue
            if int(choice) >= len(items):
                print("Invalid choice")
                continue
            return int(choice)
            

    def meow(self) -> None:
        print("\nWelcome chosen one, the Gods smile upon you and have rained down their blessing")
        time.sleep(1)
        self.character.set_health(999)
        self.character.set_max_health(999)
        self.character.set_mana(999)
        self.character.set_max_mana(999)
        self.character.set_attack(999)
        self.character.set_defence(999)
        self.character.set_health_flask(999)
        self.character.set_mana_flask(999)
