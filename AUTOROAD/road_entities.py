__author__ = 'iamja_000'

class City:
    def __init__(self, x, y, a, b):
        self.x = x
        self.y = y
        self.x0 = a
        self.y0 = b
        self.growth = 0
        print("CITY BORN AT {} {} WITH ORIGIN {} {}!".format(self.x, self.y, self.x0, self.y0))

    def __str__(self):
        return str("C")

    def getLocation(self):
        return self.x, self.y

    def broadcast_city_origin(self):
        return self.x0, self.y0

    #NEED FUNCTION TO INITIATE GROWTH TIMER
    def growth_timer(self):
        self.growth += 1
        #print("Growth at {} {} is now {}".format(self.x, self.y, self.growth))

    def growth_addition(self):
        if self.growth > 0:
            self.growth += 1
            #print("Growth at city hub {} {} is now: {}".format(self.x, self.y, self.growth))

    def growth_level(self):
        if self.growth == 10:
            self.growth = 1
            return True

class Road_Finder:
    #ADD IN A STARTING COORDINATE SO YOU KNOW WHAT TO LINK BACK TO

    starting_coordinates = []

    def __init__(self, x, y, a, b, c):
        self.x = x
        self.y = y
        self.x0 = a
        self.y0 = b
        self.c_string = c
        print("SCOUT BORN AT {} {} WITH ORIGIN CLUSTER {} {} and unique key of {}".format(self.x, self.y, self.x0, self.y0, self.c_string))

    def __str__(self):
        return "x"
        #return self.x, self.y

    def getLocation(self):
        return self.x, self.y

    def broadcast_city(self):
        #print("Originating city located at {} {}".format(self.x0, self.y0))
        return self.x0, self.y0

    def broadcast_unique_key(self):
        return self.c_string

class Temp_Path:
    def __init__(self, x, y, a, b, c):
        self.x = x
        self.y = y
        self.x0 = a
        self.y0 = b
        self.c_string = c
        print("ROAD PATH BORN AT {} {} WITH ORIGIN {} {} and unique road key of {}!".format(self.x, self.y, self.x0, self.y0, self.c_string))

    def __str__(self):
        return "#"

    def getLocation(self):
        return self.x, self.y

    def broadcast_road_key(self):
        return self.c_string

    def broadcast_city(self):
        #print("Originating city located at {} {}".format(self.x0, self.y0))
        return self.x0, self.y0

    def broadcast_name(self):
        return self.c_string
