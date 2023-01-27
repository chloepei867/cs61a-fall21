from typing import List
"""
Objects can have other objects as attribute values. 
When an object of some class has an attribute value of that same class, it is a recursive object.
"""

# Linked List Class
class Link:
    empty = ()
    def __init__(self, first, rest= empty):
        assert rest is Link.empty or isinstance(rest, Link)
        self.first = first
        self.rest = rest

    def __repr__(self):
        if self.first:
            rest_repr = ', ' + repr(self.rest)
        else:
            rest_repr = ''
        return 'Link(' + repr(self.first) + rest_repr + ')'

              
    def __str__(self):
        string = '<'
        while self.rest is not Link.empty:
            string += str(self.first) + ' '
            self = self.rest
        return string + str(self.first) + '>'


# Linked List Processing: Recursion
 # Example: range, map, and filter for linked lists  #these functions do
 # not operate on linked list(user-defined).

def square(x):
    return x * x

def odd(x):
    return x % 2 == 1

def range_link(start, end):
    """Return a Link containing consecutive integers from start to end.
    >>> range_link(3,6)
    Link(3, Link(4, Link(5)))
    """
    if start >= end:
        return Link.empty
    else:
        return Link(start, range_link(start+1, end))

def map_link(f, s):
    """
    Return a Link that contains f(x) for each x in Link s.
    >>> map_link(square, range_link(3, 6))
    Link(9, Link(16, Link(25)))
    """
    if s is Link.empty:
        return s
    else:
        return Link(f(s.first), map_link(s.rest))

def filter_link(f, s):
    """
    Return a Link that contains only the elements x of Link s for which
    f(x) is a true value.
    >>> filter_link(odd, range_link(3, 6))
    Link(3, Link(5))
    """
    if s is Link.empty:
        return s
    else:
        filtered_rest = filter_link(f, s.rest)
        if f(s.first):
            return Link(s.first, filtered_rest)
        else:
            return filtered_rest


# linked Lists Mutation
 # Adding to a Set Represented as an Ordered List

def add(s, v):
    """Add v to an ordered Link list s with no repeats, 
    return modified s.
    >>> s = Link(1, Link(3, Link(5)))
    >>> add(s, 0)
    Link(0, Link(1, Link(3, Link(5))))
    >>> add(s, 3)
    Link(0, Link(1, Link(3, Link(5))))
    >>> add(s, 4)
    Link(0, Link(1, Link(3, Link(4, Link(5)))))
    >>> add(s, 6)
    Link(0, Link(1, Link(3, Link(4, Link(5, Link(6))))))
    """
    assert s is not Link.empty
    if s.first > v:
        s.first, s.rest = v , Link(s.first, s.rest)     
    elif s.first < v and s.rest is Link.empty:  # ???
        s.rest = Link(v)
    elif s.first < v:
        s.rest = add(s.rest, v)
    return s


# Tree Class
class Tree:   # constructor
    def __init__(self, label, branches=[]):
        self.label = label
        for branch in branches:
            assert isinstance(branch, Tree)
        self.branches = list(branches)

    def __repr__(self):
        if self.branches:
            branch_str = ', ' + repr(self.branches)
        else:
            branch_str = ''
        return 'Tree({0}{1})'.format(repr(self.label), branch_str)
    
    def __str__(self):
        return '\n'.join(self.indented())

    def indented(self):
        lines = []
        for b in self.branches:
            for line in b.indented():
                lines.append(' ' + line)
        return [str(self.label)] + lines

    def is_leaf(self):
        return not self.branches

def leaves(t):
    """return a list of leaf labels in Tree T."""
    if t.is_leaf():
        return [t.label]
    else:
        all_leaves = []
        for b in t.branches:
            all_leaves.extend(leaves(b))
        return all_leaves

def height(t):
    """return the number of transitions in the longest path in T.""" 
    if t.is_leaf():
        return 0
    return 1 + max([height(b) for b in t.branches])


# Tree Mutation: Pruning Trees
def prune(t, n):
    """Prune all subtrees whose label is n."""
    t.branches = [b for b in t.branches if b.label != n]
    for b in t.branches:
        prune(b, n)

# lab08-Q5
def cumulative_mul(t):
    """Mutates t so that each node's label becomes the product of all labels in
    the corresponding subtree rooted at t.

    >>> t = Tree(1, [Tree(3, [Tree(5)]), Tree(7)])
    >>> cumulative_mul(t)
    >>> t
    Tree(105, [Tree(15, [Tree(5)]), Tree(7)])
    """
    "*** YOUR CODE HERE ***"
    mul = 1
    for b in t.branches:
      cumulative_mul(b)
      mul *= b.label
    t.label *= mul

# lab08-Q6
def add_d_leaves(t, v):
    """Add d leaves containing v to each node at every depth d.

    >>> t_one_to_four = Tree(1, [Tree(2), Tree(3, [Tree(4)])])
    >>> print(t_one_to_four)
    1
      2
      3
        4
    >>> add_d_leaves(t_one_to_four, 5)
    >>> print(t_one_to_four)
    1
      2
        5
      3
        4
          5
          5
        5

    >>> t1 = Tree(1, [Tree(3)])
    >>> add_d_leaves(t1, 4)
    >>> t1
    Tree(1, [Tree(3, [Tree(4)])])
    >>> t2 = Tree(2, [Tree(5), Tree(6)])
    >>> t3 = Tree(3, [t1, Tree(0), t2])
    >>> print(t3)
    3
      1
        3
          4
      0
      2
        5
        6
    >>> add_d_leaves(t3, 10)
    >>> print(t3)
    3
      1
        3
          4
            10
            10
            10
          10
          10
        10
      0
        10
      2
        5
          10
          10
        6
          10
          10
        10
    """
    "*** YOUR CODE HERE ***"
    def helper(tree, depth):
        for b in tree.branches:
            helper(b, depth+1)
        tree.branches.extend([Tree(v) for _ in range(depth)])
    return helper(t, 0)


# discussion 08- Q4: Multiply Links
def multiply_lnks(lst_of_lnks):
    """
    >>> a = Link(2, Link(3, Link(5)))
    >>> b = Link(6, Link(4, Link(2)))
    >>> c = Link(4, Link(1, Link(0, Link(2))))
    >>> p = multiply_lnks([a, b, c])
    >>> p.first
    48
    >>> p.rest.first
    12
    >>> p.rest.rest.rest is Link.empty
    True
    """
    # Implementation Note: you might not need all lines in this skeleton code
    mul = 1
    for link in lst_of_lnks:
        if link is Link.empty:
            return Link.empty
        mul *= link.first
    link_rest = [link.rest for link in lst_of_lnks]
    return Link(mul, multiply_lnks(link_rest))


# discussion 08- Q5: Flip Two 链表成对节点交换
def flip_two(s):
    """
    >>> one_lnk = Link(1)
    >>> flip_two(one_lnk)
    >>> one_lnk
    Link(1)
    >>> lnk = Link(1, Link(2, Link(3, Link(4, Link(5)))))
    >>> flip_two(lnk)
    >>> lnk
    Link(2, Link(1, Link(4, Link(3, Link(5)))))
    """
    "*** YOUR CODE HERE ***"

    # For an extra challenge, try writing out an iterative approach as well below!
    "*** YOUR CODE HERE ***"
    if s.rest is Link.empty:
        return 
    s.first, s.rest.first = s.rest.first, s.first
    flip_two(s.rest.rest)

# discussion 08- Q7: Leaves
def leaves(t):
    """Returns a list of all the labels of the leaf nodes of the Tree t.
    >>> leaves(Tree(1))
    [1]
    >>> leaves(Tree(1, [Tree(2, [Tree(3)]), Tree(4)]))
    [3, 4]
    """
    "*** YOUR CODE HERE ***"
    res = []
    if t.is_leaf():   # ！！！不能漏了()
        return [t.label]
    else:
        for b in t.branches:
            res += leaves(b)
        return res

# discussion 08- Q8: Find Paths
def find_paths(t, entry):
    """
    >>> tree_ex = Tree(2, [Tree(7, [Tree(3), Tree(6, [Tree(5), Tree(11)])]), Tree(1, [Tree(5)])])
    >>> find_paths(tree_ex, 5)
    [[2, 7, 6, 5], [2, 1, 5]]
    >>> find_paths(tree_ex, 12)
    []
    """
    paths = []
    if t.label == entry:
        paths.append([t.label])
    for b in t.branches:
        path = find_paths(b, entry)
        for p in path:
            p = [t.label] + p
            paths.append(p)
    return paths



