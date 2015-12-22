__author__ = 'iamja_000'

x = 2
y = 4
e = x, y

moves = ["a", "d", "w", "s"]

some_coords = [(1, 2), (2, 4), (3, 4), (1, 1), (11, 4), (7, 4)]

for i in some_coords:
    print(i)

print(e)

#if e in (some_coords):
#    print("Contains it!")

def list_convergence(e, x, y, some_coords):
    while e not in some_coords:
        print("E is {}".format(e))
        x -= 1
        e = x, y
        print("New E is {}".format(e))
    return e

def neighbour_check(e, some_coords):
    if e in some_coords:
        print("Collision!")
        return True

neighbour_check(e, some_coords)
list_convergence(e, x, y, some_coords)
e = list_convergence(e, x, y, some_coords)
print("E is now {}".format(e))

a, b = x, y
print(a, b)

check_coord = []
check_coord.append(a)
check_coord.append(b)
print("Check_coord {}".format(check_coord))

def validator_list(list_of_neighbours, move_list, x_value, y_value, move_to_remove):
    print("Checking values X: {} and Y: {}".format(x_value, y_value))
    resulting_num = x_value, y_value
    if neighbour_check(resulting_num, list_of_neighbours):
        move_list.remove("d")
        return move_list

print("Moves were: {}".format(moves))
moves = validator_list(some_coords, moves, x+1, y, "d")
print("New moves: {}".format(moves))

#so this seems to work, and we can modify the value at time of doing function

def collision_moves(self, moves, x, y):
        print("Checking neighbours for {} {}".format(x, y))
        check_coord = []
        neighbours = []
        check_coord.append(x)
        check_coord.append(y)
        for i in check_coord:
            neighbours.extend((i-1, i, i+1))
        for i in neighbours:
            if i < 0:
                neighbours.remove(i)
        print("Neighbours here: {}".format(neighbours))

        def collision_list(self, neighbours):
            pairs = []
            i = 0
            while i < ((len(neighbours) / 2)):
                a = neighbours[i]
                b = neighbours[-1]
                c = a, b
                pairs.append(c)
                b = neighbours[-2]
                c = a, b
                pairs.append(c)
                b = neighbours[-3]
                c = a, b
                pairs.append(c)
                i += 1
            for i in pairs:
                for c in i:
                    if c < 0:
                        pairs.pop[i]
            return pairs

        pair_list = collision_list(self, neighbours)
        known_entities = []

        def entity_appender(check_item):
            for i in check_item:
                a, b = i.getLocation()
                c = a, b
                known_entities.append(c)

        entity_appender(self.road_seeker)
        entity_appender(self.cities)
        entity_appender(self.road_paths)

        #NEXT STEP, LOG PATHS OR CREATE PATHS INTO A LIST TO BE CHECKED AGAINST

        print("Total coordinate set is at:  {}".format(pair_list))
        print("Occupied territory at: {}".format(known_entities))

        def move_validator_function(self, a, b, moves, all_coords, pos_collisions):
            c = a, b
            print("Our coords: {} ".format(c))
            if occupied_check(self, a+1, b, all_coords):
                print("Should remove D.")

        def occupied_check(self, a, b, all_coords):
            if self.map[b][a] == " ":
                return False
            else:
                print("Detecting collision of {} {}".format(a, b))
                return True

#this is workable but we need to deal with the edge issue

        move_validator_function(self, x, y, moves, pair_list, known_entities)
        valid_coordinates = []

        for entity in pair_list:
            if entity in known_entities:
                continue
            else:
                valid_coordinates.append(entity)

        print("Valid coordinates are {}".format(valid_coordinates))
        return valid_coordinates

        # IDEALLY I WANT TO JUST RETURN VALID OPTIONS, RATHER THAN COORDINATES

        ###RANDOMIZE THE CHOICE