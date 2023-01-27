# list comprehension
[<map exp> for <name> in <iter exp>]

odds = [1, 3, 5, 7, 9]
evens = [(num + 1) for num in odds]

[<map exp> for <name> in <iter exp> if <filter exp>]

temps = [60, 65, 71, 67, 77, 89]
hot = [temp for temp in temps if temp > 70]

#exercise: frontloaded
def front(s, f):
    """Return S but with elements chosen by F at the front.

    >>> front(range(10), lambda x: x % 2 == 1)  # odds in front
    [1, 3, 5, 7, 9, 0, 2, 4, 6, 8]
    """
    f_list = [i for i in s if f(s)]
    b_list = [i for i in s if not f(s)]
    return f_list+b_list


digits = [1,2,3]

# getitem(digits,2) 等价于 digits[2]

"""
>>> [1,2] in [3,[1,2],4]
True
>>> [1,2] in [3,[[1,2]],4]
False
"""