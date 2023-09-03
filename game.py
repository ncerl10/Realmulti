#import from python built in libraries
import time
import random

#import from other files
from setup import *
import tkinter as tk
import map

root = tk.Tk()
root.geometry('600x600')
root.configure(bg='black')
text = tk.Text(root, height = 560, width = 560, state = "disabled", background = "black", foreground = "white")
text.pack()

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
    

temp = setup()
selfend = False
selfroom = temp[0]
selfcharacter = temp[1]
selfrooms = []
selfactions = ["help", "look", "move", "loot", "flask", "attack", "equip", "status", "info", "die", "settings", "map", "meow"]
selfdescription = ["Gets the list of possible actions", "Looks around the room","Move to another room", "Search the room for loot", "Drink your flasks", "Attack the enemny", "Change your equipment", "See your statistics", "Find out more about your items", "Ends the game", "Change settings", "Shows map", "Meow"]
selfteleportable = False
selfmap = map.game_map()
out = []
with open("settings.txt", "r") as f:
    out = f.readlines()
    out = [x.split()[1] for x in out]
selfsleep = int(out[0])

def write(txt):
    text['state'] = 'normal'
    text.insert(tk.END, txt+"\n")
    text['state'] = 'disabled'

def delete():
    text.delete("1.0", tk.END)
    pass
def intro():
    """print introduction for the start of the game """
    
    # Displays the introduction messages
    print('Welcome to Hogwarts School of Witchcraft and Wizardry')
    time.sleep(selfsleep)
    print("\nThe Dark Lord Voldemort has taken over Hogwarts and opened multiple interdimensional gates, bringing hordes of enemies into the school. Your job as the chosen one is to traverse the school in order to locate The Shrieking Shack and thwart Voldemort's evil plan to take over the world.\n")
    time.sleep(selfsleep)
    decision = input('Do you wish to enter the school? ( yes / no ): ')
    
    if decision.lower() == "yes":
        name = input('\nTarnished, key in your name: ')
        selfcharacter.name = name
        # Check if the user used the secret easter egg name
        if name == "meow":
            secret()
        else:
            print("\nYou boldly opened the front gates of the school and made your way into the first room\n")
            time.sleep(selfsleep)
    elif decision.lower() == "no":
        print("\nDue to your utter cowardice, voldemort continued to gain power, spreading his control and chaos all over the world, leading to the complete annihilation of the human race.")
        selfend = True
        time.sleep(selfsleep)
        end_game()
        return
    else:
        print("\nDue to your indecision, voldemort continued to gain power, spreading his control and chaos all over the world, leading to the complete annihlation of the human race.")
        selfend = True
        time.sleep(selfsleep)
        end_game()
        return
        
def run():
    """to be run in a loop to prompt user's action"""
    display_room_name()

    # Checks if the player has entered the room before
    if not selfroom.been_here:
        # Displays a description of the room if the player has not been there before
        display_room_description()
        selfrooms.append(selfroom)
        
        if selfroom.name == "Dirtmouth":
            selfmap.dirtmouth_enter()
        elif selfroom.name == "Celestial Resort":
            selfmap.celestial_resort_enter()
        elif selfroom.name == "The Forge":
            selfmap.forge_enter()
        elif selfroom.name == "Stormveil Castle":
            selfmap.stormveil_enter()
        elif selfroom.name == "Aperture Lab":
            selfmap.aperture_enter()
        elif selfroom.name == "Zebes":
            selfmap.zebes_enter()
        elif selfroom.name == "Bunker":
            selfmap.bunker_enter()
        elif selfroom.name == "Asphodel":
            selfmap.asphodel_enter()
        elif selfroom.name == "Kingdom of Ku":
            selfmap.kingdom_ku_enter()
        elif selfroom.name == "Greenhill Zone":
            selfmap.greenhill_enter()
        elif selfroom.name == "The Hallow":
            selfmap.hallow_enter()
        elif selfroom.name == "Commencement":
            selfmap.commencement_enter()
        elif selfroom.name == "Midgar":
            selfmap.midgar_enter()
        elif selfroom.name == "Hyrule Kingdom":
            selfmap.hyrule_enter()
        elif selfroom.name == "The End Dimension":
            selfmap.end_dimension_enter()
        elif selfroom.name == "Kamurocho":
            selfmap.kamurocho_enter()
        elif selfroom.name == "Tower of Fate":
            selfmap.tower_enter()
        elif selfroom.name == "Shores of Nine":
            selfmap.shores_enter()
        elif selfroom.name == "Mementos":
            selfmap.mementos_enter()
        elif selfroom.name == "Ascent":
            selfmap.ascent_enter()
        elif selfroom.name == "The Shrieking Shack":
            selfmap.shrieking_enter()
        elif selfroom.name == "6th Circle of Hell":
            selfmap.sixth_circle_enter()
        elif selfroom.name == "Snowdin":
            selfmap.snowdin_enter()
        elif selfroom.name == "The Sealed Temple":
            selfmap.sealed_temple_enter()
        elif selfroom.name == "The Astral Plane":
            selfmap.astral_plane_enter()
        elif selfroom.name == "The Obra Dinn":
            selfmap.obradinn_enter()
        elif selfroom.name == "The Mushroom Kingdom":
            selfmap.mushroom_enter()
        elif selfroom.name == "Walled City 99":
            selfmap.walled_enter()
        elif selfroom.name == "The Last Resort":
            selfmap.last_resort_enter()
    
    decision = get_action()

    # Does the action the user selected
    
    if decision.lower() == "help":
        help()

    elif decision.lower() == "look":
        look(selfroom)
        
    elif decision.lower() == "move":
        move(selfroom)
        
    elif decision.lower() == "attack":
        attack(selfcharacter, selfroom.enemy)

    elif decision.lower() == "loot":
        loot(selfcharacter, selfroom.loot)

    elif decision.lower() == "flask":
        flask(selfcharacter)

    elif decision.lower() == "equip":
        equip(selfcharacter)

    elif decision.lower() == "status":
        status(selfcharacter)

    elif decision.lower() == "info":
        info(selfcharacter)

    elif decision.lower() == "die":
        die()

    elif decision.lower() == "meow":
        meow()

    elif decision.lower() == "settings":
        settings()

    elif selfteleportable == True and decision.lower() == "teleport":
        teleport()

    elif decision.lower() == "map":
        selfmap.display()

    if selfroom.enemy == None and selfroom.loot == None:
        if selfroom.name == "Dirtmouth":
            selfmap.dirtmouth_clear()
        elif selfroom.name == "Celestial Resort":
            selfmap.celestial_resort_clear()
        elif selfroom.name == "The Forge":
            selfmap.forge_clear()
        elif selfroom.name == "Stormveil Castle":
            selfmap.stormveil_clear()
        elif selfroom.name == "Aperture Lab":
            selfmap.aperture_clear()
        elif selfroom.name == "Zebes":
            selfmap.zebes_clear()
        elif selfroom.name == "Bunker":
            selfmap.bunker_clear()
        elif selfroom.name == "Asphodel":
            selfmap.asphodel_clear()
        elif selfroom.name == "Kingdom of Ku":
            selfmap.kingdom_ku_clear()
        elif selfroom.name == "Greenhill Zone":
            selfmap.greenhill_clear()
        elif selfroom.name == "The Hallow":
            selfmap.hallow_clear()
        elif selfroom.name == "Commencement":
            selfmap.commencement_clear()
        elif selfroom.name == "Midgar":
            selfmap.midgar_clear()
        elif selfroom.name == "Hyrule Kingdom":
            selfmap.hyrule_clear()
        elif selfroom.name == "The End Dimension":
            selfmap.end_dimension_clear()
        elif selfroom.name == "Kamurocho":
            selfmap.kamurocho_clear()
        elif selfroom.name == "Tower of Fate":
            selfmap.tower_clear()
        elif selfroom.name == "Shores of Nine":
            selfmap.shores_clear()
        elif selfroom.name == "Mementos":
            selfmap.mementos_clear()
        elif selfroom.name == "Ascent":
            selfmap.ascent_clear()
        elif selfroom.name == "The Shrieking Shack":
            selfmap.shrieking_clear()
        elif selfroom.name == "6th Circle of Hell":
            selfmap.sixth_circle_clear()
        elif selfroom.name == "Snowdin":
            selfmap.snowdin_clear()
        elif selfroom.name == "The Sealed Temple":
            selfmap.sealed_temple_clear()
        elif selfroom.name == "The Astral Plane":
            selfmap.astral_plane_clear()
        elif selfroom.name == "The Obra Dinn":
            selfmap.obradinn_clear()
        elif selfroom.name == "The Mushroom Kingdom":
            selfmap.mushroom_clear()
        elif selfroom.name == "Walled City 99":
            selfmap.walled_clear()
        elif selfroom.name == "The Last Resort":
            selfmap.last_resort_clear()
        
def help():
    """main action for user to get the list of possible actions"""
    # Displays the list of actions the user can do
    print("\nYou are able to:")
    for i, action in enumerate(selfactions):
        print(f"- {action} ({selfdescription[i]})")
    time.sleep(selfsleep)
        
def look(room):
    """main action to look around the room including rooms linked to the room and enemies in the room"""
    print("\n", end="")

    # Displays the connected rooms
    if room.left != None:
        print(f"To the left is {room.left.name}")
        
    if room.right != None:
        print(f"To the right is {room.right.name}")
        
    if room.forward != None:
        print(f"In front of you is {room.forward.name}")
        
    if room.back != None:
        print(f"Behind you is {room.back.name}")

    time.sleep(selfsleep)
    upgrades = selfcharacter.get_upgrades()

    if "Virtual Boo" in upgrades:
        if room.enemy != None:
            print(f"\nIn the middle of the room is {room.enemy.name}, {room.enemy.description}")
            time.sleep(selfsleep)
            print(f"\n{room.enemy.name} has {room.enemy.health} health")
            time.sleep(selfsleep)
        if room.loot != None:
            print(f"\nThere is {room.loot.name} hidden in {room.name}")
            time.sleep(selfsleep)
        else:
            print(f"\nThere is no loot hidden in {room.name}")
            time.sleep(selfsleep)
        
    elif room.enemy != None:
    # Displays the enemy in the room
        print(f"\nIn the middle of the room is {room.enemy.name}, {room.enemy.description}")

    time.sleep(selfsleep)

def move(room):
    """main action for user to traverse from one room to another"""
    movement = input('\nWhich direction do you wish to move in? (left, right, forward, back): ')

    # Validates the users choice
    if movement.lower() not in ["left", "right", "forward", "back"]:
        print(f"\nYou do not know what direction {movement} is and got confused")
        time.sleep(selfsleep)

    # Generate a random number to see if you managed to sneak past the enemy
    caught = False

    if selfcharacter.name == "meow":
        chance = 2
    else:
        chance = random.randint(1, 3)
        
    if room.enemy != None:
        if chance == 1:
            caught = True
        else:
            print(f"\nYou managed to sneak past {room.enemy.name}")
            time.sleep(selfsleep)

    if not caught:
        if movement.lower() == "left":
            if room.left == None:
                print("\nYou walked to the left and smashed into a wall")
                time.sleep(selfsleep)

            else:
                selfroom = room.left

        if movement.lower() == "right":
            if room.right == None:
                print("\nYou walked to the right and smashed into a wall")
                time.sleep(selfsleep)
            else:
                selfroom = room.right

        if movement.lower() == "forward":
            if room.forward == None:
                print("\nYou walked forward and smashed into a wall")
                time.sleep(selfsleep)
            # Check if you are going to the final boss room
            elif room.forward.name == "The Shrieking Shack":
                items = selfcharacter.get_items()
                # Checks if you have the required items to enter the final boss room
                if "Dectus Medallion (right)" in items and "Dectus Medallion (left)" in items:
                    print("\nCongratulations, you placed the two Dectus Medallions together releasing trememndous amounts of energy, breaking the powerful spell on the door")
                    time.sleep(selfsleep)
                    selfroom = room.forward
                else:
                    print("\nYou tried entering the The Shrieking Shack but the door was locked by a powerful spell")
                    time.sleep(selfsleep)
                    print("\nYou probably need to find a special item to break the spell (remember to loot all the rooms)")
                    time.sleep(selfsleep)
            else:
                selfroom = room.forward

        if movement.lower() == "back":
            if room.back == None:
                print("\nYou turned back and smashed into a wall")
                time.sleep(selfsleep)
            else:
                selfroom = room.back

    else:
        print(f"\nYou tried to sneak to another room but {room.enemy.name} noticed you")
        time.sleep(selfsleep)
        attack(selfcharacter, room.enemy)

def loot(user, loot):
    """main action for user to search the room for loot"""

    # Generate a random number to see if you successfully loot the room whithout the enemy noticing
    caught = False

    if user.name == "meow":
        chance = 1
    else:
        chance = random.randint(1, 3)

    if selfroom.enemy != None:
        if chance != 1:
            caught = True
        else:
            print(f"\nBy some miracle you managed to loot the room without {selfroom.enemy.name} noticing")
            
            time.sleep(selfsleep)

    if not caught:
        # Allow the user to loot the room
        if loot == None:
            print("\nYou searched every nook and cranny but there was nothing to be found")
            time.sleep(selfsleep)
        
        elif loot.name == "Flask of Crimson Tears":
            print(f"\nYou found a {loot.name}, a powerful flask")
            time.sleep(selfsleep)
            user.health_flask += 1
            selfroom.loot = None

        elif loot.name == "Flask of Cerulean Tears":
            print(f"\nYou found a {loot.name}, a powerful flask")
            time.sleep(selfsleep)
            user.mana_flask += 1
            selfroom.loot = None
            
        elif loot.name == "Dectus Medallion (right)":
            print(f"\nYou found a {loot.name}, a powerful item")
            time.sleep(selfsleep)
            user.items.append(loot)
            selfroom.loot = None

        elif loot.name == "Dectus Medallion (left)":
            print(f"\nYou found a {loot.name}, a powerful item")
            time.sleep(selfsleep)
            user.items.append(loot)
            selfroom.loot = None

    else:
        print(f"\n{selfroom.enemy.name} noticed you while you tried to loot the room")
        time.sleep(selfsleep)
        attack(user, selfroom.enemy)

def flask(user):
    """main action for user to drink their flasks"""
    # Check if the user still has available flasks
    if (user.health_flask + user.mana_flask) == 0:
        print("\nYou ran out of flasks\n")
        time.sleep(selfsleep)
    else:
        use_flask(user)

def attack(attacker, victim):
    """main action for user to attack the enemy in the room"""
    # Check if there is an enemy in the room
    if victim == None:
        print("\nYou attacked the air and realised how insane you looked")
        time.sleep(selfsleep)
    else:
        while attacker.health > 0:
            # Display users health and mana
            print(f"\n{'-'*50}\n")
            print(f"{attacker.name} has {attacker.health} health")
            print(f"{attacker.name} has {attacker.mana} mana")
            print(f"{attacker.name} has {attacker.health_flask} Flask of Crimson Tears")
            print(f"{attacker.name} has {attacker.mana_flask} Flask of Cerulean Tears")
            time.sleep(selfsleep)
            # Display enemy's health
            print(f"\n{victim.name} has {victim.health} health\n")
            time.sleep(selfsleep)

            decision = get_choice(attacker)
            
            if decision == "flask":
                use_flask_battle(attacker)
                if victim.health > 0:
                    damage = max(1, victim.attack - attacker.defence)
                    attacker.health = attacker.health - damage
                    print(f"\n{victim.name} used {victim.move}, dealing {damage} damage to {attacker.name}")
                    time.sleep(selfsleep)
                
            else:
                damage, weapon = get_attack(attacker, decision)

                # Deal damage to enemy
                damage += attacker.attack
                victim.health = victim.health - damage
                # Check if enemy died
                if victim.health > 0:
                    print(f"\n{attacker.name}{weapon.move}, dealing {damage} damage to {victim.name}")
                    time.sleep(selfsleep)
                # Allow enemy to attack if it didn't die yet
                if victim.health > 0:
                    damage = max(1, victim.attack - attacker.defence)
                    attacker.health = attacker.health - damage
                    print(f"\n{victim.name} used {victim.move}, dealing {damage} damage to {attacker.name}")
                    time.sleep(selfsleep)

                else:
                    # Check if dead enemy is the final boss
                    if victim.name == "Voldemort":
                        print("\nInsert transition to second phase or alternate enemy")
                        time.sleep(selfsleep)
                        selfroom.enemy = Phase2()
                        attack(attacker, selfroom.enemy)
                        return
                    elif victim.name == "Phase 2":
                        win(weapon)
                        return

                    print(f"\n{attacker.name}{weapon.win_front}{victim.name}{weapon.win_back}")
                    time.sleep(selfsleep)
                    if victim.name == "Sentinels":
                        secret_room()
                        selfroom.enemy = None
                        return
                    print(f"\n{victim.name} dropped a {victim.loot.name}")
                    time.sleep(selfsleep)
                    choice = input(f"\nDo you want to pick {victim.loot.name}? ( yes / no ): ")
                    if choice.lower() == "yes":
                        collect_loot(attacker, victim.loot)
                        time.sleep(selfsleep)
                        print(f"\n{victim.loot.description}")
                        time.sleep(selfsleep)

                    elif choice.lower() == "no":
                        print(f"\nYou left {victim.loot.name} on the ground and allowed the resourceful rat to steal it")
                        time.sleep(selfsleep)
                    else:
                        print(f"\nYour indecisiveness allowed the resourceful rat to steal the {victim.loot.name} when you weren't looking")
                        time.sleep(selfsleep)
                    # Removes the enemy from the room
                    selfroom.enemy = None
                    break
        # Check if the user died
        if attacker.health <= 0:
            selfend_game()

def get_choice(user):
    """sub action from attack() to prompt user for attack methods or use of flask"""
    decision = input(f"What do you want to use? ({user.weapon.name} / Spell / Flask): ")

    # Get a list of spell cost
    cost = []
    for spell in user.spells:
        cost.append(spell.cost)

    valid = False
    while not valid:
        valid = True
        if decision.lower() not in [user.weapon.name.lower(), "spell", "flask"]:
            print(f"\nYou tried to use {decision} but nothing happened")
            time.sleep(selfsleep)
            decision = input(f"\nWhat do you want to use? ({user.weapon.name} / Spell / Flask): ")
            valid = False
        # Check if user has enough mana to cast spells
        elif decision.lower() == "spell" and user.mana < min(cost):
            print("\nYou do not have enough mana to cast spells\n")
            time.sleep(selfsleep)
            decision = input(f"What do you want to use? ({user.weapon.name} / Spell / Flask): ")
            valid = False
        # Check if user has any flask to drink
        elif decision.lower() == "flask" and (user.health_flask + user.mana_flask) == 0:
            print("\nYou ran out of flasks\n")
            time.sleep(selfsleep)
            decision = input(f"What do you want to use? ({user.weapon.name} / Spell / Flask): ")    
            valid = False

    return decision
    
def get_attack(user, decision):
    """sub action from attack() to get total damage done to victim"""

    # Check if user used his weapon
    if decision.lower() == user.weapon.name.lower():
        return user.weapon.attack, user.weapon

    # check if user used spells
    elif decision.lower() == "spell":
        display_spells(user)
        time.sleep(selfsleep)
        spells = []
        for spell in user.spells:
            spells.append(spell.name.lower())
        choice = input("\nWhich spell would you like to cast?: ")
        while choice.lower() not in spells:
            print(f"\nYou tried to cast {choice} but it blew up in your face")
            time.sleep(selfsleep)
            choice = input("\nWhich spell would you like to cast?: ")
        choice = choice.lower()
        cost = user.spells[spells.index(choice)].cost
        print(f"\nYou used up {cost} mana points")
        time.sleep(selfsleep)
        user.mana = user.mana - cost
        return user.spells[spells.index(choice)].attack, user.spells[spells.index(choice)]

def use_flask_battle(user):
    """sub action from get_choice() to prompt user for the flask to drink"""
    display_flask(user)
    selection = input("Which flask would you like to drink?: ")
    valid = False
    while not valid:
        valid = True
        # Validates user selection
        if selection.lower() not in ["flask of crimson tears", "flask of cerulean tears"]:
            print(f"\nYou tried drinking {selection} but nothing happened\n")
            time.sleep(selfsleep)
            selection = input("Which flask would you like to drink?: ")
            valid = False
        # Checks if the user has enough flask of crimson tears
        elif selection.lower() == "flask of crimson tears" and user.health_flask == 0:
            print("\nYou ran out of Flask of Crimson Tears\n")
            time.sleep(selfsleep)
            selection = input("Which flask would you like to drink?: ")
            valid = False
        # Checks if the user has enough flask of cerulean tears
        elif selection.lower() == "flask of cerulean tears" and user.mana_flask == 0:
            print("\nYou ran out of Flask of Cerulean Tears\n")
            time.sleep(selfsleep)
            selection = input("Which flask would you like to drink?: ")
            valid = False

    if selection.lower() == "flask of crimson tears":
        # Makes sure the health healed does not exceed the maximum health
        final_health = min(user.max_health, user.health + FlaskOfCrimsonTears().health)
        healing = final_health - user.health
        print(f"\nYou drank a Flask of Crimson Tears and gained {healing} health")
        time.sleep(selfsleep)
        user.health = final_health
        user.health_flask -= 1
        
    elif selection.lower() == "flask of cerulean tears":
        # Makes sure the mana gained does not exceed the maximum mana
        final_mana = min(user.max_mana, user.mana + FlaskOfCeruleanTears().mana)
        healing = final_mana - user.mana
        print(f"\nYou drank a Flask of Cerulean Tears and gained {healing} mana")
        time.sleep(selfsleep)
        user.mana = final_mana
        user.mana_flask -= 1
                
def use_flask(user):
    """Function to allow the user to use flask but also allows them to cancel the action"""
    display_flask(user)
    selection = input("Which flask would you like to drink? (type cancel to quit): ")
    valid = False
    while not valid:
        valid = True
        # Validates user selection
        if selection.lower() not in ["flask of crimson tears", "flask of cerulean tears", "cancel"]:
            print(f"\nYou tried drinking {selection} but nothing happened\n")
            time.sleep(selfsleep)
            selection = input("Which flask would you like to drink?: ")
            valid = False
        # Checks if the user has enough flask of crimson tears
        elif selection.lower() == "flask of crimson tears" and user.health_flask == 0:
            print("\nYou ran out of Flask of Crimson Tears\n")
            time.sleep(selfsleep)
            selection = input("Which flask would you like to drink?: ")
            valid = False
        # Checks if the user has enough flask of cerulean tears
        elif selection.lower() == "flask of cerulean tears" and user.mana_flask == 0:
            print("\nYou ran out of Flask of Cerulean Tears\n")
            time.sleep(selfsleep)
            selection = input("Which flask would you like to drink?: ")
            valid = False

        elif selection.lower() == "cancel":
            return

    if selection.lower() == "flask of crimson tears":
        # Makes sure the health healed does not exceed the maximum health
        final_health = min(user.max_health, user.health + FlaskOfCrimsonTears().health)
        healing = final_health - user.health
        print(f"\nYou drank a Flask of Crimson Tears and gained {healing} health")
        time.sleep(selfsleep)
        user.health = final_health
        user.health_flask -= 1
        
    elif selection.lower() == "flask of cerulean tears":
        # Makes sure the mana gained does not exceed the maximum mana
        final_mana = min(user.max_mana, user.mana + FlaskOfCeruleanTears().mana)
        healing = final_mana - user.mana
        print(f"\nYou drank a Flask of Cerulean Tears and gained {healing} mana")
        time.sleep(selfsleep)
        user.mana = final_mana
        user.mana_flask -= 1
    
def display_flask(user):
    """sub action from use_flask to display flask in inventory"""
    print(f"\nNumber of Flask of Crimson Tears in inventory : {user.health_flask} (restores {FlaskOfCrimsonTears().health} health)")
    print(f"Number of Flask of Cerulean Tears in inventory: {user.mana_flask} (restores {FlaskOfCeruleanTears().mana} mana)\n")
    time.sleep(selfsleep)
        
def equip(self):
    """main action for user to equip various items"""

    display_equipment(user)

    decision = input("\ndo you want to change your equipment? ( yes / no ): ")

    while decision.lower() not in ["yes", "no"]:
        print("You briefly ponder the heavily nuanced and deeply intricate question of a choice between yes and no.")
        time.sleep(selfsleep)
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
                equip_armour(user)

            elif choice.lower() == "weapon":
                equip_weapon(user)

            elif choice.lower() == "accessory":
                equip_accessory(user)
    
def display_equipment(user):
    """sub action for equip() to display equipments that the user have"""
    
    if user.armour == None:
        print("\nArmour : Empty")
    else:
        print(f"\nArmour : {user.armour.name}")

    if user.weapon == None:
        print("Weapon : Empty")
    else:
        print(f"Weapon : {user.weapon.name}")

    if user.accessory == None:
        print("Accessory : Empty")
    else:
        print(f"Accessory : {user.accessory.name}")
    time.sleep(selfsleep)

def display_spells(user):
    """sub action from attack to display spells that the user have"""
    # Displays all spells owned
    print("\nSpells:")
    for i, spell in enumerate(user.spells):
        print(f"- {spell.name} ({spell.cost} mana)")

def equip_armour(user):
    """sub action from equip() for user to choose an armour to equip"""
    if len(user.armours) == 0:
        print("\nYou do not have any armour to equip")
        time.sleep(selfsleep)
    else:
        # Displays the armours the user owns
        print("\nIn your inventory you have: ")
        armours = user.get_armours()
        for armour in armours:
            print(f"- {armour.name}")
        time.sleep(selfsleep)
        option = input("\nWhich armour do you want to equip?: ")
        # Validates the users choice
        if option.lower() not in armours:
            print(f"\nYou tried equipping {option} but realised you cant create things out of thin air")
            time.sleep(selfsleep)
        else:
            print(f"\nYou equipped {option}")
            time.sleep(selfsleep)
            # Removes the defence increase of the previous armour
            if user.armour != None:
                user.defence = user.defence - user.armour.defence
            armour = user.armours[items.index(option.lower())]
            # Adds the defence of the new armour
            user.defence = user.defence + armour.defence
            user.armour = armour
            display_equipment(user)

def equip_weapon(user):
    """sub action from equip() for user to choose a weapon to equip"""
    if len(user.weapons) == 0:
        print("\nYou do not have any weapon to equip")
        time.sleep(selfsleep)
    else:
        # Displays the weapons the user owns
        print("\nIn your inventory you have: ")
        weapons = user.get_weapons()
        for weapon in weapons:
            print(f"- {weapon.name}")
        time.sleep(selfsleep)
        # Validates the user's choice
        option = input("\nWhich weapon do you want to equip?: ")
        if option.lower() not in weapons:
            print(f"\nYou tried equipping {option} but realised you cant create things out of thin air")
        else:
            print(f"\nYou equipped {option}")
            time.sleep(selfsleep)
            user.weapon = user.weapons[items.index(option.lower())]
            display_equipment(user)

def equip_accessory(user):
    """sub action from equip() for user to choose an accessory to equip"""
    if len(user.accessories) == 0:
        print("\nYou do not have any accessories to equip")
        time.sleep(selfsleep)
    else:
        print("\nIn your inventory you have: ")
        accessories = user.get_accessories()
        for accessory in accessories:
            print(f"- {accessory.name}")
        time.sleep(selfsleep)
        option = input("\nWhich accessory do you want to equip?: ")
        if option.lower() not in accessories:
            print(f"\nYou tried equipping {option} but realised you cant create things out of thin air")
        else:
            print(f"\nYou equipped {option}")
            time.sleep(selfsleep)

            # Removes the stat boost from the previous accessory
            if user.accessory != None:
                user.max_health = user.max_health - user.accessory.health_boost

                new_health = min(max(1, user.health - user.accessory.health_boost), user.max_health)
                user.health = new_health
                
                user.max_mana -= user.accessory.mana_boost

                new_mana = min(max(0, user.mana - user.accessory.mana_boost), user.max_mana)
                user.mana = new_mana

                user.attack -= user.accessory.attack_boost

                user.defence -= user.accessory.defence_boost

            # Adds the stat boost from the new accessory
            accessory = user.accessories[items.index(option.lower())]
            user.health += accessory.health_boost
            user.max_health += accessory.health_boost
            user.attack += accessory.attack_boost
            user.mana += accessory.mana_boost
            user.max_mana += accessory.mana_boost
            user.defence += user.accessory.defence_boost
            
            user.accessory = accessory
            display_equipment(user)

def status(user):
    """main action that prints user's status"""
    # Displays the users statistics
    print(f"\nName: {user.name}")
    print(f"Health: {user.health} / {user.max_health}")
    print(f"Mana: {user.mana} / {user.max_mana}")
    print(f"Defence: {user.defence}")
    print(f"Strength: {user.attack}")
    time.sleep(selfsleep)

def info(user):
    """main action that prompts user for the type of item to find out more information about"""
    choice = input("\nWhat do you want to find out more about? (weapons, spells, armours, accessories, flasks, items): ")
    
    if choice.lower() not in ["weapons", "spells", "armours", "accessories", "flasks", "items"]:
        print(f"\nYou do not own any {choice}")

    elif choice == "weapons":
        weapon_info(user)

    elif choice == "spells":
        spell_info(user)

    elif choice == "armours":
        armour_info(user)

    elif choice == "accessories":
        accessory_info(user)

    elif choice == "flasks":
        flask_info()

    elif choice == "items":
        item_info(user)
                
def weapon_info(user):
    """sub action from equip() that prompts user for specific weapon to find out more about"""
    # Check if the user owns any weapons
    if len(user.weapons) == 0:
        print("\nYou do not own any weapons yet")

    else:
        # Displays the weapons the user owns
        weapons = user.get_weapons()
        print("\nIn your inventory you have: ")
        for weapon in weapons:
            print(f"- {weapon.name}")
        time.sleep(selfsleep)

        decision = input("\nWhich weapon do you want to find out more about? : ")
        if decision.lower() not in weapons:
            print(f"You do not own {decision}")

        else:
            # Displays the description of the weapon
            print("\n", end="")
            print(user.weapons[weapons.index(decision)].description)
            time.sleep(selfsleep)

def spell_info(user):
    """sub action from equip() that prompts user for specific spell to find out more about"""
    # Check if the user knows any spells
    if len(user.spells) == 0:
        print("\nYou do not own any spells yet")

    else:
        # Displays the spells the user knows
        spells = user.get_spells()
        print("\nIn your inventory you have: ")
        for spell in spells:
            print(f"- {spell.name}")
        time.sleep(selfsleep)

        decision = input("\nWhich spell do you want to find out more about? : ")
        if decision.lower() not in spells:
            print(f"You do not own {decision}")

        else:
            # Displays the description of the spell
            print("\n", end="")
            print(user.spells[spells.index(decision)].description)
            time.sleep(selfsleep)

def armour_info(user):
    """sub action from equip() that prompts user for specific armour to find out more about"""
    # Check if the user owns any armours
    if len(user.armours) == 0:
        print("\nYou do not own any amours yet")

    else:
        # Displays the armours the user owns
        armours = user.get_armours()
        print("\nIn your inventory you have: ")
        for armour in armours:
            print(f"- {armour.name}")
        time.sleep(selfsleep)

        decision = input("\nWhich armour do you want to find out more about? : ")
        if decision.lower() not in armours:
            print(f"You do not own {decision}")

        else:
            # Displays the description of the armour
            print("\n", end="")
            print(user.armours[armours.index(decision)].description)
            time.sleep(selfsleep)

def accessory_info(user):
    """sub action from equip() that prompts user for specific accessory to find out more about"""
    # Checks if the user owns any accessories
    if len(user.accessories) == 0:
        print("\nYou do not own any accessories yet")

    else:
        # Displays the accessories the user owns
        accessories = user.get_accessories()
        print("\nIn your inventory you have: ")
        for accessory in accessories:
            print(f"- {accessory.name}")
        time.sleep(selfsleep)

        decision = input("\nWhich accesssory do you want to find out more about? : ")
        if decision.lower() not in accessories:
            print(f"You do not own {decision}")

        else:
            # Displays the description of the accessory
            print("\n", end="")
            print(user.accessories[accessories.index(decision)].description)
            time.sleep(selfsleep)

def flask_info():
    """sub action from equip() that prompts user for specific flask to find out more about"""
    print("\nIn your inventory you have: ")
    print("- Flask of Crimson Tears")
    print("- Flask of Cerulean Tears")

    decision = input("\nWhich accesssory do you want to find out more about? : ")
    if decision.lower() == "flask of crimson tears":
        print("\n", end ="")
        print(FlaskOfCrimsonTears().description)
        time.sleep(selfsleep)
    elif decision.lower() == "flask of cerulean tears":
        print("\n", end ="")
        print(FlaskOfCeruleanTears().description)
        time.sleep(selfsleep)
    else:
        print(f"You do not own {decision}")

def item_info(user):
    """sub action from equip() that prompts user for specific special item to find out more about"""
    # Check if the user owns any items
    if len(user.items) == 0:
        print("\nYou do not own any items yet")
    else:
        # Displays the items the user owns
        items = user.get_items()
        print("\nIn your inventory you have: ")
        for item in items:
            print(f"- {item}")
        time.sleep(selfsleep)

        decision = input("\nWhich item do you want to find out more about? : ")
        if decision.lower() not in items:
            print(f"You do not own {decision}")

        else:
            # Displays the description of the items
            print()
            print(user.items[items.index(decision)].description)
            time.sleep(selfsleep)
                
def display_room_name():
    """prints the room's name in a cool way"""
    print()
    print("="*25)
    space = " "*int((25-len(selfroom.name))/2)
    print(f"{space}{selfroom.name}{space}")
    print("="*25)
    time.sleep(selfsleep)

def display_room_description():
    """prints the room's description"""
    print()
    print(selfroom.description)
    time.sleep(selfsleep)
    look(selfroom)
    selfroom.been_here = True

def get_action():
    """sub action for run() that prompts user for a main action"""
    decision = input("\nWhat do you wish to do? (type help for list of actions): ")

    # Validate the users decision
    while decision.lower() not in selfactions:
        print(f"\nYou do not have the physical and mental capability to {decision}")
        time.sleep(selfsleep)
        decision = input("\nWhat do you wish to do? (type help for list of actions): ")

    return decision

def collect_loot(attacker, loot):
    """sub method from attack() to collect loot of defeated monster"""
    if loot.type == "weapon":
        attacker.weapons.append(loot)
        print(f"\nYou obtained a {loot.name}, a powerful weapon")
        
    elif loot.type == "spell":
        attacker.spells.append(loot)
        print(f"\nYou obtained a {loot.name}, a powerful spell")

    elif loot.type == "armour":
        attacker.armours.append(loot)
        print(f"\nYou obtained a {loot.name}, a powerful armour")

    elif loot.type == "accessory":
        attacker.accessories.append(loot)
        print(f"\nYou obtained a {loot.name}, a powerful accessory")

    elif loot.type == "upgrade":
        attacker.upgrades.append(loot)
        print(f"\nYou obtained a {loot.name}, a powerful upgrade")
        if loot.name == "Portal Gun":
            selfteleportable = True
            selfactions.append("teleport")
            selfdescription.append("Teleport to any room you have been to before")

    time.sleep(selfsleep)

def end_game():
    """displays scenario when user dies"""
    print("__   _______ _   _  ______ _____ ___________")
    time.sleep(0.2)
    print("\ \ / /  _  | | | | |  _  \_   _|  ___|  _  \\")
    time.sleep(0.2)
    print(" \ V /| | | | | | | | | | | | | | |__ | | | |")
    time.sleep(0.2)
    print("  \ / | | | | | | | | | | | | | |  __|| | | |")
    time.sleep(0.2)
    print("  | | \ \_/ / |_| | | |/ / _| |_| |___| |/ /")
    time.sleep(0.2)
    print("  \_/  \___/ \___/  |___/  \___/\____/|___/ ")
    selfend = True

def win(weapon):
    """displays scenario when user wins"""
    print(f"\nUsing the almighty {weapon.name}, you struck insert final boss down, crippling him of all his powers and stopping his evil tyranny over the school")
    time.sleep(selfsleep)
    print(" _____ ___________   _____ _       ___  _____ _   _ ")
    time.sleep(0.2)
    print("|  __ \  _  |  _  \ /  ___| |     / _ \|_   _| \ | |")
    time.sleep(0.2)
    print("| |  \/ | | | | | | \ `--.| |    / /_\ \ | | |  \| |")
    time.sleep(0.2)
    print("| | __| | | | | | |  `--. \ |    |  _  | | | | . ` |")
    time.sleep(0.2)
    print("| |_\ \ \_/ / |/ /  /\__/ / |____| | | |_| |_| |\  |")
    time.sleep(0.2)
    print(" \____/\___/|___/   \____/\_____/\_| |_/\___/\_| \_/")
    selfend = True

def die():
    """to end the game"""
    selfend_game()
    selfend = True
       
def secret():
    """secret account that gives God like stats by setting name as meow"""
    print("\nWelcome chosen one, the Gods smile upon you and have rained down their blessing")
    time.sleep(selfsleep)
    selfcharacter.health = 999
    selfcharacter.max_health = 999
    selfcharacter.mana = 999
    selfcharacter.max_mana = 999
    selfcharacter.attack = 999
    selfcharacter.defence = 999
    selfcharacter.health_flask = 999
    selfcharacter.mana_flask = 999
    selfmap.full_reveal()
    selfcharacter.items.append(DectusMedallionLeft())
    selfcharacter.items.append(DectusMedallionRight())

def meow():
    if selfroom.secret == True:
        print("""       
            
   ____ ___  ___  ____ _      __
  / __ `__ \/ _ \/ __ \ | /| / /
 / / / / / /  __/ /_/ / |/ |/ / 
/_/ /_/ /_/\___/\____/|__/|__/  
                               """)
        time.sleep(selfsleep)
        print("\nYou started communicating with the cat, leading you to discover a hidden passage\n")
        time.sleep(selfsleep)
        theLastResort = TheLastResort()
        selfroom.left = theLastResort
        theLastResort.right = selfroom
    else:
        choice = random.randint(1, 9)
        if choice == 1:
            print("""  
            
  __  __  U _____ u U  ___ u             
U|' \/ '|u\| ___"|/  \/"_ \/__        __ 
\| |\/| |/ |  _|"    | | | |\"\      /"/ 
 | |  | |  | |___.-,_| |_| |/\ \ /\ / /\ 
 |_|  |_|  |_____|\_)-\___/U  \ V  V /  U
<<,-,,-.   <<   >>     \\  .-,_\ /\ /_,-.
 (./  \.) (__) (__)   (__)  \_)-'  '-(_/ 
                                        """)
        elif choice == 2:
            print("""       
            
   ____ ___  ___  ____ _      __
  / __ `__ \/ _ \/ __ \ | /| / /
 / / / / / /  __/ /_/ / |/ |/ / 
/_/ /_/ /_/\___/\____/|__/|__/  
                               """)

        elif choice == 3:
            print("""                              
                              
 _ __ ___   ___  _____      __
| '_ ` _ \ / _ \/ _ \ \ /\ / /
| | | | | |  __/ (_) \ V  V / 
|_| |_| |_|\___|\___/ \_/\_/  
                              """)

        elif choice == 4:
            print(""" 
            
 _  _  ____  __   _  _ 
( \/ )(  __)/  \ / )( \
/ \/ \ ) _)(  O )\ /\ /
\_)(_/(____)\__/ (_/\_)
                        """)

        elif choice == 5:
            print("""   
            
 _ __ ___   ___  _____      __
| '_ ` _ \ / _ \/ _ \ \ /\ / /
| | | | | |  __/ (_) \ V  V / 
|_| |_| |_|\___|\___/ \_/\_/  
                              """)

        elif choice == 6:
            print("""                                    
                                    
,--,--,--. ,---.  ,---. ,--.   ,--. 
|        || .-. :| .-. ||  |.'.|  | 
|  |  |  |\   --.' '-' '|   .'.   | 
`--`--`--' `----' `---' '--'   '--' 
                                    """)

        elif choice == 7:
            print(""" 
 __    __     ______     ______     __     __    
/\ "-./  \   /\  ___\   /\  __ \   /\ \  _ \ \   
\ \ \-./\ \  \ \  __\   \ \ \/\ \  \ \ \/ ".\ \  
 \ \_\ \ \_\  \ \_____\  \ \_____\  \ \__/".~\_\ 
  \/_/  \/_/   \/_____/   \/_____/   \/_/   \/_/ 
                                                 """)

        elif choice == 8:
            print("""                                        
                                        
 _ .--..--.  .---.   .--.   _   _   __  
[ `.-. .-. |/ /__\\/ .'`\ \[ \ [ \ [  ] 
 | | | | | || \__.,| \__. | \ \/\ \/ /  
[___||__||__]'.__.' '.__.'   \__/\__/   
                                        """)

        elif choice == 9:
            print(""" 
 _      _____ ____  _     
/ \__/|/  __//  _ \/ \  /|
| |\/|||  \  | / \|| |  ||
| |  |||  /_ | \_/|| |/\||
\_/  \|\____\\____/\_/  \|
                          """)
      
def settings():
    """Show and change settings"""
    settings = []
    with open("settings.txt", "r") as f:
        settings = f.readlines()
        settings_dict = {}
        for row in settings:
            key, val = row.split()
            settings_dict[key] = val

    display_settings(settings_dict)
    
    change = input("\nDo you want to change your settings? ( yes / no ): ").lower()

    while change not in ["yes", "no"]:
        print("You briefly ponder the heavily nuanced and deeply intricate question of a choice between yes and no.")
        time.sleep(selfsleep)
        change = input("\nDo you want to change your settings? ( yes / no ): ").lower()
    
    if change == "yes":
    
        choice = ""
        accepted = list(settings_dict.keys())
        accepted.append("finish")
        while choice != "finish":
            choice = input("\nWhich setting do you want to change? (type finish to quit): ").lower()
            while choice not in accepted:
                print(f"{choice} is a uniquely unmodifiable property of this realm.")
                choice = input("\nWhich setting do you want to change? (type finish to quit): ").lower()

            if choice == "finish":
                with open("settings.txt", "w") as f:
                    for entry in settings_dict:
                        f.write(entry + " " + settings_dict[entry] + "\n")
                return
            
            if choice == "sleep":
                new = set_sleep(settings_dict["sleep"])
                settings_dict["sleep"] = new

            display_settings(settings_dict)
            
    elif change == "no":
        return

def display_settings(settings):
    """
    display the settings passed in
    """
    print("\nCurrent Settings:\n")
    for set in settings:
        print(f"{set}: {settings[set]}")

def set_sleep(current):
    """
    Change the interval between messages
    returns new value for sleep as string
    """
    count = 0
    print("\nsleep: the interval between messages sent by the game in seconds.")
    print(f"Current value: {current}")
    
    accept = [str(x) for x in range(6)]
    accept.append("cancel")

    new = input("\nEnter a new value for sleep (0-5 seconds), or cancel to cancel: ")
    while new not in accept:
        print("You count up to five on your fingers. Slowly.")
        time.sleep(selfsleep)
        new = input("\nEnter a new value for sleep (0-5 seconds), or cancel to cancel: ")
    
    if new.lower() == "cancel":
        return current
    else:
        selfsleep = int(new)
        return new
            

def secret_room():
    print("\nAfter you successfully defeated the sentinels, a stray ginger tabby cat emerges from behind a wall and stares at you playfully\n")
    selfroom.secret = True
    time.sleep(selfsleep)

def teleport():
    print("\nYou can teleport to: ")
    rooms = []
    for room in selfrooms:
        print(f"- {room.name}")
        rooms.append(room.name.lower())
    time.sleep(selfsleep)

    choice = input("\nWhich room do you want to teleport to?: ")
    
    if choice.lower() not in rooms:
        print(f"\nYou tried teleporting to {choice} but ended up in a dark abyss\n")
        time.sleep(selfsleep)

    else:
        selfroom = selfrooms[rooms.index(choice.lower())]
            

intro()
while selfend == False:
    run()
#root.after(1, intro)
#root.mainloop()
