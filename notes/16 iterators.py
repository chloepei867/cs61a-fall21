# Iterators
"""
** Two separate iterators can track two different positions in the same sequence. 
However, two names for the same iterator will share a position, because they share the same value.

>>> r = range(3, 13)
>>> s = iter(r)  # 1st iterator over r
>>> next(s)
3
>>> next(s)
4
>>> t = iter(r)  # 2nd iterator over r
>>> next(t)
3
>>> next(t)
4
>>> u = t        # Alternate name for the 2nd iterator
>>> next(u)
5
>>> next(u)
6

>>> next(s)
5
>>> next(t)      #重点是这里！！ t和u是一个东西,而不是相同的两个东西
7

** Calling iter on an iterator will return that iterator, not a copy.

>>> v = iter(t)  # Another alterante name for the 2nd iterator
>>> next(v)      
8
>>> next(u)
9
>>> next(t)
10

"""

"""
>>> t = [[1, 2], 4, 6, 7]
>>> s = iter(t)
>>> next(s)
[1, 2]
>>> next(s)
4
>>> list(s)
[6, 7]     # Iterators are mutable.Once the iterator moves forward, 
             it won't return the values that came before.
             Here, we have already used up the elements of [1, 2] and 4.

>>> next(s)
StopIteration   #此时元素已经用完了,不能在迭代了.

"""


# Dictionary Iteration
"""
A dictionary, its keys, its values, and its items are all iterable values.
 The order of items in a dictionary is the order in which they were added.

>>> d = {'one': 1,'two': 2, 'three': 3}
>>> d['zero'] = 0
>>> k = iter(d.keys())   # or iter(d)
>>> next(k)
'one'
>>> next(k)
'two'
>>> v = iter(d.values())
>>> next(v)
1
>>> next(v)
2
>>> i = iter(d.items())
>>> next(i)
('one', 1)             # tuples
"""

# If a dictionary changes in structure because a key is added or removed, 
 # then all iterators become invalid and future iterators 
 # may exhibit arbitrary changes to the order their contents. 
 # On the other hand, changing the value of an existing key does not change the order of the contents 
 # or invalidate iterators.

# for statement
"""
如果在for statement中使用iterator, 还是可以go through all of the elements until the end,
 but that will advance the iterator so that it cannot be used again.
"""


# Built-in Iterator Functions
"""
如map、filter等,take as arguments iterable values and return iterators,
接着再使用next()时才会开始进行迭代

>>> def double_and_print(x):
        print('***', x, '=>', 2*x, '***')
        return 2*x
>>> s = range(3, 7)
>>> doubled = map(double_and_print, s)  # double_and_print not yet called
>>> next(doubled)                       # double_and_print called once
*** 3 => 6 ***
6
>>> next(doubled)                       # double_and_print called again
*** 4 => 8 ***
8
>>> list(doubled)                       # double_and_print called twice more
*** 5 => 10 ***
*** 6 => 12 ***
[10, 12]

"""

# The Zip Function
"""
>>> list(zip([1, 2], [3, 4]))
[(1, 3), (2, 4)]

>>> list(zip([1, 2], [3, 4,5]))
[(1, 3), (2, 4)]

$$ more than two iterables can be passed to zip.
>>> list(zip([1, 2], [3, 4, 5], [6, 7]))
[(1, 3, 6), (2, 4, 7)]
"""

# example
def palindrome(s):
    """Return whether s is the same backward and forward.
    >>> palindrome([3,1,4,1,5])
    False
    >>> palindrome([3,1,4,1,3])
    True
    >>> palindrome('seveneves')
    True
    """
    return all([a==b for a, b in zip(s,reversed(s))])


def count_occurrences(t, n, x):
    """Return the number of times that x appears in the first n elements of iterator t.

    >>> s = iter([10, 9, 10, 9, 9, 10, 8, 8, 8, 7])
    >>> count_occurrences(s, 10, 9)
    3
    >>> s2 = iter([10, 9, 10, 9, 9, 10, 8, 8, 8, 7])
    >>> count_occurrences(s2, 3, 10)
    2
    >>> s = iter([3, 2, 2, 2, 1, 2, 1, 4, 4, 5, 5, 5])
    >>> count_occurrences(s, 1, 3)
    1
    >>> count_occurrences(s, 4, 2)
    3
    >>> next(s)
    2
    >>> s2 = iter([4, 1, 6, 6, 7, 7, 8, 8, 2, 2, 2, 5])
    >>> count_occurrences(s2, 6, 6)
    2
    """
    return sum([next(t) == x for i in range(n)])


def repeated(t, k):
    """Return the first value in iterator T that appears K times in a row.
    Iterate through the items such that if the same iterator is passed into
    the function twice, it continues in the second call at the point it left
    off in the first.

    >>> s = iter([10, 9, 10, 9, 9, 10, 8, 8, 8, 7])
    >>> repeated(s, 2)
    9
    >>> s2 = iter([10, 9, 10, 9, 9, 10, 8, 8, 8, 7])
    >>> repeated(s2, 3)
    8
    >>> s = iter([3, 2, 2, 2, 1, 2, 1, 4, 4, 5, 5, 5])
    >>> repeated(s, 3)
    2
    >>> repeated(s, 3)
    5
    >>> s2 = iter([4, 1, 6, 6, 7, 7, 8, 8, 2, 2, 2, 5])
    >>> repeated(s2, 3)
    2
    """
    assert k > 1
    "*** YOUR CODE HERE ***"
    count = 0
    number_sofar = None
    try:
        while True:
            temp_number = next(t)
            if temp_number == number_sofar:
                count += 1
            else:
                count = 1
                number_sofar = temp_number
            if count == k:
                return number_sofar
    except Exception as e:
        print('DEBUG:', e)

