#Higher-Order Function example: Repeat
from tkinter import Y


def repeat(f, x):
    while f(x) != x :
        x = f(x)
    return x

def g(y):
    return (y + 5) // 3

"""
>>> repeat(g, 5)
2
hint: while语句为true时会一直循环！！
"""

#Environment Diagrams for Nested Def Statements
def make_adder(n):
    def adder(k):
        return k + n
    return adder

add_three = make_adder(3)
add_three(4)


#How to draw an environment diagram
"""
When a function is defined:
Create a function value:  func <name>(<formal parameters>)[parent=<parent>]
Its parent is the current frame.

Bind <name> to the function value in the current frame

When a function is called:
1. add a local frame, titled with the <name> of the function being called.
2. copy the parent of the function to the local frame: [parent=<label>]
3. bind the <formal parameters> to the arguments in the local frame.
4. execute the body of the function in the environment that starts with the local frame.
"""


#local names. Formal parameters of functions have a local scope.
#举例
def f(x, y):
    return g(x)

def g(a):
    return a + y

"""
f(1, 2)
报错：NameError: global name 'y' is not defined.
说明：f(x,y)里的y=2 is not in the current environment(which consists of the 
local frame:g and the global frame)
"""

#function composition
def square(x):
    return x * x

def make_adder(n):
    def adder(k):
        return k + n
    return adder

def compose1(f, g):
    def h(x):
        return f(g(x))
    return h

compose1(square,make_adder(2))(3) #用PythonTutor看一下过程


#self-reference
def print_all(x):
    print(x)
    return print_all

print_all(1)(3)(5)


#returning a function by its own name
def print_sums(n):
    print(n)
    def next_sum(k):
        return print_sums(n+k)
    return next_sum

print_sums(1)(3)(5)


"""
Currying is the act of transforming a multi argument function into a single
argument higher-order function that returns a function that takes the rest of 
the arguments.
"""

#研究下下面几个例子
def delay(arg):
    print('delayed')
    def g():
        return arg
    return g

delay(delay)()(6)()
print(delay(print)()(4))


# exercise: environment diagram
def horse(mask):
    horse = mask
    def mask(horse):
        return horse
    return horse(mask)

mask = lambda horse: horse(2)
horse(mask)


def remove(n, digit):
    """Return digits of non-negative N that are not DIGIT, for some
    non-negative DIGIT less than 10.
    >>> remove(231, 3)
    21
    >>> remove(243132, 2)
    4313
    """
    kept = 0
    digits = 0
    while n>0:
        last = n%10
        n = n//10
        if last != digit:
            kept = kept + (last*10**digits)
            digits = digits +1
    return kept


wow = 6

def much(wow):
    if much == wow:
        such = lambda wow: 5
        def wow():
            return such
        return wow
    such = lambda wow: 4
    return wow()

wow = much(much(much))(wow)


