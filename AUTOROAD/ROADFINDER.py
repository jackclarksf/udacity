__author__ = 'iamja_000'

#CREATE A MAP OF ARBITARY SIZE
#RANDOMLY SCATTER ROAD "OBJECTS" ON THE MAP
#HAVE EACH ROAD SEND OUT A QUEST DEVICE, MOVING AT A RANDOM WALK
#PRINT TO SCREEN
#DETECT COLLISSION BETWEEN ROAD OBJECT AND CITY
#FORM NEW COMPLETE ROAD OBJECT

#OBJECTS:
#CITY
#ROAD FINDER
#ROAD

#IMPLEMENT COLLISIONS FOR THE #

import random
from random import randrange

seed = 1
size = 5

def generateLocation(world):
    x = randrange(0, size)
    y = randrange(0, size)
    while (str(world[y][x]) != " "):
        x = randrange(0, (size-1))
        y = randrange(0, (size-1))
    return x, y

class City:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "C"

    def getLocation(self):
        return self.x, self.y

class Road_Finder:
    #ADD IN A STARTING COORDINATE SO YOU KNOW WHAT TO LINK BACK TO

    starting_coordinates = []

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.starting_coordinate()

    def __str__(self):
        return "x"

    def getLocation(self):
        return self.x, self.y

    def starting_coordinate(self):
        self.starting_coordinates.append(self.x)
        self.starting_coordinates.append(self.y)

class Temp_Path:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "#"

    def getLocation(self):
        return self.x, self.y

class Game:
    def __init__(self):
        self.tick = 0
        self.road_seeker = []
        self.cities = []
        self.turns = []
        self.paths = []
        self.map = [[" " for i in range(size)] for i in range(size)]

        def city_generation(seed):
            for i in range(seed):
                self.calculate_display()
                x, y = generateLocation(self.map)
                self.cities.append(City(x, y))
                print("City {} is located at {} {}".format(self.cities[i], x, y))

        city_generation(seed)

        def roadGeneration():
            for i in self.cities:
                x, y = i.getLocation()
                moves = self.valid_moves(x, y)
                choice = self.random_move(moves)
                x, y = self.move_entity(choice, x, y)
                self.road_seeker.append(Road_Finder(x, y))

        roadGeneration()

    def city_check(self):
        for i in self.road_seeker:
            x, y = i.getLocation()
            for c in self.cities:
                a, b = c.getLocation()
                print("Road scout = {}, {} and city location is {} {}".format(x, y, a, b))
                #doesn't work below here, check
                e = x, y
                f = a, b
                #if self.map[y][x] == self.map[b][a]:
                if e == f:
                    print("Collision!")
                    print("Doing more road_seeking")
                    self.road_seeking(x, y)
                else:
                    print("No collision!")
                    continue

    def path_check(self, x, y):
        print("Our location is: {} {}".format(x, y))
        for r in self.paths:
            a, b = r.getLocation()
            print("Path locations: {} {}".format(a, b))
            e = x, y
            f = a, b
            if e == f:
                print("Path Collision!")
                print("Doing more road_seeking")
                return False
                #else:
                #    #THROWS TO A LOOP. NEEDS WORK
                #    print("No path collision!")
                #    continue

    def road_seeking_iterate(self):
        for i in self.road_seeker:
            x, y = i.getLocation()
            print("Current location is: {} {}".format(x, y))
            i.x, i.y = self.road_seeking(x, y)
            print("New location after running road seeking should be {} {}".format(i.x, i.y))

    def road_seeking(self, x, y):
        print("Current location during road_seeking is X {} Y {}".format(x, y))
        self.paths.append(Temp_Path(x, y))
        for i in self.paths:
            print("Temp path {} is {} {}.".format(i, i.x, i.y))
        moves = self.valid_moves(x, y)
        choice = self.random_move(moves)
        x, y = self.move_entity(choice, x, y)
        if self.collision_checker(x, y) == True:
            print("Uh oh!")
        print("New location should be {} {}".format(x, y))
        for c in self.cities:
            print("Checking cities")
            a, b = c.getLocation()
            print("City location is {} {}".format(a, b))
            e = a, b
            f = x, y
            if e == f:
                self.road_seeking(x, y)
            else:
                continue

        #if self.path_check(x, y) == False:
        #    self.road_seeking(x, y)
        #else:
        #    print("No collisions!")

        for r in self.paths:
            print("Checking paths")
            a, b = r.getLocation()
            print("Path location is {} {} and current location is {} {}".format(a, b, x, y))
            e = a, b
            f = x, y
            if e == f:
                print("Collision, re-running!")
                self.road_seeking(x, y)
            else:
                print("Returning value {} {}".format(x, y))
                return x, y
        return x, y
    #currently seems a bit buggy/ THIS IS WHERE THE PROBLEM IS
    #houston, we have a collision problem

    def valid_moves(self, x, y):
        moves = ["a", "d", "w", "s"]
        if x == 0:
            moves.remove("a")
        if x == (size - 1):
            moves.remove("d")
        if y == 0:
            moves.remove("w")
        if y == (size -1):
            moves.remove("s")
        return moves

    def move_entity(self, choice, x, y):
        if choice == "a":
            x -= 1
        elif choice == "d":
            x += 1
        elif choice == "s":
            y += 1
        elif choice == "w":
            y -= 1
        return x, y

    def random_move(self, moves):
        selection = random.choice(moves)
        return selection

    def calculate_display(self):
        for path in self.paths:
            x, y = path.getLocation()
            self.map[y][x] = "#"
        for city in self.cities:
            x, y = city.getLocation()
            self.map[y][x] = "C"
        for road in self.road_seeker:
            x, y = road.getLocation()
            self.map[y][x] = "x"

    #IMPLEMENT A FUNCTION TO PULL OCCUPIED LOCATIONS INTO A LIST OF TUPLES SO YOU CAN CHECK AGAINST IT

    def collision_checker(self, loc_x, loc_y):
        location_list = []
        for path in self.paths:
            x, y = path.getLocation()
            a = x, y
            location_list.append(a)
        for city in self.cities:
            x, y = city.getLocation()
            a = x, y
            location_list.append(a)
        for road in self.road_seeker:
            x, y = road.getLocation()
            print("Tip of the spear located at: {} {}".format(x, y))
        print(location_list)
        g = loc_x, loc_y
        if g in location_list:
            return True


    def display(self):
        for i in self.map:
            print(i)

    def tick_forward(self):
        choice = input("Do you want to tick, [y]?")
        if choice == "y":
            self.tick += 1
            print("Tick forward. Current tick: {}".format(self.tick))
        else:
            print("Invalid. Go again")
            self.tick_forward()

game = Game()

while True:
#    game.road_finder_generation()
    game.road_seeking_iterate()
#    game.city_check()
#    game.path_check()
    game.calculate_display()
    game.display()
    game.tick_forward()

#next step, create a new entity that moves and leaves a path across the map. If it connects to a city, register that
#currently only working for one square at a time, due to the return data, need to create an iterable - FIXED
#COLLISION DETECTION NOT WORKING