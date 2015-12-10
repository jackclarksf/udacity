__author__ = 'iamja_000'

print("Testing")

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
        water_level = input("Please specify how wet you'd like it, on a scale of one to three: ")
        sizes = [0, 1, 2, 3]
        while int(water_level) not in sizes:
            print("Your selection of {} is invalid as is not in {} ".format(water_level, sizes))
            water_level = input("Try again (1 to 3), please: ")
        else:
            water_math = (len(self.base_map[0])*len(self.base_map[0]))
            print("Our water math is {} divided by water_level input of {}".format(water_math, water_level))
            squares_to_fill = int(water_math) / int(water_level)
            print("We need to fill {} squares".format(squares_to_fill))
            #PROBABLY NEED TO SORT OUT THE FLOAT THING HERE
            #INITIALIZE THE SCREEN_DRAW FUNCTION HERE
            self.draw_new_entities("W", squares_to_fill)

    def draw_new_entities(self, entity_to_draw, entity_count):
        i = 0
        while i < entity_count:
            for i in self.base_map:
                self.base_map[i][i].replace("$", entity_to_draw)
                i += 1
                #NEED TO FIX THIS LIST NAVIGATION, PROBABLY


    def display_map(self):
        for i in self.base_map:
            print(i)

    def map_to_string(self):
        string_to_print = ""
        i = 0
        dog = (len(self.base_map))
        while i < (dog-1):
            #print(i)
            #print(self.base_map[i])
            i += 1
            linked = ', '.join(self.base_map[i])
            linked_clean = linked.replace(",", " ")
            string_to_print += linked_clean
            string_to_print += "\n"
        print(string_to_print)



pirate_game = Map_Procedural()
pirate_game.display_map()
pirate_game.map_to_string()