# bound method
"""
bound method:
a function which has its first parameter pre-bound to a particular value.
"""


# exercise: player game
"""
This class represents a player in a video game.
It tracks their name and health.
"""
class Player:
    """
    >>> player = Player("Mario")
    >>> player.name
    'Mario'
    >>> player.health
    100
    >>> player.damage(10)
    >>> player.health
    90
    >>> player.boost(5)
    >>> player.health
    95
    """
    def __init__(self, name):
        self.name = name
        self.health = 100

    def damage(self, k):
        self.health -= k
    
    def boost(self, b):
        self.helath += b


# exercise: chlothing class
"""
Clothing is a class that represents pieces of clothing in a closet. 
It tracks the color, category, and clean/dirty state.
"""
class Clothing:
    """
    >>> blue_shirt = Clothing("shirt", "blue")
    >>> blue_shirt.category
    'shirt'
    >>> blue_shirt.color
    'blue'
    >>> blue_shirt.is_clean
    True
    >>> blue_shirt.wear()
    >>> blue_shirt.is_clean
    False
    >>> blue_shirt.clean()
    >>> blue_shirt.is_clean
    True
    """
    def __init__(self, category, color):
        self.category = category
        self.color = color
        self.is_clean = True

    def wear(self):
        self.is_clean = False
    
    def clean(self):
        self.is_clean = True


# Class variables
"""
A class variable is an assignment inside the class 
that isn't inside a method body.
Class variables are "shared" across all instances of a class 
because they are attributes of the class, not the instance.
"""

class Product:
    sales_tax = 0.07

    def get_total_price(self, quantity):
        return (self.price * (1 + self.sales_tax)) * quantity

pina_bar = Product("Piña Chocolotta", 7.99,
    ["200 calories", "24 g sugar"])
truffle_bar = Product("Truffalapagus", 9.99,
    ["170 calories", "19 g sugar"])

pina_bar.sales_tax
truffle_bar.sales_tax
pina_bar.get_total_price(4)
truffle_bar.get_total_price(4)

# exercise: student grade class
"""
This class represents grades for students in a class.
"""
class StudentGrade:
    """
    >>> grade1 = StudentGrade("Arfur Artery", 300)
    >>> grade1.is_failing()
    False
    >>> grade2 = StudentGrade("MoMo OhNo", 158)
    >>> grade2.is_failing()
    True
    >>> grade1.failing_grade
    159
    >>> grade2.failing_grade
    159
    >>> StudentGrade.failing_grade
    159
    >>>
    """
    failing_grade = 159    #class variables

    def __init__(self, student_name, num_points):
        self.student_name = student_name
        self.num_points = num_points

    def is_failing(self):
        return self.num_points < self.failing_grade


# Accessing attributes: getattr(), hasattr()
getattr(pina_bar, 'inventory')   # 1
hasattr(pina_bar, 'reduce_inventory')  # True


# Public vs. Private
"""
Attributes are all public:
As long as you have a reference to an object, 
you can access or change any attributes.

"Private" attributes
To communicate the desired access level of attributes, 
Python programmers generally use this convention:

__ (double underscore) before very private attribute names
_ (single underscore) before semi-private attribute names
no underscore before public attribute names
"""
