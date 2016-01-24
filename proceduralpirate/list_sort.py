__author__ = 'iamja_000'

#PLAN - WRITE A PROGRAM THAT GENERATES A LIST AND THEN SORTS IT

import random

size = int(input("Please specify the size of the map (x by x): "))

class LIST_TESTER:
    def __init__(self):
        self.base_map = [[(random.choice("$X")) for i in range(size)] for i in range(size)]
        long_list_pos = self.list_sort_system()
        print("Our long list is: {}".format(long_list_pos))

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

    def list_modifier(self, list_seed):
        #TAKE LIST SEED
        #GO UP OR GO DOWN
        #BRING ENTITIES CLOSER
        #INCREMENENT COUNT
        #IF YOU REACH 0, THEN START FROM TOP AND DESCEND TO SEED
        #IF YOU REACH TOP, THEN START FROM BOTTOM AND ASCEND TO SEED



game = LIST_TESTER()
game.display_map()