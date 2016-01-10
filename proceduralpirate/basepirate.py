__author__ = 'iamja_000'

print("Testing")
import random
from random import randrange

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
        self.treasure_placement("$")
        self.clumping("W")

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
        self.base_map = self.draw_map_entities("W", final_number)

    #SCAN LINES IN MAP - DONE
    #GET POSITIONS OF CLUMP_ITEM - DONE
    #WORK OUT HOW TO CLUMP TOGETHER
    def clumping(self, clump_item):
        print("Starting clumping")
        total_location_list = []
        test_line = 0
        while test_line < size:
            line_location_list = []
            for i, j in enumerate(self.base_map[test_line]):
                if j == clump_item:
                    #print(i)
                    line_location_list.append(i)
            test_line += 1
            total_location_list.append(line_location_list)
        print("Our final loc list is... {}".format(total_location_list))
        longest = max(total_location_list, key=len)
        print("Our longest list is {}".format(longest))
        longest_pos = total_location_list.index(longest)
        print("Location of longest list is: {}".format(longest_pos))
        next_list = total_location_list[longest_pos-1]
        print("Location of adjacent list is: {}".format(next_list))
        #NEXT STEPS = FIND LINE WITH LARGEST NUMBERS. MAKE THIS DOMINANT. CLUMP OTHERS TO BE NEAR IT.
        #STEP UP AND DOWN THROUGH LINES, EXPANDING ^ AND THEN ONWE DOWN, TILL DONE

    def list_fiddler(self, list_to_check_against, list_to_change):
        print(list_to_check_against)
        print(list_to_change)


    def treasure_placement(self, land_to_place_on):
        joined_map = sum(self.base_map, [])
        spot_to_draw = self.spot_selection(joined_map, land_to_place_on)
        print("Placing X at {}".format(spot_to_draw))
        joined_map[spot_to_draw] = "X"
        joined_map_treasure = self.list_joiner(joined_map, size)
        print("Created joined map")
        self.base_map = joined_map_treasure

    def draw_map_entities(self, entity_to_draw, number_to_draw):
        joined_map = sum(self.base_map, [])
        drawn_entities = 1
        while drawn_entities <= number_to_draw:
            #print("Drawing entity {} out of {}".format(drawn_entities, number_to_draw))
            spot_to_draw = self.spot_selection(joined_map, "$")
            joined_map[spot_to_draw] = "W"
            drawn_entities += 1
        joined_map2 = self.list_joiner(joined_map, size)
        return joined_map2

    def spot_selection(self, checkable, check_mark):
        random_spot = randrange(0, len(checkable))
        #print("Our random spot is {} and at this point there is {}".format(random_spot, checkable[random_spot]))
        while checkable[random_spot] != check_mark:
            #print("Error, try again")
            random_spot = randrange(0, len(checkable))
            #print("Our random spot is NOW {} and at this point there is {}".format(random_spot, checkable[random_spot]))
        return random_spot

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

    def string_count(self):
        count = 0
        joined_map = sum(self.base_map, [])
        for i in joined_map:
            if i == "W":
                count +=1
        print("Count of W is: {}".format(count))




pirate_game = Map_Procedural()
print("Displaying map")
pirate_game.display_map()
print("Starting drawing")
print(pirate_game.map_to_string())
pirate_game.string_count()