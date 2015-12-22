__author__ = 'iamja_000'

def easy_coordinate(x, y, n):
    xrange = list(range(x-n, x+(n+1)))
    yrange = list(range(y-n, y+(n+1)))
    combined_coordinates = []
    for i in xrange:
        for j in yrange:
            if (i, j) != (x, y):
                combined_coordinates.append((i, j))
    print("Coord list is {}".format(combined_coordinates))

easy_coordinate(4, 5, 2)

#TAKES IN X AND Y POSITION, THEN LETS YOU SPECIFY TILE SEEK SIZE, AND DELETES INVALID ONES.
# CAN RETURN COORDINATES FOR ANY SCAN AMOUNT
def easy_limit_coordinate(x, y, n, size):
    xrange = list(range(x-n, x+(n+1)))
    yrange = list(range(y-n, y+(n+1)))
    combined_coordinates = []
    for i in xrange:
        if i < 0:
            xrange.remove(i)
        elif i > size:
            xrange.remove(i)
        else:
            for j in yrange:
                if j < 0:
                    yrange.remove(j)
                elif j > size:
                    yrange.remove(j)
                else:
                    if (i, j) != (x, y):
                        combined_coordinates.append((i, j))
    print("Coord list is {}".format(combined_coordinates))
    return combined_coordinates



easy_limit_coordinate(2, 4, 10, 10)

print("DOG ON IT")

easy_limit_coordinate(5, 7, 3, 10)

easy_limit_coordinate(0, 0, 10, 10)

    def coordinate_maker(self):
        x_map = [i for i in range(size)]
        y_map = [i for i in range(size)]
        mixed_list = []
        for i in x_map:
            for b in y_map:
                c = i, b
                mixed_list.append(c)
        return mixed_list

    #THERE MUST BE A WAY TO MODIFY THIS SO AS TO GET ANY COORDINATES FROM BOARD