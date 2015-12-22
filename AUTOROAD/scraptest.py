__author__ = 'iamja_000'

import random

size = 10

map = [[" " for i in range(size)] for i in range(size)]
coord_map = [[i for i in range(size)] for i in range(size)]

#print(coord_map)
def coordinate_builder(size):
    print("Launching builder")
    printer_list = []
    count = 0
    for i in range(size):
        printer_number = i, count
        print(printer_number)
        printer_list.append(printer_number)
    print(printer_list)

#coordinate_builder(size)

def coordinate_seeker(x, y):
    check_coord = []
    neighbours = []
    check_coord.append(x)
    check_coord.append(y)
    for i in check_coord:
        neighbours.extend((i-1, i, i+1))
    print(check_coord)
    print(neighbours)

#coordinate_seeker(0, 0)

x_map = [i for i in range(size)]
y_map = [i for i in range(size)]

#print(x_map)

def coordinate_maker(x_input, y_input):
    mixed_list = []
    for i in x_input:
        for b in y_input:
            c = i, b
            mixed_list.append(c)
    return mixed_list

coord_doubles = coordinate_maker(x_map, y_map)

for i in coord_doubles:
    a, b = i
    #print(a, b)

#print(map)

for i in coord_doubles:
    a, b = i
    map[b][a] = "X"

#print(map)

dog = random.randint(0, 10)
#print(dog)

def random_maker(length_of_string):
    random_string = ""
    for i in range(int(length_of_string)):
        random_string += str(random.randint(0, 9))
    return random_string

#lemonhead = random_maker(3)
#print(lemonhead)

def print_something(func_to_print):
    print("Hello! {}".format(func_to_print))

#print_something(random_maker(3))

size = 10
def coordinate_seeker(x, y):
        #check_coord = []
    neighbours = []
    neighbours.extend((x-2, x, x+2))
    neighbours.extend((y-2, y, y+2))
    for i in neighbours:
        if i < 0:
            neighbours.remove(i)
        #MAYBE USE A GENERATOR EXPRESSION?

    print("Neighbours is {}".format(neighbours))

coordinate_seeker(4, 5)

def coordinate_seeker_mark_two(variable_x, variable_y, modifier_amount, board_size):
    xneighbours = []
    yneighbours = []
    print("Launching mark two")
    check_counter = 0
    modifier_amount_iterator = 1
    while modifier_amount_iterator <= modifier_amount:
            xneighbours.extend((variable_x-modifier_amount_iterator, variable_x, variable_x+modifier_amount_iterator))
            yneighbours.extend((variable_y-modifier_amount_iterator, variable_y, variable_y+modifier_amount_iterator))
            modifier_amount_iterator += 1
    print("Mark two neighbours is x {} and y {}".format(xneighbours, yneighbours))
    for i in xneighbours:
            if i < 0:
                xneighbours.remove(i)
    for i in xneighbours:
            if i > board_size:
                xneighbours.remove(i)
    for i in yneighbours:
            if i < 0:
                yneighbours.remove(i)
    for i in yneighbours:
            if i > board_size:
                yneighbours.remove(i)
    print("Mark two neighbours after modification is x {} and y {} with length x and length y".format(xneighbours, yneighbours, len(xneighbours), len(yneighbours)))

    neighbours = xneighbours + yneighbours
    n_length = len(neighbours)
    print("N should be {}".format(n_length))
    print("Combined neighbours is {} with length: {} ".format(neighbours, n_length))
    pairs = []

    i = 0
    while i < (int(n_length) / 2):
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
            print("Pairs is {}".format(pairs))
    #THIS GIVES US POSSIBLE LOCATION PAIRS TO CHECK WITHIN THE SPECIFIED AMOUNT

#a.extend(range(5,10))

coordinate_seeker_mark_two(4, 5, 1, size)

def easy_coordinate(x, y, n):
    xrange = list(range(x-n, x+n))
    yrange = list(range(y-n, y+n))
    combined_coordinates = []
    for i in xrange:
        for j in yrange:
            if (i, j) != (x, y)
            combined_coordinates.append((i, j))

easy_coordinate(4, 5, 1)