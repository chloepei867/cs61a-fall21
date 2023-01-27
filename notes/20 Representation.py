# string conversion
"""
str和repr的区别

The str is legible to humans.
The repr is legible to the Python interpreter.
The docstring for repr explains this property:
repr(object) -> string
"""

# the repr string for an object
#The result of calling repr on the value of an expression 
 # is what Python prints in an interactive session.
"""
>>> 12e12
12000000000000.0
>>> print(repr(12e12))
12000000000000.0
"""

# some objects do not have a simple Python-readable string.
"""
>>> repr(min)
'<built-in function min>'
"""

# the str string for an object
"""
>>> from datetime import date
>>> tues = date(2011, 9, 12)
>>> repr(tues)
'datetime.date(2011, 9, 12)'
>>> str(tues)
'2011-09-12'
"""

# Callable objects
"""
>>> def make_adder(n):
        def adder(k):
            return n + k
        return adder
>>> add_three = make_adder(3)
>>> add_three(4)
7

%%可以改写为：
>>> class Adder(object):
        def __init__(self, n):
            self.n = n
        def __call__(self, k):
            return self.n + k
>>> add_three_obj = Adder(3)
>>> add_three_obj(4)
7
"""

# __str__ usage
"""
The __str__ method is used in multiple places by Python: 
print() function, 
str() constructor, 
f-strings, 
and more.
"""

# __repr__ usage
"""
The __repr__ method is used multiple places by Python: 
when repr(object) is called 
and when displaying an object in an interactive Python session.
"""