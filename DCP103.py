# given a stirng and a set of characters find the smallest substring with all of the characters
# naive solution is to go through every char in the string and as soon as you find one of your chars
# you consider that the start of a chain and continue to go until you find all the characters
# return the smallest set

def find_smallest_substring(string, chars):
    shortest = ""
    shortest_size = 0


    for i in range(len(string)):
        if string[i] in chars:
            # so we try to make a substring of this
            possible_shortest = ""
            possible_shortest += string[i]
            possible_shortest_size = 1
            print(possible_shortest)



    return "a"


test = "figehaeci"
test_Set = {'a', 'e', 'i'}
print(find_smallest_substring(test,test_Set))