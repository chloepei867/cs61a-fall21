
# ------------------------Lists-------------------------------------------------------
# Lists in environment diagram (详见图24-1)
 # addition & slicing: create new lists containing existing elements.
"""
>>> s = [2, 3]
>>> t = [5, 6]
a = s + [t]
b = a[1:]
a[1] = 9
b[1][1] = 0  # A and B all contained T, so this change to T affects A and B as well.

s → [2, 3]
t → [5, 0]
a → [2, 9, [5, 0]]
b → [3, [5, 0]]

"""

# ------------------------objects------------------------------------------------------
"""
Instance attributes are found before class attributes; 
class attributes are inherited
(详见24-3)
"""

# ------------------------iterables & iterators----------------------------------------
def smallest_abv(s):
    """take a list and return the indices of all elements that
    have the smallest absolute value.
    >>> s = [-4, -3, -2, 3, 2, 4]
    >>> smallest_abv(s)
    [2, 4]
    """
    min_abs = min(map(abs, s))
    return [i for i, x in enumerate(s) if x==min_abs]
    # return [i for i in range(len(s)) if abs(s[i]) == min_abs]



def largest_sum(s):
    """
    take a list and return the largest sum of two adjacent elements.
    >>> s = [-4, -3, -2, 3, 2, 4] 
    >>> largest_sum(s)
    6
    """
    if len(s) == 2:
        return sum(s)
    return max(s[0]+s[1],largest_sum(s[1:]))
    # solution 2:
     # return max([s[i] + s[i+1] for i in range(len(s)-1)])
    
    # solution 3:
     # return max([a+b for a, b in zip(s[:-1], s[1:])])



def other_elements(s):
    """
    take a list s, and return True if every element equals some other elements in s.
    >>> s = [4, 3, 2, 3, 2, 4] 
    >>> other_element(s)
    True
    >>> t = [-4, -3, -2, 3, 2, 4] 
    >>> other_elements(t)
    False
    """
    for i in s:
        s_without = s.remove(i)
        if not (i in s_without):
            return False
    return True

    # solution 2:
    return all([s[i] in s[:i]+s[i+1:] for i in range(len(s))])
    # solution 3:
    return min([sum(1 for y in s if y == x) for x in s]) > 1
    # solution 4:
    return all(map(lambda x: s.count(x)>1, s))


def digit_dict(s):
    """
    map each digit d to the lists of elemenets in s that end with d.
    >>> >>> digit_dict([5, 8, 13, 21, 34, 55, 89])
    {1: [21], 3: [13], 4: [34], 5: [5, 55], 8: [8], 9: [89]}
    """
    return {i: [x for x in s if x%10 ==i] for i in range(10) if any([x%10 ==i for x in s])}
    
    # solution 2:
    last_digits = list(map(lambda x: x%10, s))
    return {i: [x for x in s if x%10 == i] for i in range(10) if i in last_digits}
    

# ------------------------Linked Lists-------------------------------------------------
def ordered(s, key=lambda x: x):
    """
    Is Link s ordered?
    >>> ordered(Link(1, Link(3, Link(4))))
    True
    >>> ordered(Link(1, Link(4, Link(3))))
    False
    >>> ordered(Link(1, Link(-3, Link(4))))
    False
    >>> ordered(Link(1, Link(-3, Link(4))), key=abs)
    True
    >>> ordered(Link(-4, Link(-1, Link(3))))
    True
    >>> ordered(Link(-4, Link(-1, Link(3))), key=abs)
    False
    """
    if s is Link.empty or s.rest is Link.empty:
        return True
    elif key(s.first) > key(s.rest.first):
        return False
    else:
        return ordered(s.rest)
    

def merge(s, t):
    """Return a sorted Link containing the elements of sorted s & t.
    >>> a = Link(1, Link(5))
    >>> b = Link(1, Link(4))
    >>> merge(a, b)
    Link(1, Link(1, Link(4, Link(5))))
    >>> a
    Link(1, Link(5))
    >>> b
    Link(1, Link(4))
    """
    if s is Link.empty:
        return t
    elif t is Link.empty:
        return s
    elif s.first <= t.first:
        return Link(s.first, merge(s.rest, t))
    else:
        return Link(t.first, merge(s, t.rest))



def merge_in_place(s, t):
    """
    Return a sorted Link containing the elements of sorted s & t.
    >>> a = Link(1, Link(5))
    >>> b = Link(1, Link(4))
    >>> merge_in_place(a, b)
    Link(1, Link(1, Link(4, Link(5))))
    >>> a
    Link(1, Link(1, Link(4, Link(5))))
    >>> b
    Link(1, Link(4, Link(5)))
    """
    if s is Link.empty:
        return t
    elif t is Link.empty:
        return s
    elif s.first <= t.first:
        s.rest = merge_in_place(s.rest, t)
        return s
    else:
        t.rest = merge_in_place(s, t.rest)
        return t
























class Link:
    """A linked list.

    >>> Link(1, Link(2, Link(3)))
    Link(1, Link(2, Link(3)))
    >>> s = Link(1, Link(Link(2, Link(3)), Link(4)))
    >>> s
    Link(1, Link(Link(2, Link(3)), Link(4)))
    >>> print(s)
    <1 <2 3> 4>
    """

    empty = ()

    def __init__(self, first, rest=empty):
        assert rest is Link.empty or isinstance(rest, Link)
        self.first = first
        self.rest = rest

    def __repr__(self):
        if self.rest:
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