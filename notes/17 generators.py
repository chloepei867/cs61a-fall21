"""
Generator is returned from a generator function.
"""


# exercise: Countdown
def countdown(n):
    """
    Generate a countdown of numbers from N down to 'blast off!'.
    >>> c = countdown(3)
    >>> next(c)
    3
    >>> next(c)
    2
    >>> next(c)
    1
    >>> next(c)
    'blast off!'
    """
    while n > 0:
        yield n
        n -= 1
    yield "blast off!"

# Fibonacci generator
def generate_virfib():
    """Generate the next Virahanka-Fibonacci number.
    >>> g = generate_virfib()
    >>> next(g)
    0
    >>> next(g)
    1
    >>> next(g)
    1
    >>> next(g)
    2
    >>> next(g)
    3
    """
    prev = 0
    curr = 1
    while True:
        yield prev
        prev, curr = curr, prev + curr  

# yielding from iterables
def a_then_b(a, b):
    """
    >>> list(a_then_b(["Apples", "Aardvarks"], ["Bananas", "BEARS"]))
    ["Apples", "Aardvarks", "Bananas", "BEARS"]
    """
    for item in a:
        yield item
    for item in b:
        yield item

#---上述函数可以改写成：
def a_then_b(a, b):
    yield from a
    yield from b

list(a_then_b(["Apples", "Aardvarks"], ["Bananas", "BEARS"]))


# Yielding from generators
"""
A yield from can also yield the results 
 of another generator function (which could be itself).
"""
#examples:
def countdown(k):
    if k > 0:
        yield k
        yield from countdown(k - 1)

#上述函数等价于：
def countdown(k):
    while True:
        if k > 0:
            yield k
            k -= 1


# Generator functions with returns
"""
When a generator function executes a return statement, 
 it exits and cannot yield more values.
"""
#example
def f(x):
    yield x
    yield x + 1
    return
    yield x + 3   # unreachable

list(f(2))  # [2, 3]

"""
Providing a value to be returned is allowed, 
 but this value is not yielded.
"""
#example
def g(x):
    yield x
    yield x + 1
    return x + 2
    yield x + 3

list(g(2))     #--->  [2, 3]

# how to fix it?
def h(x):
    y = yield from g(x)   # capturing the returned value
    yield y

list(h(2))     # ---> [2, 3, 4]


# Examples: Counting Partitions
def count_partitions(n, m):
    """
    >>> count_partitions(6, 4)
    9
    """
    if n < 0 or m == 0:
        return 0
    else:
        exact_match = 0
        if n == m:
            exact_match = 1
        with_m = count_partitions(n-m, m)
        without_m = count_partitions(n, m-1)
        return exact_match + with_m + without_m

# converting to a generator
def partitions(n, m):
    """List partitions.

    >>> for p in partitions(6, 4): print(p)
    4 + 2
    4 + 1 + 1
    3 + 3
    3 + 2 + 1
    3 + 1 + 1 + 1
    2 + 2 + 2
    2 + 2 + 1 + 1
    2 + 1 + 1 + 1 + 1
    1 + 1 + 1 + 1 + 1 + 1
    """
    if n < 0 or m == 0:
        return 
    else:
        if n == m:
            yield str(m)
        for p in partitions(n-m, m):
            yield str(m) + "+" + p
        yield from partitions(n, m-1)


def prefixes(s):
    """
    >>> list(prefixes('both'))
    ['b', 'bo', 'bot', 'both']
    """
    if s:
        yield from prefixes(s[:-1])
        yield s


# exercise: filter iter
def filter_iter(iterable, fn):
    """
    >>> is_even = lambda x: x % 2 == 0
    >>> list(filter_iter(range(5), is_even)) # a list of the values yielded from the call to filter_iter
    [0, 2, 4]
    >>> all_odd = (2*y-1 for y in range(5))
    >>> list(filter_iter(all_odd, is_even))
    []
    >>> naturals = (n for n in range(1, 100))
    >>> s = filter_iter(naturals, is_even)
    >>> next(s)
    2
    >>> next(s)
    4
    """
    "*** YOUR CODE HERE ***"
    for i in iterable:
        if fn(i):
            yield i

# exercise: merge
def merge(a, b):
    """
    >>> def sequence(start, step):
    ...     while True:
    ...         yield start
    ...         start += step
    >>> a = sequence(2, 3) # 2, 5, 8, 11, 14, ...
    >>> b = sequence(3, 2) # 3, 5, 7, 9, 11, 13, 15, ...
    >>> result = merge(a, b) # 2, 3, 5, 7, 8, 9, 11, 13, 14, 15
    >>> [next(result) for _ in range(10)]
    [2, 3, 5, 7, 8, 9, 11, 13, 14, 15]
    """
    "*** YOUR CODE HERE ***"
    first_a, first_b = next(a), next(b)
    while True:
        if first_a == first_b:
            yield first_a
            first_a, first_b = next(a), next(b)
        elif first_a < first_b:
            yield first_a
            first_a = next(a)
        else:
            yield first_b
            first_b = next(b)


# exercise: generate_primes
def is_prime(n):
    """Returns True if n is a prime number and False otherwise.
    >>> is_prime(2)
    True
    >>> is_prime(16)
    False
    >>> is_prime(521)
    True
    """
    def helper(i):
        if i > (n ** 0.5): # Could replace with i == n
            return True
        elif n % i == 0:
            return False
        return helper(i + 1)
    return helper(2)

def primes_gen(n):
    """Generates primes in decreasing order.
    >>> pg = primes_gen(7)
    >>> list(pg)
    [7, 5, 3, 2]
    """
    if n == 1:
        return
    if is_prime(n):
        yield n
    yield from primes_gen(n-1)