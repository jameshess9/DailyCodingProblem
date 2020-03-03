# given a string return the first recurring character

# naive solution is to create a list and keep iterating until the current char is in the string

def naive_solution(string):
    chars = []

    for char in string:
        if char in chars:
            return char
        else:
            chars.append(char)
    return None


# this solution is better because its bounded by the amount of characters
# at each iteration it checks if we have already seen that character and if we have we continue
# O(len(string) * 26 len(string)) -> n^2 runtime compared to the !n


def index_solution(string):
    seen_letters = []

    min_index = None
    ret_val = None
    # so basically for each character we are going to store the index of the next time the char is seen
    for i in range(len(string)):
        if not string[i] in seen_letters:
            seen_letters.append(string[i])
            for j in range(i + 1, len(string)):
                if string[j] == string[i]:
                    if min_index is None or j < min_index:
                        min_index = j
                        ret_val = string[i]
    return ret_val

# easiest most simple solution


def dict_solution(string):
    dict = {}

    for char in string:
        if char in dict:
            return char
        else:
            dict[char] = 0
    return None


test = "jiaurtnbijhsrntyabiounadjirehwafonciurheguivahnmiuorgvhnmzerlijrhmvklzndmlkfvbmhkjlfedbaeaiufov"
print(naive_solution(test))
print(dict_solution(test))
print(index_solution(test))
