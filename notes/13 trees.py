# Tree: Implementation
def tree(label, branches=[]):   #by default, the branch of the tree is an empty list.
    for branch in branches:
        assert is_tree(branch), 'branches must be trees'
    return [label] + list(branches)   # creates a list from a sequence of branches

def label(tree):
    return tree[0]

def branches(tree):
    return tree[1:]

def is_tree(tree):
    if type(tree) != list or len(tree) < 1:   # A tree must be a list and has at least one element.
        return False
    for branch in branches(tree):  # to verify that all branches are also trees.
        if not is_tree(branch):
            return False
    return True

def is_leaf(tree):
    return not branches(tree)    # to check that the branches are empty.


def fib_tree(n):
    if n <= 1:   #just a leaf
        return tree(n)
    else:
        left, right = fib_tree(n-2), fib_tree(n-1)
        return tree(label(left)+label(right),[left, right])


# Tree Processing Uses Recursion
def count_leaves(t):
    """Count the leaves of a tree."""
    if is_leaf(t):
        return 1
    else:
        return sum([count_leaves(branch) for branch in branches(t)])


"""
If you sum a list of lists, you get a list containing the elements of those lists.
>>> sum([[1], [2,4], []])
[1,2,4]
>>> sum([[[1]], [2]], [])
[[1], 2]
"""

def leaves(tree):
    """Return a list containing the leaf labels of tree."""
    if is_leaf(tree):
        return [label(tree)]
    else:
        return sum([leaves(b) for b in branches(tree)], []) # The empty list is to make sure that the argument of sum is a list of lists.


#Creating Trees
def increment_leaves(t):
    """Return a tree like t but with leaf labels incremented."""
    if is_leaf(t):
        return tree(label(t)+1)
    else:
        bs = [increment_leaves(b) for b in branches(t)]
        return tree(label(t), bs)


# Example: Printing Trees
def print_tree(t, indent=0):# The indentation level of a label corresponds to its depth in the tree.
    print(' '*indent + str(label(t)))
    for b in branches(t):
        print_tree(b, indent+1)


# Example: Summing Paths
def print_sums(t, so_far):
    so_far += label(t)
    if is_leaf(t):
        return so_far
    else:
        for b in branches(t):
            print_sums(b, so_far)

# Example: Counting Paths
def count_paths(t, total):
    """Return the number of paths from the root to any node in tree t
    for which the labels along the path sum to total.
    """
    if label(t) == total:
        found = 1
    else:
        found = 0
    return found + sum([count_paths(b,total-label(t)) for b in branches(t)])


# Height 
def height(t):
    """Return the height of a tree.

    >>> t = tree(3, [tree(5, [tree(1)]), tree(2)])
    >>> height(t)
    2
    >>> t = tree(3, [tree(1), tree(2, [tree(5, [tree(6)]), tree(1)])])
    >>> height(t)
    3
    """
    "*** YOUR CODE HERE ***"
    if is_leaf(t):
        return 0
    return 1+ max([height(b) for b in branches(t)])


# Exercise: Maximum Path Sum
def max_path_sum(t):
    """Return the maximum path sum of the tree.

    >>> t = tree(1, [tree(5, [tree(1), tree(3)]), tree(10)])
    >>> max_path_sum(t)
    11
    """
    "*** YOUR CODE HERE ***"
    def helper(t, so_far):
        so_far += label(t)
        if is_leaf(t):
            return so_far
        else:
            return label(t)+max([max_path_sum(b) for b in branches(t)])   
    return helper(t, 0)


# Exercise
def find_path(t, x):
    """takes in a tree and a value x and returns a list containing the nodes along the path 
        required to get from the root of the tree to a node containing x.
    >>> t = tree(2, [tree(7, [tree(3), tree(6, [tree(5), tree(11)])] ), tree(15)])
    >>> find_path(t, 5)
    [2, 7, 6, 5]
    >>> find_path(t, 10)  # returns None
    """
    if label(t) == x:
        return [label(t)]
    for b in branches(t):
        path = find_path(b, x)
        if path:
            return [label(t)] + path

#count palindrome
"""
A palindrome is a word or a phrase that is the same 
 whether you read it backward or forward, for example, the word "refer."
>>> word = "hello"
>>> word_reverse = word[::-1]
>>> word_reverse
"olleh"
"""

# trees: preorder 树的前序遍历


def preorder(t):
    """Return a list of the entries in this tree in the order that they
    would be visited by a preorder traversal (see problem description).

    >>> numbers = tree(1, [tree(2), tree(3, [tree(4), tree(5)]), tree(6, [tree(7)])])
    >>> preorder(numbers)
    [1, 2, 3, 4, 5, 6, 7]
    >>> preorder(tree(2, [tree(4, [tree(6)])]))
    [2, 4, 6]
    """
    "*** YOUR CODE HERE ***"
    if is_leaf(t):
        return [label(t)]
    else:
        result = [label(t)]
        for b in branches(t):
            result.extend(preorder(b))
        return result

