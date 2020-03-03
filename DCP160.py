from math import inf


# given a tree where each edge has a weight return the longest path in the tree
# i initially solved this probably incorrectly solving for the longest path from the root to the leaf nodes
# the problem description can start from a child to another child and never go to root
# thus I only have the given solution for this problem because I looked at the answer before solving


class Node:
    def __init__(self, val, children=[]):
        self.val = val
        self.children = children


def longest_path(root):
    height, path = longest_height_and_path(root)
    return path

# so when we start from root we basically have 2 options
# option 1 -> our path goes through root so the path is equal to one child + root + other child
# this is because our path will go from the one child into the root back into the other child
# option 2 -> our path does not go through root so the path is the maximum between the two children

# so we look into our child nodes paths and store the longest seen path so far
# then we take the max between adding 2 children including our current node or just using a child nodes path
def longest_height_and_path(root):
    longest_path_so_far = -inf
    highest, second_highest = 0, 0

    # this loop actually includes our base case
    # our base case is when a node has no children
    for length, child in root.children:
        # for each child we look for the longest path of the child
        height, longest_path_length = longest_height_and_path(child)

        longest_path_so_far = max(longest_path_so_far, longest_path_length)

        if height + length > highest:
            highest, second_highest = height + length, highest
        elif height + length > second_highest:
            second_highest = height + length

    # longest_path_so_far is equal to the highest path we have seen that does not include the root node
    # highest + second_highest is the highest and second highest path length of our children
    # we add that together to include root to get the longest path that includes root
    return highest, max(longest_path_so_far, highest + second_highest)