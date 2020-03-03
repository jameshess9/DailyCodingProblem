# given a positive integer n find the smallest number of squared integers which sum up to n
# for example given n = 13 return 2 b/c 3^2 + 2^2 = 9 + 4 = 13
# n = 27 return 3 b/c 3^2 + 3^2 + 3^2 = 9 + 9 + 9 = 27
import math


def find_parts_rec(total, num_left):
    # the first square
    square = 1
    square_value = 1
    if num_left == 2:
        while total - square_value >= 0:
            amount_left = total - square_value
            root = math.sqrt(amount_left)
            # if root % 1 == 0 there is no decimal therefore it is a perfect square
            if root % 1 == 0:
                return True
            else:
                square += 1
                square_value = square ** 2
        return False
    else:
        while total - square_value >= 0:
            amount_left = total - square_value
            if find_parts_rec(amount_left, num_left - 1):
                return True
            else:
                square += 1
                square_value = square ** 2
        return False


def find_parts(int):
    retVal = 0
    count = 1
    while retVal == 0:
        count += 1
        # we start from 2 and keep trying until we get an answer
        possible = find_parts_rec(int, count)
        if possible:
            retVal = count
        else:
            continue
    return retVal


print(find_parts(27))
