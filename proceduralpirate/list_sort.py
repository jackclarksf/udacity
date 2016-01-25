__author__ = 'iamja_000'

#PLAN - WRITE A PROGRAM THAT GENERATES A LIST AND THEN SORTS IT

import random

size = int(input("Please specify the size of the map (x by x): "))

class LIST_TESTER:
    def __init__(self):
        print("Our size is {}".format(size))
        self.base_map = [[(random.choice("$X")) for i in range(size)] for i in range(size)]
        long_list_pos = self.list_sort_system()
        #print("Our long list is: {}".format(long_list_pos))
        self.list_stepper(long_list_pos)
        print("Cheese!")

    def display_map(self):
        for i in self.base_map:
            print(i)

    def list_sort_system(self):
        test_line = 0
        aggregated_dict = {}
        value_list = []
        while test_line < size:
            line_location_list = []
            for i, j in enumerate(self.base_map[test_line]):
                if j == "X":
                    line_location_list.append(i)
            aggregated_dict[test_line] = line_location_list
            test_line += 1

        for i, j in aggregated_dict.items():
            value_list.append(j)

        longest = max(value_list, key=len)
        print(longest)

        for position, list in aggregated_dict.items():
            if list == longest:
                print("!!!! {}".format(position))
                return position

    def list_stepper(self, list_seed):
        print("Our list seed is: {}".format(list_seed))
        print("So base string is: {}".format(self.base_map[list_seed]))
        if list_seed == 0:
            self.list_modifier("up", list_seed)
        elif list_seed == size-1:
            self.list_modifier("down", list_seed)
        else:
            self.list_modifier((random.choice(["up", "down"])),list_seed)



    def list_modifier(self, direction, list_start_point):
        print("OK we are going: {}".format(direction))
        our_seed = list_start_point
        count = 0
        if direction == "up":
            list_start_point = list_start_point+1
            while list_start_point < size:
                print("up!: {}".format(self.base_map[list_start_point]))
                #COMPARISON AND CHANGE OPERATION GOES HERE
                list_start_point += 1
                count += 1
            print("G'UP Our list start point is now: {} which is same as size {} and count is {}".format(list_start_point, size, count))
            if count < size-1:
                print("Still got to do some stuff, holmes")
                while our_seed > 0:
                    our_seed -= 1
                    print("down!: {}".format(self.base_map[our_seed]))
                    #COMPARISON AND CHANGE OPERATION GOES HERE
                    count += 1
                print("G'UP THEN G'DOWN Our list position is now: {} which is same as size {} and count is {}".format(our_seed, size, count))

        elif direction == "down":
            print("List start point is: {}".format(list_start_point))
            list_start_point = list_start_point-1
            print("List start point is: {}".format(list_start_point))
            while list_start_point >= 0:
                print("down!: {}".format(self.base_map[list_start_point]))
                #COMPARISON AND CHANGE OPERATION GOES HERE
                if list_start_point == 0:
                    count += 1
                    list_start_point -= 1
                    print("We are at zero and list_start_point is {} and count is now {}".format(list_start_point, count))
                else:
                    list_start_point -= 1
                    count += 1
                print("G'DOWN Our list start point is now: {} and our seed was {} and size is {} and count is {}".format(list_start_point, our_seed, size, count))
            if count < size-1:
                print("Still got to do some stuff, holmes")
                while our_seed < size-1:
                    our_seed += 1
                    print("up! with seed: {} and list: {}".format(our_seed, self.base_map[our_seed]))
                    #COMPARISON AND CHANGE OPERATION GOES HERE
                    count += 1
                print("G'DOWN THEN G'UP Our list position is now: {} which is same as size {} and count is {}".format(our_seed, size, count))


        #GO UP OR GO DOWN
        #BRING ENTITIES CLOSER
        #INCREMENENT COUNT
        #IF YOU REACH 0, THEN START FROM TOP AND DESCEND TO SEED
        #IF YOU REACH TOP, THEN START FROM BOTTOM AND ASCEND TO SEED
        print("Lemon")



game = LIST_TESTER()
game.display_map()