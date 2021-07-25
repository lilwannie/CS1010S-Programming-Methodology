#
# CS1010S --- Programming Methodology
#
# Mission 14 Template
#
# Note that written answers are commented out to allow us to run your
# code easily while grading your problem set.

from hungry_games_classes import *
from engine import *
import simulation
import random



# Rename XX_AI to YourName_AI
class anson_AI(Tribute):
    def next_action(self):
        # Next action should return a tuple of what your next action should
        # be. For the full list of tuple that your AI can return, refer to
        # the pdf file

        # As an example: the following code will make your AI just walk around 
        # randomly every turn. You do NOT have to use this code if you don't 
        # want to!
        things_around = self.objects_around()
        inventory = self.get_inventory()
        hunger = self.get_hunger()
        health = self.get_health()
        exits = self.get_exits()
        weapons = tuple(filter(lambda x: isinstance(x, Weapon), inventory))
        ranged_weapons = tuple(filter(lambda x: isinstance(x, RangedWeapon), inventory))
        ammo_types = tuple(filter(lambda x: isinstance(x, Ammo), inventory))
        
        
        for thing in things_around:
            if isinstance(thing,Thing):
                return ("TAKE", thing)
        while hunger >= 75:
            for food in self.get_food():
                return ("EAT", food)
        for thing in things_around:
            if isinstance(thing, Tribute):
                if ranged_weapons:
                    for individual_ranged_weapon in ranged_weapons:
                        if individual_ranged_weapon.shots_left() == 0:
                            return ("LOAD", individual_ranged_weapon, tuple(filter(lambda x: x == x.weapon_type(), ammo_types)[0]))
                        else:
                            return ("ATTACK", thing, individual_ranged_weapon)

                else:
                    for weapon in weapons:
                        return ("ATTACK", thing, weapon)
                    
                    
                
                

            elif isinstance(thing,LivingThing):
                for weapon in weapons:
                        return ("ATTACK", thing, weapon)
            
                
                
##                You can filter the weapons/ammo from self.objects_around() using isinstance(x,Weapon)
##                or isinstance(x,Ammo).
##                If the resulting filter is empty,
##                it means you have no more weapon/ammo to take.
##                Otherwise, you can just return ("TAKE", )

        if exits:
            index = random.randint(0, len(exits)-1)
            direction = exits[index]
            return ("GO", direction)
        else: # Otherwise, do nothing
            pass

        

        
        
        

       
        

# NOTE: DO NOT remove the 2 lines of code below.
#
# In particular, you will need to modify the `your_AI = XX_AI` line so that
# `XX_AI` is the name of your AI class.
# For instance, if your AI class is called `MyPrecious_AI`, then you have to
# modify that line to:
#
#     your_AI = MyPrecious_AI
#
# Failure to do so will result in the following exception on Coursemology when
# you run the test cases:
#
#     Traceback (most recent call last):
#       in <module>
#     NameError: name 'your_AI' is not defined
#
# You have been warned!
time_limit = 50 # Modify if your AI needs more than 50 moves for task 2
your_AI = anson_AI # Modify if you changed the name of the AI class



##################
# Simulation Code
##################
##########
# Task 1 #
##########
# Goal:
# 1. Your AI should be able to pick up a Weapon / RangedWeapon
# 2. Your AI should be able to kill chicken
# 3. Your AI should be able to pick up chicken_meat after killing chicken

# Replace XX_AI with the class name of your AI
# Replace gui=True with gui=False if you do not wish to see the GUI
simulation.task1(anson_AI("XX AI", 100), gui=True)


##########
# Task 2 #
##########
## 1. Your AI should be able to pick up a Weapon / RangedWeapon
## 2. Your AI should be able to move around and explore
## 3. Your AI should be able to find harmless Tribute and kill him

# Replace XX_AI with the class name of your AI
# Replace gui=True with gui=False if you do not wish to see the GUI

time_limit = 20    # You may change the time limit if your AI is taking too long
simulation.task2(XX_AI("XX AI", 100), time_limit, gui=True)



#################
# Optional Task
#################
## You can create your own map and see how your AI behaves!

# Define the parameters of the map
def config():
    ## The game should have a 3x3 map
    game_map = GameMap(3)

    ## You can change the numbers to create different kinds of maps for
    ## the optional task.
    game_config = GameConfig()
    game_config.set_item_count(Weapon, 3)
    game_config.set_item_count(Animal, 10)
    game_config.set_item_count(RangedWeapon, 5)
    game_config.set_item_count(Food, 5)
    game_config.set_item_count(Medicine, 5)

    game = GameEngine(game_map, game_config)

    # Add some dummy tributes
    ryan = Tribute("Ryan", 100)
    waihon = Tribute("Wai Hon", 100)
    soedar = Tribute("Soedar", 100)

    game.add_tribute(ryan)
    game.add_tribute(waihon)
    game.add_tribute(soedar)

    # Yes, your AI can fight with himself
    #ai_clone = XX_AI("AI Clone", 100)
    #game.add_tribute(ai_clone)

    return game

# Replace XX_AI with the class name of your AI
# Replace gui=True with gui=False if you do not wish to see the GUI
#simulation.optional_task(XX_AI("XX AI", 100), config, gui=False)
