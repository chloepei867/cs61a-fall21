from math import truediv, floordiv
50/3
#等同于：
truediv(50,3)

50//3
#等同于：
floordiv(50,3)

#Prime Factorization
#Each positive integer n has a set of prime factors: primes whose product is n.

def smallest_prime_factor(n):
    """return the smallest k > 1 that evenly divides n."""
    k = 2
    while n % k != 0:
        k += 1
    return k

def prime_factors(n):
    """print the prime factors of n in non-decreasing order
    >>> prime_factors(8)
    2
    2
    2
    >>> prime_factors(12)
    2
    2
    3
    >>> prime_factors(858)
    2
    3
    11
    13
    """
    while n > 1:
        k =smallest_prime_factor(n)
        n = n // k
        print(k)

#等同于：
def prime_factors(n):
    while n > 1:
        smallest_prime = 2
        while n % smallest_prime != 0:
            smallest_prime += 1
        n = n // smallest_prime
        print(smallest_prime)


#Boolean Contexts
"""False values in Python: False, 0, ''(empty string), None ..."""
"""True values in Python: anything else(True)"""

#命令行运行python
"""
python3 test.py #注意：在windows里可能需要用py代替python3
python3 -i test.py, 运行python脚本，并打开一个交互式会话
python3 -m doctest test.py, 运行doctest
python3 -m doctest test.py -v, 运行doctest，-v option stands for verbose
(不仅告诉你哪个测试未通过，还告诉你哪个测试通过了)
"""

#short-circuiting 短路特性
"""
To evaluate the expression <left> and <right>:
# Evaluate the subexpression <left>.
# If the result is a false value v, then the expression evaluates to v.
# Otherwise, the expression evaluates to the value of the subexpression <right>.

To evaluate the expression <left> or <right>:
# Evaluate the subexpression <left>.
# If the result is a true value v, then the expression evaluates to v.
# Otherwise, the expression evaluates to the value of the subexpression <right>.

To evaluate the expression not <exp>:
# Evaluate <exp>; The value is True if the result is a false value, and False otherwise.

>>> True and 14
14
>>> 0 and 14
0
>>> -1 and 1 > 0
True #不是返回 1 > 0 哦！！！
>>> True and 1 / 0 and False
error #出错
>>> (True or False) and False
False

>>> False or 0
0
>>> True or 14
True
>>> 0 or False or 2 or 1 / 0
2

>>> not 10
False
>>> True and True
True
"""

#Debugging
# Debugging Techniques
"""
1/running doctests
python3 -m doctest test.py

2/ writing your own tests
· test-driven development: write tests before coding
· write more tests after coding
· test edge cases: 测试极端值

3/ using print statements
用途：
// 用于view the results of function calls 
// 用在while loop结尾to view the state of the counter variables after each iteration

3.1 example:通过修改debug = True or False,来控制是否打印
debug = True
def foo(n):
i = 0
while i < n:
    i += func(i)
    if debug:
        print('DEBUG: i is', i)

4/ interactive debugging
run: python -i file.py

5/ PythonTutor Debugging

6/ using assert statements
def double(x):
    assert isinstance(x, int), "The input to double(x) must be an integer"
    return 2 * x
说明：如果input x 不是int，那么就会返回"The input to double(x) must be an integer"的错误提示信息

"""

#isinstance(object, classinfo)
"""

a = 2
b = [1,2,3]
>>> isinstance(a,int)
True
>>> isinstance(a,str)
False
>>> isinstance(b,list)
True

"""
