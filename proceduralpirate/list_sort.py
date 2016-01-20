__author__ = 'iamja_000'

#PLAN - WRITE A PROGRAM THAT GENERATES A LIST AND THEN SORTS IT

import random

size = int(input("Please specify the size of the map (x by x): "))

class LIST_TESTER:
    def __init__(self):
        self.base_map = [[(random.choice("$X")) for i in range(size)] for i in range(size)]

    def display_map(self):
        for i in self.base_map:
            print(i)

game = LIST_TESTER()
game.display_map()