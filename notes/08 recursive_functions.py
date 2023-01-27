# 1.7.3 mutual recursion
"""
When a recursive procedure is divided among two functions that call each other, 
the functions are said to be mutually recursive.
"""

# 举例1：考虑一个非负整数的奇偶性
"""
a number is even if it is one more than an odd number
a number is odd if it is one more than an even number
0 is even
"""

def is_even(n):
    if n == 0:
        return True
    else:
        return is_odd(n-1)

def is_odd(n):
    if n == 0:
        return False
    else:
        return is_even(n-1)


#上述可以改写为：
def is_even(n):
    if n == 0:
        return True
    else:
        if (n-1) == 0:
            return False
        else:
            return is_even((n-1)-1)


# 举例2: the Luhn algorithm
"""
Used to verify that a credit card numbers is valid.

1/ From the rightmost digit, which is the check digit, moving left, double the value of every second digit; 
if product of this doubling operation is greater than 9 (e.g., 7 * 2 = 14), 
then sum the digits of that product (e.g., 14: 1 + 4 = 5)

2/ Take the sum of all the digits
"""
def sum_digits(n):
    if n < 10:
        return n
    else:
        last = n%10
        all_but_last = n//10
        return last + sum_digits(all_but_last)
    

def luhn_sum(n):
    if n < 10:
        return n
    else:
        last = n% 10
        all_but_last = n//10
        return last + luhn_sum_double(all_but_last)


def luhn_sum_double(n):
    last = n%10
    all_but_last = n//10
    luhn_digit = sum_digits(last*2)
    if n < 10:
        return luhn_digit
    else:
        return luhn_sum(all_but_last) + luhn_digit



# 1.7.3 printing in recursive functions
def cascade(n):
    """
    >>> cascade(2013)
    2013
    201
    20
    2
    20
    201
    2013
    """
    if n < 10:
        print(n)
    else:
        print(n)
        cascade(n//10)
        print(n)

# 不是一定要有base cases(if n < 10),所以上述可以改写成： 
# The base case is what prevents recursive functions from recursing infinitely
def cascade(n):
    """Print a cascade of prefixes of n."""
    print(n)
    if n >= 10:
        cascade(n//10)
        print(n)


# 举例2：
"""
n个石子，两个玩家依次轮流拿走1-2个石子，最后一个拿走石子的玩家获胜
alice的策略：每次只拿一个
bob的策略：如果还有偶数个，就拿2个；反之拿1个
"""

def play_alice(n):
    if n == 0:
        print("Bob wins!")
    else:
        play_bob(n-1)

def play_bob(n):
    if n == 0:
        print("Alice wins!")
    elif is_even(n):
        play_alice(n-2)
    else:
        play_alice(n-1)


# 1.7.4 tree recursion
"""
A function with multiple recursive calls is said to be tree recursive.
"""

#举例： Fibonacci numbers
def fib(n):
    if n == 1:
        return 0
    if n == 2:
        return 1
    else:
        return fib(n-2) + fib(n-1)


# 举例：partitions
"""
The number of partitions of a positive integer n, 
using parts up to size m, is the number of ways in which n can be expressed 
as the sum of positive integer parts up to m in increasing order.
"""

def count_partitions(n, m):
    """Count the ways to partition n using parts up to m."""
    if n == 0:
        return 1
    elif n < 0:
        return 0
    elif m == 0:
        return 0
    else:
        return count_partitions(n-m, m) + count_partitions(n, m-1)


# There are three main steps in a recursive definition:
"""
1/ Base case. 

You can think of the base case as the case of the simplest function input, 
or as the stopping condition for the recursion.

2/ Recursive call on a smaller problem. 

You can think of this step as calling the function on a smaller problem that our current problem depends on. 
We assume that a recursive call on this smaller problem will give us the expected result; 
we call this idea the "recursive leap of faith".

3/ Solve the larger problem. 
"""


# is_prime(): recursion version

def is_prime(n):
    def is_factor(x):
        if x >= n:
            return True
        if x < n and n%x == 0:
            return False
        return is_factor(x+1)   
    return is_factor(2)



# disc 03- Q5 : recursive hailstone
def hailstone(n):
    """Print out the hailstone sequence starting at n, and return the number of elements in the sequence.
    >>> a = hailstone(10)
    10
    5
    16
    8
    4
    2
    1
    >>> a
    7
    """
    def k(n, x):
        print(n)
        if n == 1:
            return x
        elif n%2 == 0:
            n = n//2
        else:
            n = n*3 + 1
        x += 1
        return k(n, x)    
    return k(n, 1)


# disc 03- Q5 : merge numbers
def merge(n1, n2):
    """ Merges two numbers by digit in decreasing order
    >>> merge(31, 42)
    4321
    >>> merge(21, 0)
    21
    >>> merge (21, 31) 
    3211
    """
    if n1 == 0 and n2:
        return n2
    elif n2 == 0 and n1:
        return n1
    elif n1%10 <= n2%10:
        return merge(n1//10, n2)*10 + n1%10
    else:
        return merge(n2//10, n1)*10 + n2%10

# cascade
def cascade(n):
    if n < 10:
        print(n)
    else:
        print(n)
        cascade(n//10)
        print(n)


# inverse cascade solution 
def inverse_cascade(n):
    grow(n)
    print(n)
    shrink(n)

def f_then_g(f, g, n):
    if n:
        f(n)
        g(n)

grow = lambda n: f_then_g(grow, print, n//10)
shrink = lambda n: f_then_g(print, shrink, n//10)

# hw03: Ping-pong

def num_eights(pos):
    """Returns the number of times 8 appears as a digit of pos.

    >>> num_eights(3)
    0
    >>> num_eights(8)
    1
    >>> num_eights(88888888)
    8
    >>> num_eights(2638)
    1
    >>> num_eights(86380)
    2
    >>> num_eights(12345)
    0
    """
    if pos == 8:
        return 1
    elif pos < 10 and pos != 8:
        return 0
    else:
        return num_eights(pos//10) + num_eights(pos%10)


def pingpong_iter(n):
    i, current, direction = 1,1,1
    while i <n:
        if i % 8 == 0 or num_eights(i):
            direction = -direction
        current += direction
        i += 1
    return current

def pingpong(n):
    def helper(n, i, current, direction):
        if i == n:
            return current
        else:
            if i % 8 == 0 or num_eights(i):
                return helper(n, i+1, current-direction, -direction)
            else:
                return helper(n, i+1, current+direction, direction)
    return helper(n, 1, 1, 1)   


# solution 2
def pingpong(n):
    if n <= 8:
        return n
    return pingpong(n-1) + direction(n-1)

def direction(n):
    if n < 8:
        return 1
    if n%8 == 0 or num_eights(n):
        return -1*direction(n-1)
    return direction(n-1)
    

# hw03: count_coins
def get_larger_coin(coin):
    """Returns the next larger coin in order.
    >>> get_larger_coin(1)
    5
    >>> get_larger_coin(5)
    10
    >>> get_larger_coin(10)
    25
    >>> get_larger_coin(2) # Other values return None
    """
    if coin == 1:
        return 5
    elif coin == 5:
        return 10
    elif coin == 10:
        return 25

def get_smaller_coin(coin):
    """Returns the next smaller coin in order.
    >>> get_smaller_coin(25)
    10
    >>> get_smaller_coin(10)
    5
    >>> get_smaller_coin(5)
    1
    >>> get_smaller_coin(2) # Other values return None
    """
    if coin == 25:
        return 10
    elif coin == 10:
        return 5
    elif coin == 5:
        return 1

def count_coins(change):
    """Return the number of ways to make change using coins of value of 1, 5, 10, 25.
    >>> count_coins(15)
    6
    >>> count_coins(10)
    4
    >>> count_coins(20)
    9
    >>> count_coins(100) # How many ways to make change for a dollar?
    242
    >>> count_coins(200)
    1463
    >>> from construct_check import check
    >>> # ban iteration
    >>> check(HW_SOURCE_FILE, 'count_coins', ['While', 'For'])
    True
    """
    def constrained_count(change, smallest_coin):
        if change == 0:
            return 1
        if change < 0:
            return 0
        if smallest_coin == None:
            return 0
        without_coin = constrained_count(change, get_larger_coin(smallest_coin))
        with_coin = constrained_count(change - smallest_coin, smallest_coin)
        return without_coin + with_coin
    return constrained_count(change, 1)



