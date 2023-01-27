#append()和extend()的区别
"""
>>> s = [2, 3]
>>> t = [5, 6]
>>> s.append(t)
[2,3,[5,6]]
>>> s.append(4)
[2,3,4]

>>> s = [2, 3]
>>> t = [5, 6]
>>> s.extend(t)
[2,3,5,6]
>>> s.extend(4)
Error. 4 is not an iterable!

"""

# Example: strings
"""
>>> s = 'Hello'
>>> s.upper()
'HELLO'
>>> s.swapcase()
'hELLO'
>>> s
'Hello'      #可以看到s本身没有改变。
             # each of methods invocations has returned a new string
             # based on the old string. 
"""


# Mutation Operations
"""
All names that refer to the same object are affected by a mutation.
Only objects of mutable types can change: lists & dictionaries
"""

# Mutation can happen within a function call
def mystery(s):
    s.pop()
    s.pop()

"""
>>> list = [1,2,3,4]
>>> len(list)
4
>>> mystery(list)
>>> len(list)
2
"""
#=============================================================
def another_mystery(x):
    x.pop()
    x.pop()

"""
>>> x = [1,2,3,4]
>>> len(x)
4
>>> another_mystery()   # No arguments!
>>> len(x)
2
"""


# tuples: anything separated by commas is evaluated as a tuple.圆括号非必须
"""
>>> tuple([3, 4, 5])
(3, 4, 5)
>>> 2,   
(2,)  # a tuple with only one element. The comman is necessary.
>>> (2,)
(2,)
>>> (3, 4) + (5, 6)
(3, 4, 5, 6)
>>> 5 in (3,4,5)
True

"""

# the value of an expression can change because of changes in names
 # or objects.

#name change:
"""
>>> x = 2
>>> x + x
4

>>> x = 3   # numbers are immutable. The name is changed. 
>>> x + x
6
"""

#object mutation
"""
>>> x = [1, 2]
>>> x + x
[1,2,1,2]
>>> x.append(3)    # the object is changed.
>>> x + x
[1,2,3,1,2,3]    

"""


# a immutable sequence may still change 
 # if it contains a mutable value as an element.

"""
>>> s = ([1,2],3)
>>> s[0] = 4   
Error
>>> s[0][0] = 4
>>> s
([4,2],3)
"""


# Sameness and Change
"""
>>> a = [10]
>>> b = a
>>> a == b
True
>>> a.append(20)
>>> a == b
True
"""

"""
>>> a = [10]   #a and b are two lists that have the same contents, but are different.
>>> b = [10]
>>> a == b
True
>>> a.append(20)
>>> a == b
False
"""

# Identity Operators
"""
<exp0> is <exp1>
evaluates to True if both exp0 and exp1 evaluate to the same object

<exp0> == <exp1>
evaluates to True if both exp0 and exp1 evaluate to equal values.

"""
# idential objects are always equal values, but not the other way around.
"""
>>> a = [10]
>>> b = [10]
>>> a == b
True
>>> a is b
False
"""


# Mutable default arguments: DANGEROUS!!
"""
>>> def f(s=[]):
        s.append(5)
        return len(s)

>>> f()
1
>>> f()
2
>>> f()  # Each time the function is called, s is bound to the same value.
         # That's how default argument work.
3

"""


# Mutable Functions
def make_withdraw_account(initial):
    balance = [initial]
    
    def withdraw(amount):  # this function doesn't reassign any name within the parent
                           # instead, it changes the value of balance itself.
        if balance[0] - amount < 0:
            return 'Insufficient funds'
        balance[0] -= amount
        return balance[0]
    
    return withdraw