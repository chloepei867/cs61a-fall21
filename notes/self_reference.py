#self reference
"""
Self-reference refers to a particular design of HOF, where a function eventually
returns itself. In particular, a self-referencing function will not return a function
call, but rather the function object itself.
"""

def print_all(x):
    print(x)
    return print_all

def print_n(n):
    """
    >>> f = print_n(2)
    >>> f = f("hi")
    hi
    >>> f = f("hello")
    hello
    >>> f = f("bye")
    done
    >>> g = print_n(1)
    >>> g("first")("second")("third")
    first
    done
    done
    <function inner_print>
    """
    def inner_print(x):
        if n <= 0:
            print("done")
        else:
            print(x)
        return print_n(n-1)      ##这里是重点，在调用函数本身的时候进行迭代
    return inner_print