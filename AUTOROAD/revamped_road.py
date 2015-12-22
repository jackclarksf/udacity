__author__ = 'iamja_000'

import random
from random import randrange
from road_entities import City
from road_entities import Road_Finder
from road_entities import Temp_Path

#NEED TO WRITE A MOVEMENT ERROR CHECKER AND A BETTER BOARD CLEANER

#NEED FUNCTION TO DEFINE ORIGIN CITY, AND AN ORIGIN PATH NUMBER, WHICH IS TIED TO A UNIQUE SEED FOR EACH ROAD CREATOR

#NEXT FUNCTION SHOULD BE TO CHECK CITY GROWTH RATE AT EACH TIME STEP QAND PRINT OUT GROWTH AND POPULATION GROWTH OVER TIME

#NEXT STEPS:
# HAVE CITIES REGENERATE SCOUTS - DONE, INCLUDING ANCHOR KNOWLEDGE
# HAVE SCOUT ROADS DECAY - HALF DONE
#NEED TO WRITE FUNCTION TO SCATTER INITIAL CITY LOCATIONS TO AVOID CLUMPS - HALF-DONE

#need to straighten non_city roads

#POSSIBLE ROAD_DELETER SOLUTION
#CREATE LIST OF DELETED ROAD_SEEKERS
#GET ORIGIN CITIES
#CHECK ROAD_SEEKER IN MAP FOR COLLISION
#DELETE IF THERE'S A COLLISION
#LATER PLAN - GIVE EACH ROAD_SEEKER A UNIQUE ORIGIN COORDINATE. ONLY DELETE ROADS WITH CORIGIN & UNIQUEID ORIGIN

seed = 4
size = 10

def generateLocation(world):
    x = randrange(0, size)
    y = randrange(0, size)
    while (str(world[y][x]) != " "):
        x = randrange(0, (size - 1))
        y = randrange(0, (size - 1))
    return x, y

#THIS CURRENTLY ONLY WORKS WITH TWO. NEED TO RE-ENGINEER FOR MORE. SUITS OUR PURPOSES NOW, THOUGH.
def city_scatter_location(city_number, map_size, step_point):
    sub_divide = map_size/city_number
    if step_point == 0:
        x = randrange(0, sub_divide)
        y = randrange(0, map_size)
    else:
        x = randrange(sub_divide, (sub_divide*(step_point+1)))
        y = randrange(0, map_size)
    return x, y

#NEW GOAL - CHECK FOR PROXIMITY WITHIN SPECIFIABLE NUMBER OF TILES
#IF SOMETHING IS THERE, THEN RE-ROLL CITIES

class Game:
    def __init__(self):
        self.tick = 0
        self.dead_ids = []
        self.road_seeker = []
        self.dead_roads = []
        self.road_paths = []
        self.cities = []
        self.map = [[" " for i in range(size)] for i in range(size)]

        def city_generation(seed):
            city_coordinates = []
            x, y = generateLocation(self.map)
            self.cities.append(City(x, y, x, y))
            for i in range(seed-1):
                x, y = generateLocation(self.map)
                city_coordinates = self.entity_finder(self.cities, city_coordinates)
                print("Our city locations are {}".format(city_coordinates))
                if len(city_coordinates) > 0:
                    x, y = generateLocation(self.map)
                    #print("Candidate location is {} {}".format(x, y))
                    while self.scout_for_city_proximity(x, y, city_coordinates, 4) != False:
                        x, y = generateLocation(self.map)
                        #print("New location is {} {}".format(x, y))
                self.cities.append(City(x, y, x, y))
                #STILL NOT ITERATING CORRECTLY

        city_generation(seed)

        def initial_scout_generation(seed):
            for i in range(seed):
                x, y = self.cities[i].getLocation()
                a, b = x, y
                self.additional_scout_generation(x, y, a, b)

        initial_scout_generation(seed)

    ###RANDOM SEEDER - RETURNS A RANDOM STRING OF NUMBERS OF SPECIFIABLE LENGTH. NEXT - IMPLEMENT GLOBAL LIST TO CHECK
    def random_maker(self, length_of_string):
        random_string = ""
        for i in range(int(length_of_string)):
            random_string += str(random.randint(0, 9))
        return random_string

    ###MOVEMENT CHECKING ZONE
    def additional_scout_generation(self, input_x, input_y, c_x, c_y):
            possible_moves = self.valid_moves(input_x, input_y)
            choice_move = self.random_move(possible_moves)
            x, y = self.move_entity(choice_move, input_x, input_y)
            proposed_path_value = self.random_maker(3)
            final_path_value = self.reroll_path_value(proposed_path_value)
            self.road_seeker.append(Road_Finder(x, y, c_x, c_y, final_path_value))

#TAKES IN X AND Y POSITION, THEN LETS YOU SPECIFY TILE SEEK SIZE, AND DELETES INVALID ONES.
# CAN RETURN COORDINATES FOR ANY SCAN AMOUNT, INCLUDING WHOLE BOARD
    def easy_limit_coordinate(self, x, y, n, size):
        xrange = list(range(x-n, x+(n+1)))
        yrange = list(range(y-n, y+(n+1)))
        combined_coordinates = []
        for i in xrange:
            if i < 0:
                xrange.remove(i)
            elif i >= size:
                xrange.remove(i)
            else:
                for j in yrange:
                    if j < 0:
                        yrange.remove(j)
                    elif j >= size:
                        yrange.remove(j)
                    else:
                        if (i, j) != (x, y):
                            combined_coordinates.append((i, j))
        return combined_coordinates

#GENERATES A LIST OF ENTITIES
    def entity_finder(self, check_item, list_to_add):
            for i in check_item:
                c = i.getLocation()
                list_to_add.append(c)
            return list_to_add

    def entity_seeker(self, a, b, c):
        known_items = []
        known_items = self.entity_finder(a, known_items) #self.road_seeker
        known_items = self.entity_finder(b, known_items) #self.cities
        known_items = self.entity_finder(c, known_items) #self.road_paths
        return known_items

    def move_validator_function(self, a, b, moves, all_coords, pos_collisions):
        #print("Potential moves are: {}".format(moves))
        c = a, b
        if "a" in moves:
            if self.occupied_check(a-1, b):
                moves.remove("a")
        if "d" in moves:
            if self.occupied_check(a+1, b):
                moves.remove("d")
        if "w" in moves:
            if self.occupied_check(a, b-1):
                moves.remove("w")
        if "s" in moves:
            if self.occupied_check(a, b+1):
                moves.remove("s")
        return moves

    def occupied_check(self, a, b):
        if self.map[b][a] == " ":
            return False
        else:
            return True

    def occupied_within_tiles(self, x, y, city_list):
        while self.scout_for_city_proximity(x, y, city_list, 3) != False:
            x, y = generateLocation(self.map)
            return x, y
        return x, y

    def find_valid_coordinates(self, all_coordinates, known_neighbours):
        valid_coordinates = []
        for entity in all_coordinates:
            if entity in known_neighbours:
                continue
            else:
                valid_coordinates.append(entity)
        return valid_coordinates

    #SCOUT & CITY FINDER FUNCTION

    def scout_city_collision(self, x, y, cities_to_check):
        for i in cities_to_check:
            print("Checking i {} against {} {}".format(i, x, y))
            d = x, y
            if i == d:
                print("Scout {} overlaps with city at {}".format(d, i))
                return True

    def scout_for_city_check(self, x, y, i):
        #generates list of cities excluding location
        city_locations = []
        scout_c_loc = i.broadcast_city()
        for c in self.cities:
            d = c.getLocation()
            if d == scout_c_loc:
                continue
            else:
                city_locations.append(d)
        return city_locations

#NOT QUITE SURE OF WHAT THIS DOES
    def scout_for_city_return(self, x, y, i):
        #generates list of cities excluding location
        city_locations = []
        scout_c_loc = i.broadcast_city()
        for c in self.cities:
            d = c.getLocation()
            if d == scout_c_loc:
                continue
            else:
                return c
        return c

    def return_specific_city(self, x, y):
        for i in self.cities:
            c = i.getLocation()
            d = x, y
            if c == d:
                return i
            else:
                continue

#checks whether city within list is within SPECIFIABLE DISTANCE of coordinates of the thing
            #SHOULD BE ABLE TO REIMPLEMENT THIS, SURELY?
    def scout_for_city_proximity(self, x, y, city_list, tile_value):
        for i in city_list:
            temp_x, temp_y = i
            if (x-tile_value) <= temp_x <= (x+tile_value):
                if (y-tile_value) <= temp_y <= (y+tile_value):
                    return True
                else:
                    return False
            elif (y-tile_value) <= temp_y <= (y+tile_value):
                if (x-tile_value) <= temp_x <= (x+tile_value):
                    return True
                else:
                    return False

    def scout_for_city_list_coordinates(self, x, y, city_list, tile_value):
        for i in city_list:
            temp_x, temp_y = i
            if (x-tile_value) <= temp_x <= (x+tile_value):
                if (y-tile_value) <= temp_y <= (y+tile_value):
                    return temp_x, temp_y
                else:
                    return False
            elif (y-tile_value) <= temp_y <= (y+tile_value):
                if (x-tile_value) <= temp_x <= (x+tile_value):
                    return temp_x, temp_y
                else:
                    return False

    def scout_movement_toward_city(self, x, y, candidate_cities, moves):
        #print("Launching movement cycle of checking {} {} against {} with current moves {}".format(x, y, candidate_cities, moves))
        a, b = candidate_cities[0]
        #THIS IS ONLY DOING THIS ONCE FOR EACH THING, RATHER THAN DOING ALL
        if x < a:
            moves.remove("a")
        elif x > a:
            moves.remove("d")
        elif x == a:
            moves.remove("a")
            moves.remove("d")
        if y < b:
            moves.remove("w")
        elif y > b:
            moves.remove("s")
        elif y == b:
            moves.remove("w")
            moves.remove("s")
        return moves

    def valid_moves(self, x, y):
        collision_free = []
        moves = ["a", "d", "w", "s"]
        moves = self.edge_moves(moves, x, y)
        pair_list = self.easy_limit_coordinate(x, y, 1, size)
        known_neighbours = self.entity_seeker(self.road_seeker, self.cities, self.road_paths)
        possible_coordinates = self.find_valid_coordinates(pair_list, known_neighbours)
        moves = self.move_validator_function(x, y, moves, possible_coordinates, known_neighbours)
        return moves

    def edge_moves(self, moves, x, y):
        if x == 0:
            moves.remove("a")
        if x == (size - 1):
            moves.remove("d")
        if y == 0:
            moves.remove("w")
        if y == (size - 1):
            moves.remove("s")
        return moves

    def random_move(self, moves):
        selection = random.choice(moves)
        return selection

    ###ENTITY MOVEMENT ZONE
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

    ###VISUAL ZONE

    #THIS FUNCTION LETS US DISPLAY A SPECIFIC ENTITY ON A MAP COMPOSED OF NESTED LISTS
    def display_subsector(self, entity_to_display, name):
        for c in entity_to_display:
            x, y = c.getLocation()
            self.map[y][x] = name

    def display_blank_coordinates(self):
        coord_doubles = self.easy_limit_coordinate(0, 0, size, size)
        for i in coord_doubles:
            a, b = i
            self.map[b][a] = " "
            #CURRENTLY CAN ONLY BE BLANKE

    #THIS FUNCTION CLEANS THE PATH FROM THE MAP IF A CITY HAS BEEN FORMED - STILL A BIT BUGGY
    def road_cleaner(self, c_x_origin, c_y_origin):
        road_origin = c_x_origin, c_y_origin
        for r in self.road_paths:
            r_x, r_y = r.getLocation()
            comb_r_coord = r_x, r_y
            #print("Checking path {} with location {} against origin {}".format(r, comb_r_coord, road_origin))
            for c in self.cities:
                x, y = c.getLocation()
                comb_c_coord = x, y
                c_origin = c.broadcast_city_origin()
                #print("City is located at {} with origin {}".format(comb_c_coord, c_origin))
                if road_origin == comb_c_coord:
                    #print("Collision between road_seeker at {} with origin {} and starting_city at {}".format(comb_r_coord, road_origin, comb_c_coord))
                    #print("road_paths has len {}".format(len(self.road_paths)))
                    self.road_paths.remove(r)
                    #print("road paths now has len {}".format(len(self.road_paths)))
                else:
                    return self.road_paths
            return self.road_paths

                #TEST IF ROAD PATHS APPEARS OUTSIDE FUNCTION, OTHERWISE YOU MAY NEED TO RETURN IT

    def reroll_path_value(self, path_value):
        for i in self.road_paths:
            path_id = i.broadcast_road_key
            if path_value == path_id:
                path_value == self.random_maker(3)
            else:
                return path_value
        return path_value


    def check_road_id_against_paths(self, road_identifier):
        for i in self.road_paths:
            path_id = i.broadcast_road_key()
            if road_identifier == path_id:
                print("Deleting road path with {} due to collision with {}".format(road_identifier, path_id))
                self.road_paths.remove(i)
                if road_identifier not in self.dead_ids:
                    self.dead_ids.append(road_identifier)

    def road_printer(self):
        print("Road paths is currently {}".format(self.road_paths))
        print("Dead paths is currently: {}".format(self.dead_ids))
        #for i in self.road_paths:
            #path_id = i.broadcast_road_key()
            #print("Road locations with keys {}".format(path_id))

    def get_dead_roads_and_delete(self):
        for i in self.road_paths:
            path_id = i.broadcast_road_key()
            print("Road paths keys are: {}".format(path_id))
            for c in self.dead_ids:
                print("Dead ids are: {}".format(c))
                if path_id == c:
                    print("Collision between {} and {}".format(path_id, c))
                    self.road_paths.remove(i)
        return self.road_paths

    def dead_road_coordinates(self):
        print("Origin city coordinates of dead roads {}".format(self.dead_roads))

    def wipe_all_dead_roads(self):
        #function currently doesn't work because road_paths only captures current state. Need record of all originating cities
        #suggested fix - have each scout creation log the origin coordinate elsewhere
        for o in self.cities:
            d, e = o.broadcast_city_origin()
            f = d, e
            for i in self.dead_roads:
                print("Testing cities {} against dead roads with origin {}".format(f, i))
                if i == f:
                    print("Collision between i {} and f {}".format(i, f))
                    #SWEEP THROUGH ROADS AND DELETE THOSE WITH THAT ORIGIN COORDINATE
                    for q in self.road_paths:
                        cx0, cx0 = q.broadcast_city()
                        trouble_origin = cx0, cx0
                        if i == trouble_origin:
                            print("Attempting to remove road path with origin {} as collides with dead road {}".format(trouble_origin, i))
                            self.road_paths.remove(q)
                            #this has become an auto-deleter function. oh dear.

    def print_all_roads_and_locations(self):
        self.dead_road_coordinates()
        for i in self.road_paths:
            a, b = i.getLocation()
            cx0, cy0 = i.broadcast_city()
            #print("Road {} {} has origin city {} {}".format(a, b, cx0, cy0))

    def road_deleter(self, origin_spotx, origin_spoty):
        #print("Road paths is {}".format(self.road_paths))
        for i in self.road_paths:
            a, b = i.broadcast_city()
            x = origin_spotx
            y = origin_spoty
            z = x, y
            q = a, b
            c = i.broadcast_name()
            #print("Road path has origination: {} {} with key {}".format(a, b, c))
            if z == q:
                #print("Removing road path with origin of {} due to scout with origin of {}".format(z, q))
                self.road_paths.remove(i)
        #print("Road paths is now {}".format(self.road_paths))
        return self.road_paths

    #THIS FUNCTION DISPLAYS THE WHOLE MAP, LOADING EACH SECTOR INDIVIDUALLY
    def display_map(self):
        self.display_blank_coordinates()
        self.display_subsector(self.road_paths, "#")
        self.display_subsector(self.cities, "c")
        self.display_subsector(self.road_seeker, "x")
        for i in self.map:
            print(i)

    #THIS LETS US MOVE THE MAP FORWARD
    def tick_forward(self):
        choice = input("Do you want to tick, [y]?")
        if choice == "y":
            self.tick += 1
            print("Tick forward. Current tick: {}".format(self.tick))
        else:
            print("Invalid. Go again")
            self.tick_forward()

# MOVE SCOUT ITEMS
    def scout_iterate(self):
        for i in self.road_seeker:
            road_id = i.broadcast_unique_key()
            #print("Checking road with unique key: {}".format(road_id))
            x, y = i.getLocation()
            possible_moves = self.valid_moves(x, y)
            if len(possible_moves) == 0:
                cx0, cy0 = i.broadcast_city()
                dead_coord = cx0, cy0
                self.road_seeker.remove(i)
                self.check_road_id_against_paths(road_id)
                #self.road_deleter(cx0, cy0)
                #self.dead_roads.append(dead_coord)
                self.map[y][x] = "."
            else:
                possible_cities = self.scout_for_city_check(x, y, i)
                if self.scout_for_city_proximity(x, y, possible_cities, 1):
                    c_x, c_y = self.scout_for_city_list_coordinates(x, y, possible_cities, 1)
                    cx0, cy0 = i.broadcast_city()
                    dead_coord = cx0, cy0
                    self.road_seeker.remove(i)
                    self.check_road_id_against_paths(road_id)
                    #self.road_deleter(cx0, cy0)
                    #self.dead_roads.append(dead_coord)
                    self.cities.append(City(x, y, c_x, c_y))
                    candidate_c = self.return_specific_city(x, y)
                    candidate_c.growth_timer()
                    return self.road_paths

                elif self.scout_for_city_proximity(x, y, possible_cities, 2):
                    moves = ["a", "d", "w", "s"]
                    moves = self.scout_movement_toward_city(x, y, possible_cities, moves)
                    i.x, i.y = self.scout_movement(i, moves)
                    c_x, c_y = i.broadcast_city()
                    if self.map[y][x] != " ":
                        self.road_paths.append(Temp_Path(x, y, c_x, c_y, road_id))
                else:
                    i.x, i.y = self.scout_movement(i, possible_moves)
                    c_x, c_y = i.broadcast_city()
                    if self.map[y][x] != " ":
                        self.road_paths.append(Temp_Path(x, y, c_x, c_y, road_id))
                    self.scout_for_city_check(i.x, i.y, i)
        return self.road_paths

    def scout_movement(self, scout_target, moves):
        x, y = scout_target.getLocation()
        a, b = self.movement_validator(x, y, moves)
        return a, b

    def movement_validator(self, x, y, moves):
        def check_against(self, moves, x, y):
            choice_move = self.random_move(moves)
            x, y = self.move_entity(choice_move, x, y)
            return x, y

        x, y = check_against(self, moves, x, y)
        return x, y

game_world = Game()

while True:
    game_world.display_map()
    #game_world.road_printer()
    game_world.scout_iterate()
    game_world.get_dead_roads_and_delete()
    game_world.road_printer()
    #game_world.all_current_ids_on_board()
    #game_world.dead_road_coordinates()
    #game_world.wipe_all_dead_roads()
    #game_world.print_all_roads_and_locations()
    #print("Length of paths {}".format(len(game_world.road_paths)))
    for c in game_world.cities:
        c.growth_addition()
        if c.growth_level():
            #print("Should attempt growth now")
            x, y = c.getLocation()
            x0, y0 = c.broadcast_city_origin()
            #print("City at location {} {} has origin {} {}".format(x, y, x0, y0))
            game_world.additional_scout_generation(x, y, x0, y0)
            #CURRENT ISSUE - ROAD_CLEANER FUNCTION BURIED DEEPLY. NEED TO RETURN MODIFIED ROAD PATHS TO MAIN LOOP.

    #print("Length of paths now {}".format(len(game_world.road_paths))) #CURRENTLY PRINTING ZERO. WHY???
    game_world.tick_forward()

    #NOW SUCCESSFULLY PRINTING ROAD PATHS, BUT SINGLE TENANCY MEANS YOU CHOP OUT SPOTTY THINGS - MUST MAKE SURE ROAD PATHS DO NOT OVERLAP