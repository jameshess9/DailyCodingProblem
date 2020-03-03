# given a list of ints and a goal number k return the contiguous elems of the list that sum to k
# ex 1, 2, 3, 4, 5 and K = 9 return 2,3,4 bc they are in a row

# naive solution for every number in the list we check and see if thats the beginning of the right chain


def find_cont_sum(numbers, k):
    for i in range(len(numbers)):
        potential_chain = []
        potential_chain.append(numbers[i])
        chain_value = numbers[i]

        for j in range(i + 1, len(numbers)):
            if chain_value == k:
                return potential_chain
            elif chain_value > k:
                break
            else:
                potential_chain.append(numbers[j])
                chain_value += numbers[j]

# so we know that if the solution is required to be so every time we reach a new elem we are going to add the right elem
# and then if we go over we will have to subtract the lower elems
# this code wouldnt work in the situation where there is a chain that goes over k that is not the solution


def better_find_cont_sum(numbers, k):
    retVal = []
    retVal_total = 0
    numbers_index = 0

    while retVal_total < k:
        retVal.append(numbers[numbers_index])
        retVal_total += numbers[numbers_index]
        numbers_index += 1

    while retVal_total > k:
        removed_elem = retVal.pop(0)
        retVal_total -= removed_elem

    if retVal_total == k:
        return retVal
    else:
        return []


numbers = [1, 2, 3, 4, 5]
test_k = 9
print(better_find_cont_sum(numbers, test_k))
