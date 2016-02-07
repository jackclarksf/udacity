__author__ = 'iamja_000'

#INSTEAD OF DOING A LINE BY LINE COMPARISON, JUST GROUP EACH LINE
#IF LINE HAS MORE THAN 2 ENTITIES THEN CLUMP REMAINDER TO NEARBY LINES

import random

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
            dominant_list = []
            sub_ordinate_list = []
            for a, b in enumerate(i):
                if b == choice_1:
                    dominant_list.append(a)
            #print(dominant_list)
            #print(len(dominant_list))
            if len(dominant_list) > 2:
                self.list_changer(i, dominant_list)


    def list_changer(self, value, list_major_positions):
        list_check_value = 0
        for i in list_major_positions:
            print("Our list positions are {} and increment is {} and step is {} and prev is one is {}".format(list_major_positions, i, list_check_value, list_major_positions[list_check_value-1]))
            empty = 0
            print(list_major_positions)
            print(i)
            print(value)
            print(len(value))
            if list_check_value == 0:
                print("Distance between us and upper is: {}".format(abs(list_major_positions[list_check_value] - list_major_positions[list_check_value+1])))
                if abs(list_major_positions[list_check_value] - list_major_positions[list_check_value+1]) > 1:
                    print("We should put you next to: {} which is number {} and currently {}".format(list_major_positions[list_check_value+1], list_major_positions[list_check_value+1]-1, value[(list_major_positions[list_check_value+1]-1)]))
                    value[(list_major_positions[list_check_value+1]-1)] = choice_1
                    value[(list_major_positions[list_check_value])] = choice_2
            print("I is now... \n {}".format(value))

            if i < (len(value))-1:
                print("Checking i {} plus one {} and minus one {} in base list with length: {}".format(i, i+1, i-1, len(value)))
                if self.list_neighbour_check(value[i-1], choice_2):
                    empty += 1
                if self.list_neighbour_check(value[i+1], choice_2):
                    empty += 1
                if empty == 2:
                    print("Empty on both sides, we should move")
                else:
                    print("Looks like collisions...")
            list_check_value += 1


    def list_neighbour_check(self, checked_list_entity, value):
        if checked_list_entity == value:
            return True


            #    distance = abs(major_list[i]-j)
            #    #print("Our difference is: {}".format(distance))
            #    if distance < 1:
            #        dist_count += 1
            #        print("[ifdist] Distance between {} and {} is {} and dist_count is {}".format(major_list[i], j, distance, dist_count))
            #    elif dist_count > 0:
            #        print("[elifdist]Distance between {} and {} is {}".format(major_list[i], j, distance))
            #i += 1







game = LIST_SORTER()