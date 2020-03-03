# finds the most common number in an array
# req for most common is greater than math.floor(size/2)
# the majority elem will always be added more times than it will be subtracted so its running sum for
# times seen vs times not seen will always end positive
# the majority elem is the only elem with this property so it will always return the majority elem
# O(n) runtime and O(1) space
def find_most_common_number(array):
    cur_highest = array[0]
    num_highest = 1
    for i in range(1, len(array)):
        if array[i] == cur_highest:
            num_highest += 1
        else:
            num_highest -= 1
            if num_highest == 0:
                cur_highest = array[i]
                num_highest = 1
    return cur_highest

    return cur_highest


# this solution follows the same algorithm as what I did with syntax improvements to improve readability

def given_solution(array):
    # in the given solution we enumerate instead of saving index
    for i, e in enumerate(array):
        # since we add the i == 0 inclusion we don't have to start off by saving the first elem and starting
        # at array + 1
        if i == 0 or count == 0:
            majority = e
            count = 1
        elif majority == e:
            count += 1
        else:
            count -= 1
    return majority


test = [1, 1, 3, 1, 3, 1, 3]
print(find_most_common_number(test))
print(given_solution(test))
