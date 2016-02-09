__author__ = 'iamja_000'

#INSTEAD OF DOING A LINE BY LINE COMPARISON, JUST GROUP EACH LINE
#IF LINE HAS MORE THAN 2 ENTITIES THEN CLUMP REMAINDER TO NEARBY LINES

import random
import time

size = int(input("How long dya want your lists and map size, then?"))

choice_1 = str(input("What is the dominant character on terrain?"))
choice_2 = str(input("What is another character on terrain"))

class LIST_SORTER:
    def __init__(self):
        self.base_map = [[(random.choice(choice_1+choice_2)) for i in range(size)] for i in range(size)]
        self.display_map()
        self.list_analysis()
        self.display_map()


    def display_map(self):
        for i in self.base_map:
            print(i)

    def list_analysis(self):
        for i in self.base_map:
            dominant_list = self.dominant_list_builder(i)
            if self.list_cluster_check(dominant_list) > 2:
                self.alt_list_changer(i, dominant_list)
                #self.list_changer(i, dominant_list)

    def dominant_list_builder(self, value):
        dom_list = []
        for a, b in enumerate(value):
            if b == choice_1:
                dom_list.append(a)
        return dom_list


    def list_cluster_check(self, list_positions):
        #print(list_positions)
        abs_gap = []
        for a, b in enumerate(list_positions):
            if a == len(list_positions)-1:
                continue
            else:
                abs_gap.append(abs(b-list_positions[a+1]))

        continuous_clumps = 1
        for i in abs_gap:
            if i != 1:
                continuous_clumps += 1
        #print("Our number of clumps is: {}".format(continuous_clumps))
        return continuous_clumps

    def alt_list_changer(self, value, list_major_positions):
        list_check_value = 0
        print("Top list_major_positions are now: {}".format(list_major_positions))
        for i in list_major_positions:
            print("I is ... \n {}".format(value))
            print("Top sub list_major_positions are now: {}".format(list_major_positions))
            if self.list_cluster_check(list_major_positions) > 2:
            #print(list_major_positions)
            #print(len(list_major_positions))
                time.sleep(1)
                temp_rand = random.randint(1, 2)
                if temp_rand == 1:
                    print("BINGO")
                    if list_check_value == 0:
                        if abs(list_major_positions[list_check_value] - list_major_positions[list_check_value+1]) > 1:
                            value[(list_major_positions[list_check_value+1]-1)] = choice_1
                            value[(list_major_positions[list_check_value])] = choice_2
                            list_check_value += 1
                    elif list_check_value < (len(list_major_positions))-1:
                        if abs(list_major_positions[list_check_value] - list_major_positions[list_check_value+1]) > 1:
                            #print("Cheese")
                            value[(list_major_positions[list_check_value+1]-1)] = choice_1
                            value[(list_major_positions[list_check_value])] = choice_2
                            list_check_value += 1
                    elif list_check_value == len(list_major_positions)-1:
                        print("Matched")
                else:
                    print("NO DICE")
                print("I is now... \n {}".format(value))
                list_major_positions = self.dominant_list_builder(value)
                print("Our list major positions are now: {}".format(list_major_positions))


    def list_changer(self, value, list_major_positions):
        list_check_value = 0
        for i in list_major_positions:
            print("Our list positions are {} and increment is {} and step is {} and prev is one is {}".format(list_major_positions, i, list_check_value, list_major_positions[list_check_value-1]))
            empty = 0
            if list_check_value == 0:
                print("Distance between us and upper is: {}".format(abs(list_major_positions[list_check_value] - list_major_positions[list_check_value+1])))
                if abs(list_major_positions[list_check_value] - list_major_positions[list_check_value+1]) > 1:
                    print("We should put you next to: {} which is number {} and currently {}".format(list_major_positions[list_check_value+1], list_major_positions[list_check_value+1]-1, value[(list_major_positions[list_check_value+1]-1)]))
                    value[(list_major_positions[list_check_value+1]-1)] = choice_1
                    value[(list_major_positions[list_check_value])] = choice_2

            elif list_check_value > 0:
                print("Okay")

            print("I is now... \n {} \n and list_check_value is now {}".format(value, list_check_value))
            list_check_value += 1




    def list_neighbour_check(self, checked_list_entity, value):
        if checked_list_entity == value:
            return True




game = LIST_SORTER()