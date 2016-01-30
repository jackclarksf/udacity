__author__ = 'iamja_000'

#PLAN - WRITE A PROGRAM THAT GENERATES A LIST AND THEN SORTS IT

import random

size = int(input("Please specify the size of the map (x by x): "))

class LIST_TESTER:
    def __init__(self):
        print("Our size is {}".format(size))
        self.base_map = [[(random.choice("$X")) for i in range(size)] for i in range(size)]
        self.display_map()
        long_list_pos = self.list_sort_system()
        print("Our long list is: {}".format(long_list_pos))
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
                return position

    def list_stepper(self, list_seed):
        print("Our list seed is: {} \n base string is {} ".format(list_seed, self.base_map[list_seed]))
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
                self.list_changer(list_start_point-1, list_start_point)
                list_start_point += 1
                count += 1
            print("G'UP Our list start point is now: {} which is same as size {} and count is {}".format(list_start_point, size, count))
            if count < size-1:
                print("Still got to do some stuff, holmes")
                while our_seed > 0:
                    our_seed -= 1
                    print("down!: {}".format(self.base_map[our_seed]))
                    self.list_changer(our_seed+1, our_seed)
                    count += 1
                print("G'UP THEN G'DOWN Our list position is now: {} which is same as size {} and count is {}".format(our_seed, size, count))

        elif direction == "down":
            list_start_point = list_start_point-1
            while list_start_point >= 0:
                if list_start_point == 0:
                    print("down!: {}".format(self.base_map[list_start_point]))
                    self.list_changer(list_start_point+1, list_start_point)
                    count += 1
                    list_start_point -= 1
                    print("We are at zero and list_start_point is {} and count is now {}".format(list_start_point, count))
                else:
                    self.list_changer(list_start_point+1, list_start_point)
                    list_start_point -= 1
                    count += 1
                print("G'DOWN Our list start point is now: {} and our seed was {} and size is {} and count is {}".format(list_start_point, our_seed, size, count))
            if count < size-1:
                print("Still got to do some stuff, holmes")
                while our_seed < size-1:
                    our_seed += 1
                    print("up! with seed: {} and list: {}".format(our_seed, self.base_map[our_seed]))
                    self.list_changer(our_seed-1, our_seed)
                    count += 1
                print("G'DOWN THEN G'UP Our list position is now: {} which is same as size {} and count is {}".format(our_seed, size, count))

    def list_changer(self, list_to_check, list_to_change):
        #FUNCTION THAT READS THE CHECK LIST, THEN CHANGES THE LIST TO MATCH IT
        print("So that means we're comparing list {} {} against list {} {}".format(list_to_change, self.base_map[list_to_change], list_to_check, self.base_map[list_to_check]))
        change_list = []
        check_list = []
        for i, j in enumerate(self.base_map[list_to_change]):
            if j == "X":
                change_list.append(i)
        for i, j in enumerate(self.base_map[list_to_check]):
            if j == "X":
                check_list.append(i)
        print("So positions of X to check are {} against {}".format(change_list, check_list))

        if (len(change_list) == 0 or len(check_list) == 0):
            print("No length!")

        else:
            for i in change_list:
                length_list = len(change_list)
                print("Length is {} and i is {}".format(length_list, i))
                if self.is_same(i, check_list):
                    print("i {} has a buddy in there".format(i))
                else:
                    print("Gotta do it")
                    self.list_manipulator(i, check_list, change_list)


            #for j in check_list:
            #    print("Distance between i {} and j {} is {}".format(i, j, (abs(i-j))))
            #    if i == j:
            #        print("Success!")

    def list_manipulator(self, value, list_to_check, change_list):
        abs_vals = []
        list_vals = []
        for i in list_to_check:
            abs_vals.append(abs(value-i))
            list_vals.append(i)
        print(abs_vals)
        print(list_vals)
        print(min(abs_vals))

    def is_same(self, value, list_to_check):
        for i in list_to_check:
            if value == i:
                return True

game = LIST_TESTER()
game.display_map()