from fractions import gcd     # greatest common divisor
# get()
"""
words = {
    "más": "more",
    "otro": "other",
    "agua": "water"
}
>>> words.get("agua")
water
>>> words.get("hello","你好")
你好
"""

# Dictionary rules
"""
// A key cannot be a list or dictionary (or any mutable type)
// All keys in a dictionary are distinct (there can only be one value per key)
// The values can be any type, however!
"""

# Dictionary iteration: keys are iterated over in the order they are first added.
"""
insects = {"spiders": 8, "centipedes": 100, "bees": 6}
for name in insects:
    print(insects[name])
打印结果 → 8 100 6
"""

# Dictionary comprehensions
"""
{key: value for <name> in <iter exp>}
>>> {x: x*x for x in range(3,6)}
{3: 9, 4: 16, 5: 25}
"""

# Exercise: Prune
def prune(d, keys):
    """Return a copy of D which only contains key/value pairs
    whose keys are also in KEYS.
    >>> prune({"a": 1, "b": 2, "c": 3, "d": 4}, ["a", "b", "c"])
    {'a': 1, 'b': 2, 'c': 3}
    """
    return {key: d[key] for key in keys}

# Exercise: Index
def index(keys, values, match):
    """Return a dictionary from keys k to a list of values v for which 
    match(k, v) is a true value.
    
    >>> index([7, 9, 11], range(30, 50), lambda k, v: v % k == 0)
    {7: [35, 42, 49], 9: [36, 45], 11: [33, 44]}
    """
    return {k:[v for v in values if match(k,v)] for k in keys}


#Data abstraction: a methodology by which functions enforce an abstraction barrier
#between representation and use.

#举例：Rational Numbers
"""
The functions below implement an abstract data type for rational numbers.
constructor:
rational(n, d) -- returns a rational number x
selector:
numer(x)       -- returns the numerator of x
denom(x)       -- returns the denominator of x
"""

# Rational Number Arithmetic Implementation


def mul_rational(x, y):
    return rational(numer(x)*numer(y), denom(x)*denom(y))


def add_rational(x, y):
    nx, ny = numer(x), numer(y)
    dx, dy = denom(x), denom(y)
    return rational(nx*dy+ny*dx, dx*dy)


def equal_rational(x, y):
    return numer(x)*denom(y) == numer(y)*denom(x)


# Representing Pair Using Lists
pair = [1, 2]

# unpacking a list
x, y = pair        # x = pair[0], y = pair[1]

"""
>>> from operator import getitem
>>> getitem(pair, 0)
1
"""

# Representing Rational Numbers


def rational(n, d):
    """Construct a rational number that represents n/d."""
    return [n, d]        # construct a list


def numer(x):
    return x[0]


def denom(x):
    return x[1]


# Reducing to the Lowest Terms


def rational(n, d):
    g = gcd(n, d)
    return [n//g, d//g]


# Abstraction Barriers
"""
Abstraction Barriers separate different parts of a program 
so that each part only needs to know so much about the rest of the program.
They allow you to make changes to one part of your program 
and have other parts take advantage of those changes 
without breaking in any way or creating inconsistencies.
"""


# Data Representations
"""
The purpose of maintaining abstraction barriers is 
so that you can change your data representation 
without having to rewrite your entire program.
"""


# Rational Data Abstraction Implemented as Functions
def rational(n, d):      # Constructor is a higher-order function
    def select(name):    # This function represents a rational number
        if name == 'n':
            return n
        elif name == 'd':
            return d
    return select


def numer(x):
    return x('n')


def denom(x):
    return x('d')