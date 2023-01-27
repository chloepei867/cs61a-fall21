#Q3 If function vs statement
def if_function(condition, true_result, false_result):
    """Return true_result if condition is a true value, and
    false_result otherwise.

    >>> if_function(True, 2, 3)
    2
    >>> if_function(False, 2, 3)
    3
    >>> if_function(3==2, 'equal', 'not equal')
    'not equal'
    >>> if_function(3>2, 'bigger', 'smaller')
    'bigger'
    """
    if condition:
        return true_result
    else:
        return false_result

def with_if_statement():
    """
    >>> result = with_if_statement()
    61A
    >>> print(result)
    None
    """
    if cond():
        return true_func()
    else:
        return false_func()

def with_if_function():
    """
    >>> result = with_if_function()
    Welcome to
    61A
    >>> print(result)
    None
    """
    return if_function(cond(), true_func(), false_func())

def cond():
    "*** YOUR CODE HERE ***"
    return False

def true_func():
    "*** YOUR CODE HERE ***"
    print("Welcome to")

def false_func():
    "*** YOUR CODE HERE ***"
    print("61A")

#with_if_function()中，当if_function()被调用时，三个operands都会被evaluate

"""
可以看到with_if_statement()和with_if_statement()的结果是不一样的。
主要原因是rules ofevaluation for if statements and call expressions不同。
rules of call expressions:
1.Evaluate the operator to get a function.
2. Evaluate the operand(s) from left to right.
3. Apply the value of the operator on the value(s) of the operand(s).
!!!重点是第二点，要把参数从左到右都evaluate一遍
"""

def is_prime(n):
    """
    >>> is_prime(10)
    False
    >>> is_prime(7)
    True
    """
    for i in range(2,n):
        if n%i == 0:
            return False
    return True