# given a 2d matrix of 0 and 1
# let 0 equal empty space and 1 equal to wall
# you can only move down and right
# return number of ways to get to the bottom right from the top left
# what we do at each point is check and see if bottom/right have walls and if they don't
# we add total # of moves from each direction to our current spots num_moves == retVal
# if we are at the bottom right we return 1


def find_num_paths_rec(grid, position):
    ret_val = 0
    x = position[0]
    y = position[1]

    if x == len(grid) - 1 and y == len(grid[0]) - 1:
        return 1

    if x + 1 < len(grid) and grid[x + 1][y] == 0:
        ret_val += find_num_paths_rec(grid, (x + 1, y))

    if y + 1 < len(grid[0]) and grid[x][y + 1] == 0:
        ret_val += find_num_paths_rec(grid, (x, y + 1))

    return ret_val 


def find_num_paths(grid):
    position = (0, 0)
    return find_num_paths_rec(grid, position)


def given_solution(matrix):
    # they use a dynamic programming approach to fill in a 2d array for each grid spot
    m, n = len(matrix), len(matrix[0])
    num_ways_matrix = [[0 for j in range(n)] for i in range(m)]
    # so we initially start of with an array of all 0's representing each grid location

    # we can think of this problem as each grid spot can be reached by going from either the top or the left
    # so all the grid positions on the top can only be reached from the left therefore they all have only 1 way
    # note if we hit a wall we must break because those spots are no longer reachable

    for j in range(n):
        if matrix[0][j] == 1:
            break
        num_ways_matrix[0][j] = 1

    # same for first column

    for i in range(m):
        if matrix[i][0] == 1:
            break
        num_ways_matrix[i][0] = 1


    # now we loop through the array and add the top and left elems value to current val

    for i in range(1, m):
        for j in range(1, n):
            from_top = num_ways_matrix[i - 1][j] if matrix[i - 1][j] != 1 else 0
            from_left = num_ways_matrix[i][j - 1] if matrix[i][j - 1] != 1 else 0

            num_ways_matrix[i][j] = from_top + from_left

    return num_ways_matrix[-1][-1]



test = [[0, 0, 1],
        [0, 0, 1],
        [1, 0, 0]]

print(find_num_paths(test))
print(given_solution(test))
