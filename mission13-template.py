#
# CS1010S --- Programming Methodology
#
# Mission 13 Template
#
# Note that written answers should be commented out to allow us to run your
# code easily while grading your problem set.

from hungry_games import *
import random



#################################################################################
#                                                                               #
# PASTE YOUR MISSION 12/13 CODE HERE                                               #
#                                                                               #
#################################################################################


class Weapon(Thing):

    ###########
    # Task 1a #
    ###########

    def __init__(self, name, min_dmg, max_dmg):
        super().__init__(name)
        self.min_dmg = min_dmg
        self.max_dmg = max_dmg
        


    ###########
    # Task 1b #
    ###########

    def min_damage(self):
        # your code here
        return self.min_dmg 

    def max_damage(self):
        # your code here
        return self.max_dmg 

    ###########
    # Task 1c #
    ###########

    def damage(self):
        # your code here
        return random.randint(self.min_damage(), self.max_damage())




############
##  Task2 ##
############

class Ammo(Thing):

    ###########
    # Task 2a #
    ###########
    def __init__(self,name,weapon,quantity):
        super().__init__(name)
        self.weapon = weapon
        self.quantity = quantity 


    ###########
    # Task 2b #
    ###########
    # definition of get_quantity here

    def get_quantity(self):
        return self.quantity 


    ###########
    # Task 2c #
    ###########
    # definition of weapon_type here
    def weapon_type(self):
        return self.weapon.name #getting the name of the object bow 


    ###########
    # Task 2d #
    ###########
    def remove_all(self):
        self.quantity = 0 



############
##  Task3 ##
############

class RangedWeapon(Weapon):

    ###########
    # Task 3a #
    ###########
    def __init__(self,name,min_dmg,max_dmg):
        super().__init__(name,min_dmg,max_dmg)
        self.shots = 0 
        


    ###########
    # Task 3b #
    ###########
    # definition of shots_left here
    def shots_left(self):
        return self.shots 


    ###########
    # Task 3c #
    ###########
    # definition of load here
    def load(self,ammo): #ammo is an object 
        if ammo.weapon_type() == self.name: #if ammo is meant for the weapon based on the name 
            self.shots += ammo.get_quantity()
            ammo.remove_all() # since all ammo goes into the weapon 
            
        


    ###########
    # Task 3d #
    ###########
    def damage(self):
        # your code here
        if self.shots == 0:
            return 0
        else:
            self.shots -= 1
            return super().damage()
        
###########
# Task 4a #
###########
# definition of Food class here

class Food(Thing):
    def __init__(self,name,food_value):
        super().__init__(name)
        self.food_value = food_value

    def get_food_value(self):
        return self.food_value
    


###########
# Task 4b #
###########
# definition of Medicine class here

class Medicine(Food):
    def __init__(self,name,food_value,medicine_value):
        super().__init__(name,food_value)
        self.medicine_value = medicine_value

    def get_medicine_value(self):
        return self.medicine_value 



##############
# Task 5a&b  #
##############
# definition of Animal class here

class Animal(LivingThing):
    def __init__(self,name,health,food_value,*threshold):
        super().__init__(name,health,threshold)
        self.food_value = food_value


    def get_food_value(self):
        return self.food_value

    def get_threshold(self):
        if self.threshold == ():
            return random.randint(0,4)
        else:
            return self.threshold[0]

    def go_to_heaven(self):
       
        food = Food(self.name + ' meat' , self.food_value)
        self.get_place().add_object(food)
        self.get_place().del_object(self)
        HEAVEN.add_object(self)
        GAME_LOGGER.add_event("DEAD", self)
        

######################
# Class: LivingThing #
######################

class LivingThing(MobileObject):
    def __init__(self, name, health, threshold):
        super().__init__(name, None)
        self.health = health
        self.threshold = threshold

    def get_threshold(self):
        return self.threshold

    def get_health(self):
        return self.health

    def add_health(self, health):
        self.health = min(100, self.health+health)

    def reduce_health(self, health):
        self.health = max(0, self.health-health)
        if self.health == 0:
            self.go_to_heaven()

    def go_to_heaven(self):
        self.get_place().del_object(self)
        HEAVEN.add_object(self)
        GAME_LOGGER.add_event("DEAD", self)

    def move_to(self, new_place):
        old_place = self.get_place()

        # we can only move to one of the neighboring place
        if new_place in old_place.get_neighbors():
            GAME_LOGGER.add_event("MOVE", self, old_place, new_place)
            old_place.del_object(self)
            new_place.add_object(self)
        else:
            GAME_LOGGER.warning("{} cannot move from {} to {}".format(self.get_name(), old_place.get_name(), new_place.get_name()))

    def act(self):
        if self.threshold >= 0 and random.randint(0, self.threshold) == 0:
            new_place = self.get_place().random_neighbor()
            if new_place:
                self.move_to(new_place)

'''
#################
# Class: Person #
#################

class Person(LivingThing):
    def __init__(self, name, health, threshold):
        self.inventory = []
        super().__init__(name, health, threshold)

    def take(self, thing):
        # Can only take things in current location and not owned by others
        if isinstance(thing, Thing) and thing in self.place.objects and not thing.is_owned():
            thing.set_owner(self)
            self.inventory.append(thing)
            self.place.del_object(thing)
            GAME_LOGGER.add_event("TOOK", self, thing)
        else:
            GAME_LOGGER.warning("{} cannot take {}.".format(self.get_name(), thing.get_name()))

    def remove_item(self, thing):
        #Can only remove things in inventory
        if isinstance(thing, Thing) and thing in self.get_inventory() and thing.get_owner()==self:
            thing.set_owner(None)
            self.inventory.remove(thing)
        else:
            GAME_LOGGER.warning("{} does not own {}.".format(self.get_name(), thing.get_name()))

    def go(self, direction):
        new_place = self.place.get_neighbor_at(direction.upper())
        if new_place is not None:
            self.move_to(new_place)
        else:
            GAME_LOGGER.warning("{} cannot go {} from {}".format(self.get_name(), direction, self.get_place().get_name()))

    def get_inventory(self):
        return list(self.inventory)

    def objects_around(self):
        return list(filter(lambda t: t is not self, self.get_place().get_objects()))

    def get_exits(self):
        return self.get_place().get_exits()

'''




#################################################################################
#                                                                               #
# MISSION 13                                                                    #
# TESTING CODE IS BELOW ALL THE TASKS                                           #
#                                                                               #
#################################################################################


#############
##  Task 1 ##
#############

class Tribute(Person):


    ############
    #  Task 1a #
    ############
    def __init__(self, name, health):
        # Tributes will not move by themselves, so set threshold to -1
        super().__init__(name, health, -1)
        # add hunger property
        self.hunger = 0 #start the game with full stomach 




    ############
    #  Task 1b #
    ############
    # definition of get_hunger here
    def get_hunger(self):
        return self.hunger 




    ############
    #  Task 1c #
    ############
    # definition of add_hunger here
    def add_hunger(self,hunger):
        if self.get_hunger() < 100:
            self.hunger += hunger
        else: #if hunger level is 100 or more
            return super().go_to_heaven()




    ############
    #  Task 1d #
    ############
    # definition of reduce_hunger here
    def reduce_hunger(self,hunger):
        #ensure that hunger is always >= 0
        if hunger > self.get_hunger():
            self.hunger = 0
        else:
            self.add_hunger(-hunger)
    
        




    #############
    ##  Task 2 ###ONGOING
    #############
    def eat(self,food):
        if food in self.get_inventory():
            self.reduce_hunger(food.get_food_value())
            if isinstance(food,Medicine):
                self.health += food.get_medicine_value()
                if self.health > 100:
                    self.health = 100
            self.remove_item(food)

   

               


    ############
    #  Task 3a #
    ############
    # definition of get_weapons here

    def get_weapons(self):
        return tuple(filter(lambda elem : isinstance(elem,Weapon),self.get_inventory()))




    ############
    #  Task 3b #
    ############
    # definition of get_food here

    def get_food(self):
        return tuple(filter(lambda elem: isinstance(elem,Food),self.get_inventory()))




    ############
    #  Task 3c #
    ############
    # definition of get_medicine here
    def get_medicine(self):
        return tuple(filter(lambda elem: isinstance(elem,Medicine),self.get_inventory()))





    #############
    ##  Task 4 ##
    #############
    # definition of attack here
    def attack(self,living_thing, weapon):
        if (weapon not in self.get_inventory()) or (living_thing.get_place() != self.get_place()):
            pass
        else:
            living_thing.reduce_health(weapon.damage())
            
    




#############
##  Task 5 ##
#############
# You can either draw it here; or draw it on a piece of paper,
# then take a picture and upload it.
# Please ensure that your name appears somewhere in your image.




################
# Testing Code #
################


def test_task1():
    print("===== Task 1b ======")
    cc = Tribute("Chee Chin", 100)
    print(cc.get_hunger())          # 0

    print("===== Task 1c ======")
    Base = Place("base")
    cc = Tribute("Chee Chin", 100)
    Base.add_object(cc)
    print(cc.get_place().get_name())    # base
    cc.add_hunger(50)
    print(cc.get_hunger())              # 50
    cc.add_hunger(50)                   # Chee Chin went to heaven!
    print(cc.get_hunger())              # 100
    print(cc.get_place().get_name())    # Heaven

    print("===== Task 1d ======")
    cc = Tribute("Chee Chin", 100)
    cc.add_hunger(10)
    print(cc.get_hunger())          # 10
    cc.reduce_hunger(20)
    print(cc.get_hunger())          # 0

# Uncomment to test task 1
test_task1()

def test_task2():
    print("===== Task 2 ======")
    cc = Tribute("Chee Chin", 100)
    chicken = Food("chicken", 5)
    aloe_vera = Medicine("aloe vera", 2, 5)

    Base = Place("base")
    Base.add_object(cc)
    Base.add_object(chicken)
    Base.add_object(aloe_vera)

    cc.reduce_health(10)
    cc.add_hunger(4)
    print(named_col(cc.get_inventory()))    # []

    cc.eat(chicken)
    print(cc.get_hunger())                  # 4

    cc.take(chicken)                        # Chee Chin took chicken
    cc.take(aloe_vera)                      # Chee Chin took aloe vera
    print(named_col(cc.get_inventory()))    # ['chicken', 'aloe vera']

    cc.eat(aloe_vera)
    print(cc.get_health())                  # 95
    print(cc.get_hunger())                  # 2

    print(named_col(cc.get_inventory()))    # ['chicken']

    cc.eat(chicken)
    print(cc.get_health())                  # 95
    print(cc.get_hunger())                  # 0
    print(named_col(Base.get_objects()))    # ['Chee Chin']

# Uncomment to test task 2
test_task2()

def test_task3():
    print("===== Task 3 ======")
    cc = Tribute("Chee Chin", 100)
    chicken = Food("chicken", 5)
    aloe_vera = Medicine("aloe vera", 2, 5)
    bow = RangedWeapon("bow", 4, 10)
    sword = Weapon("sword", 2, 5)

    Base = Place("base")
    Base.add_object(cc)
    Base.add_object(chicken)
    Base.add_object(aloe_vera)
    Base.add_object(bow)
    Base.add_object(sword)

    cc.take(bow)                           # Chee Chin took bow
    cc.take(sword)                         # Chee Chin took sword
    cc.take(chicken)                       # Chee Chin took chicken
    cc.take(aloe_vera)                     # Chee Chin took aloe_vera

    print(named_col(cc.get_inventory()))   # ['bow', 'sword', 'chicken', 'aloe vera']
    print(named_col(cc.get_weapons()))     # ('bow', 'sword')
    print(named_col(cc.get_food()))        # ('chicken', 'aloe vera')
    print(named_col(cc.get_medicine()))    # ('aloe vera',)

# Uncomment to test task 3
test_task3()

def test_task4():
    print("===== Task 4 ======")
    Base = Place("base")
    cc = Tribute("Chee Chin", 100)
    sword = Weapon("sword", 10, 10)
    bear = Animal("bear", 20, 10)

    Base.add_object(cc)
    Base.add_object(sword)
    Base.add_object(bear)

    print(bear.get_health())                # 20

    cc.attack(bear, sword)
    print(bear.get_health())                # 20

    cc.take(sword)                          # Chee Chin took sword
    cc.attack(bear, sword)
    print(bear.get_health())                # 10

    cc.attack(bear, sword)                  # bear went to heaven
    print(named_col(Base.get_objects()))    # ['Chee Chin', 'bear meat']

# Uncomment to test task 4
test_task4()
