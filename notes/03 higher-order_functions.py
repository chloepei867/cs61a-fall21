#Higher-Order Functions 
"""functions that can accept other functions as arguments
   or return functions as values
 """

#the Fibonacci Sequence
def fib(n):
    """compute the nth Fibonacci number, for n >= 1."""
    pred, curr = 0,1
    k = 1
    while k < n:
        pred, curr = curr, pred + curr
        k += 1
    return curr


##1.1 functions as arguments

def cube(x):
    return x**3

def summation(n,term):
    total, k = 0, 1
    while k <= n:
        total, k = total + term(k), k+1
    return total

summation(5,cube)


##1.2 functions as general methods
###example: Gloden ratio

def improve(update,close,guess=1):
    """
    update function: to improve that guess
    close comparison: to check whether the current guess is "close enough" to be considered correct
    """
    while not close(guess):
        guess = update(guess)
    return guess

def golden_update(guess):
    """
    the well-known properties of the golden ratio are that it can be computed by repeatedly summing the inverse of any positive number with 1, 
    and that it is one less than its square
    所以可以用这个特性来update guess
    """
    return 1/guess + 1

def square_close_to_successor(guess):
    return approx_eq(guess*guess, guess + 1)

def approx_eq(x, y, tolerance = 1e-15): #1e-15表示10的-15次方
    return abs(x-y)<tolerance

improve(golden_update, square_close_to_successor)


#检验general method improve的正确性
from math import sqrt
phi = 1/2 + sqrt(5)/2
def improve_test():
    approx_phi = improve(golden_update, square_close_to_successor)
    assert approx_eq(phi, approx_phi), "phi differs from its approximation"

improve_test()


##1.3 defining functions III: nested definitions
def average(x, y):
    return (x+y)/2
def sqrt(a):
    """
    local def statements do not get evaluated until sqrt is called.
    """
    def sqrt_update(x):
        return average(x, a/x)
    def sqrt_close(x):
        return approx_eq(x*x, a)
    return improve(sqrt_update, sqrt_close)

###lexical scope
"""
在上面这个例子中：sqrt_update refers to the name a, which is a formal parameter of its enclosing function sqrt. 
This discipline of sharing names among nested definitions is called lexical scoping.
or: Lexical Scoping defines how variable names are resolved in nested functions: 
inner functions contain the scope of parent functions even if the parent function has returned.
"""

###closures: locally defined functions are often called closures.

###

#举例说明
"""
下面的return结果为"I am just a local"而不是"I am global".
Because the function func() counts where is was originally
defined which is under the scope of function whatismyscope.
"""
scope = "I am global"
def whatismyscope():
    """
    >>> whatismyscope()
    I am just a local
    """
    scope = "I am just a local"
    def func():
        return scope
    return func()


##1.4 Functions as Returned Values
"""An important feature of lexically scoped programming languages is 
that locally defined functions maintain their parent environment when they are returned."""

def square(x):
    return x*x

def successor(x):
    return x+1

def compose1(f,g):
    def h(x):
      return f(g(x))  
    return h

def f(x):
    """never called"""
    return -x

square_successor = compose1(square,successor)
result = square_successor(12)  


##1.5 currying
"""
use higher-order functions to convert a function that takes multiple arguments 
into a chain of functions that each take a single argument.
More specifically, given a function f(x, y), we can define a function g such that g(x)(y) is equivalent to f(x, y).
Here, g is a higher-order function that takes in a single argument x 
and returns another function that takes in a single argument y.
"""

#example: curried version of the pow function:
def curried_pow(x):
    """
    >>> curried_pow(2)(3)
    8
    """
    def h(y):
        return pow(x,y)
    return h


#can define functions to automate currying, as well as the inverse uncurrying transformation:
def curry2(f):
    """return a curried version of the given two-argument function."""
    def g(x):
        def h(y):
            return f(x, y)
        return h
    return g

def uncurry2(g):
    """return a two-argument version of the given curried function."""
    def f(x, y):
        return g(x)(y)
    return f 


##1.6 Lambda Expressions --unnamed functions
"""
A lambda expression evaluates to a function that has a single return expression as its body. 
Assignment and control statements are not allowed.
"""

"""
lambda x: f(g(x))    
# a function that taks x and returns f(g(x))
"""

"""
>>> (lambda x: x * x)(3)
9
"""



##1.7 Function Decorators
"""
Python provides special syntax to apply higher-order functions as part of executing a def statement, called a decorator. 
Perhaps the most common example is a trace.
"""
#example:
def trace(fn):
    def wrapped(x):
        print('->',fn, '(', x, ')')
        return fn(x)
    return wrapped

@trace
def triple(x):
    return 3*x
#等价于：
def triple(x):
    return 3*x
triple = trace(triple)


#example:
def make_pretty(func):
    def inner():
        print("I got decorated")
        func()
    return inner


def ordinary():
    """
    >>> ordinary()
    I am ordinary
    #let's decorate this ordinary function
    >>> pretty = make_pretty(ordinary)
    >>> pretty()
    I got decorated
    I am ordinary
    """
    print("I am ordinary")


def ordinary():
    print("I am ordinary")
ordinary = make_pretty(ordinary)
#等价于：
@make_pretty
def ordinary():
    print("I am ordinary")


#locally defined functions
"""Functions defined within other function bodies are bound to names in a local frame."""
def make_adder(n):
    """return a function that takes one argument k and returns k + n
    >>> add_three = make_adder(3)
    >>> add_three(4)
    7
    >>> make_adder(3)(4)
    7
    """
    def adder(k):
        return n + k
    return adder