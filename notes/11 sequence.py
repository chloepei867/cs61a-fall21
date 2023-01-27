from math import log10


def sum_nums(nums):
    """
    Returns the sum of the numbers in NUMS.
    >>> sum_nums([6, 24, 1984])
    2014
    >>> sum_nums([-32, 0, 32])
    0
    """ 
    if (nums == []):
        return 0
    else:
        return nums[0] + sum_nums( nums[1:] )


# recursively reversing a string
def reverse(s):
    """Returns a string with the letters of S
    in the inverse order.
    >>> reverse('ward')
    'draw'
    """
    if len(s) == 1:
        return s
    else:
        return reverse(s[1:]) + s[0]

# exercise: reversing a number


def reverse(n):
    """Returns N with the digits reversed.
    >>> reverse_digits(123)
    321
    """
    if n < 10:
        return n
    else:
        all_but_last, last = n//10, n%10
        return last*10**int(log10(all_but_last)+1) + reverse(all_but_last)

# key function
coords = [ [37, -144], [-22, -115], [56, -163] ]
max(coords, key=lambda coord: coord[0])  # [56, -163]
min(coords, key=lambda coord: coord[0])  # [-22, -115]

gymnasts = [ ["Brittany", 9.15, 9.4, 9.3, 9.2],
    ["Lea", 9, 8.8, 9.1, 9.5],
    ["Maya", 9.2, 8.7, 9.2, 8.8] ]
min(gymnasts, key=lambda scores: min(scores[1:]))    # ["Maya", ...]
max(gymnasts, key=lambda scores: sum(scores[1:], 0)) # ["Brittany", ...]


#The Closure Property of Data Types
"""
a method for combining data values satisfies the closure property if:
the resule of combination can itself be combined using the same method
ex: Lists can contain lists as elements.
"""


"""
>>> sum([3,4,5])
12
>>> sum([3,4,5],4)
16
>>> sum([[2,3],[4]],[])
[2,3,4]
>>> sum([[2,3],[4]])
Error
>>> [] + [2,3] +[4]
[2,3,4]
"""

#all(iterable) → bool
"""
Return True if bool(x) is True for all values x in the iterable.
If the iterable is empty, return True
>>> [x<5 for x in range(5)]
[True,True,True,True,True]

>>> all([x<5 for x in range(5)])
True

>>> all(range(5))
False
"""

# zip的使用方法
"""
>>> a = [1,2,3]
>>> b = [4,5,6]
>>> c = [4,5,6,7,8]
>>> zipped = zip(a,b)     # 返回一个对象
>>> zipped
<zip object at 0x103abc288>
>>> list(zipped)  # list() 转换为列表
[(1, 4), (2, 5), (3, 6)]
>>> list(zip(a,c))              # 元素个数与最短的列表一致
[(1, 4), (2, 5), (3, 6)]

>>> a1, a2 = zip(*zip(a,b))          # 与 zip 相反，zip(*) 可理解为解压，返回二维矩阵式
>>> list(a1)
[1, 2, 3]
>>> list(a2)
[4, 5, 6]
"""


