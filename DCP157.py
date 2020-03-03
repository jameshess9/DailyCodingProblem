# given a string determine whether any permutation of it is a palindrome

# what we do here is create an array and then for each char we check if it's in that array
# if the char is in the array we remove it, and if it's not in the array we append it
# basically a palindrome you need 2 equal letters on each side to make it a palindrome
# so if this list ends up with 0 elems at the end it is a palindrome
# we allow the array to go up to 1 because of the one "pivot" char that can sit in the middle
def is_palindrome(strng):
    arr = []
    for char in strng:
        if char in arr:
            arr.remove(char)
        else:
            arr.append(char)

    # if len == 0 then we have a matching char for each char
    # elif len == 1 and it is an odd length word that one char sits in the middle
    if len(arr) == 0 or (len(arr) == 1 and len(strng) % 2 == 1):
        return True
    else:
        return False


print(is_palindrome("racecar"))