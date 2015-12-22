__author__ = 'iamja_000'

print("Testing")
import random

#Challenge Brief: Design a program that uses procedural techniques to create a pirate map. The pirate map is an image of any dimensions that should look similar to the following examples, or at least contain similar content.
#
#Mandatory Items
#- At least one distinguishable landmass on the map.
#- An X, to mark the treasure.
#Points
#Feature	Points Awarded
#Terrain features (forests, hills, mountains)	1
#Seed based generation (different seed, different map)	1
#Believable landmasses (as in, look like islands)	1
#Decorations (Ships, giant squid, waves)	1
#A marked path to follow to the X	1
#Rivers	1

size = int(input("Please specify the size of the map (x by x): "))
print("Your size is: {} ".format(size))

class Map_Procedural:
    def __init__(self):
        self.base_map = [["$" for i in range(size)] for i in range(size)]
        self.base_terrain = []
        self.water = []
        #print("OK, your base map is: {}".format(self.base_map))
        self.water_generation()

    def water_generation(self):
        water_level = input("Please specify how wet you'd like it, by percentage: ")
        float_level = float(water_level)
        print("Our level is now {}".format(float_level))
        squares = (len(self.base_map[0])*len(self.base_map[0]))
        print("Percentage {} filling {} squares".format(float_level, squares))
        percent_operate = 100/float_level
        print("Our multiplier is {}".format(percent_operate))
        final_number = squares / percent_operate
        print("Our final number of squares should be {}".format(final_number))
        number_squares = (float(float_level)/float(squares)) / 100.0
            #PROBABLY NEED TO SORT OUT THE FLOAT THING HERE
            #INITIALIZE THE SCREEN_DRAW FUNCTION HERE
        self.base_map = self.draw_new_entities("W", float_level)

#NEW IDEA

#this function takes in an entity to draw, and a percentage count and creates a string with the changed characters
#now need to split string into multiple strings

#NEW FUNCTION IDEA - DEF DRAW NEW ENTITIES
#RANDOMLY FILL A SPOT IN STRING FOR EACH ONE
#MAKE SURE IT'S FILLED AND IF COLLISION THEN GO AGAIN
#RETURN ENDPOINT

 #   def draw_new_entities(self, entity_to_draw, entity_count):
 #       joined_map = sum(self.base_map, [])
 #       j = 0
 #       for i in joined_map:
 #           #print(" i' is {} and j is {}".format(i, j))
 #           if random.randint(0, 100) < entity_count:
 #               #print(joined_map[j])
 #               joined_map[j] = entity_to_draw
 #               #print(joined_map[j])
 #           j += 1
  #      #print(joined_map)
 #       joined_map2 = self.list_joiner(joined_map, size)
 #       #print(joined_map2)
 #       return joined_map2

    def list_joiner(self, arr_name, arr_size):
        arrs = []
        while len(arr_name) > arr_size:
            pice = arr_name[:arr_size]
            arrs.append(pice)
            arr_name = arr_name[arr_size:]
        arrs.append(arr_name)
        return arrs

    def display_map(self):
        for i in self.base_map:
            print(i)

    def map_to_string(self):
        string_to_print = ""
        i = 0
        dog = (len(self.base_map))
        while i < (dog-1):
            i += 1
            linked = ', '.join(self.base_map[i])
            linked_clean = linked.replace(",", " ")
            string_to_print += linked_clean
            string_to_print += "\n"
        return string_to_print



pirate_game = Map_Procedural()
#pirate_game.display_map()
print(pirate_game.map_to_string())