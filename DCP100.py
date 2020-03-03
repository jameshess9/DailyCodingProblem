# given an infinite 2d grid and a given list of points find the min travel distance between the points
# req : must go in order that the elems are listed in
# can move in any of the 8 directions therefore total number of moves will be equal to
# the max between delta x and delta y
def find_shortest_path(points):
    retVal = 0
    for i in range(len(points) - 1):
        first_elem = points[i]
        next_elem = points[i + 1]

        delta_x = abs(first_elem[0] - next_elem[0])
        delta_y = abs(first_elem[1] - next_elem[1])

        if (delta_x > delta_y):
            retVal += delta_x
        else:
            retVal += delta_y
    return retVal


test = [(0, 0), (1, 1), (1, 3)]
print(find_shortest_path(test))
