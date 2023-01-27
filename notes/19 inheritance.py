# Base classes(superclass) and subclasses
"""
When multiple classes share similar attributes, 
you can reduce redundant code by defining a base class 
and then subclasses can inherit from the base class.
"""
class Animal:
    species_name = "Animal"
    scientific_name = "Animalia"
    play_multiplier = 2
    interact_increment = 1

    def __init__(self, name, age=0):
        self.name = name
        self.age = age
        self.calories_eaten  = 0
        self.happiness = 0

    def play(self, num_hours):
        self.happiness += (num_hours * self.play_multiplier)
        print("WHEEE PLAY TIME!")

    def eat(self, food):
        self.calories_eaten += food.calories
        print(f"Om nom nom yummy {food.name}")
        if self.calories_eaten > self.calories_needed:
            self.happiness -= 1
            print("Ugh so full")

    def interact_with(self, animal2):
        self.happiness += self.interact_increment
        print(f"Yay happy fun time with {animal2.name}")

# subclasses
"""
Subclasses can override existing class variables and assign new class variables.
"""

# overriding methods
class Panda(Animal):
    species_name = "Giant Panda"
    scientific_name = "Ailuropoda melanoleuca"
    calories_needed = 6000

    def interact_with(self, other):
        print(f"I'm a Panda, I'm solitary, go away {other.name}!")

panda1 = Panda("Pandeybear", 6)
panda2 = Panda("Spot", 3)
panda1.interact_with(panda2)     # call the overriding method!


# Exercise: Clothing
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

class KidsClothing(Clothing):
    """
    >>> onesie = KidsClothing("onesie", "polka dots")
    >>> onesie.wear()
    >>> onesie.is_clean
    False
    >>> onesie.clean()
    >>> onesie.is_clean
    False
    >>> dress = KidsClothing("dress", "rainbow")
    >>> dress.clean()
    >>> dress.is_clean
    True
    >>> dress.wear()
    >>> dress.is_clean
    False
    >>> dress.clean()
    >>> dress.is_clean
    False
    """
  
    # Override the clean() method
    # so that kids clothing always stays dirty!
    def clean(self):
        self.is_clean = self.is_clean


# exercise: catplay
class Animal:
    species_name = "Animal"
    scientific_name = "Animalia"
    play_multiplier = 2
    interact_increment = 1

    def __init__(self, name, age=0):
        self.name = name
        self.age = age
        self.calories_eaten  = 0
        self.happiness = 0

    def play(self, num_hours):
        self.happiness += (num_hours * self.play_multiplier)
        print("WHEEE PLAY TIME!")

    def eat(self, food):
        self.calories_eaten += food.calories
        print(f"Om nom nom yummy {food.name}")
        if self.calories_eaten > self.calories_needed:
            self.happiness -= 1
            print("Ugh so full")

    def interact_with(self, animal2):
        self.happiness += self.interact_increment
        print(f"Yay happy fun time with {animal2.name}")


class Cat(Animal):
    """
    >>> adult = Cat("Winston", 12)
    >>> adult.name
    'Winston'
    >>> adult.age
    12
    >>> adult.play_multiplier
    3
    >>> kitty = Cat("Kurty", 0.5)
    >>> kitty.name
    'Kurty'
    >>> kitty.age
    0.5
    >>> kitty.play_multiplier
    6
    """
    species_name = "Domestic cat"
    scientific_name = "Felis silvestris catus"
    calories_needed = 200
    play_multiplier = 3
  
    def __init__(self, name, age):
      #  Call the super class to set name and age
      # If age is less than 1, set play multiplier to 6
      super().__init__(name, age)
      if self.age < 1:
          self.play_multiplier = 6


# Exercise: Dog weight
class Animal:
    species_name = "Animal"
    scientific_name = "Animalia"
    play_multiplier = 2
    interact_increment = 1

    def __init__(self, name, age=0):
        self.name = name
        self.age = age
        self.calories_eaten  = 0
        self.happiness = 0

    def play(self, num_hours):
        self.happiness += (num_hours * self.play_multiplier)
        print("WHEEE PLAY TIME!")

    def eat(self, food):
        self.calories_eaten += food.calories
        print(f"Om nom nom yummy {food.name}")
        if self.calories_eaten > self.calories_needed:
            self.happiness -= 1
            print("Ugh so full")

    def interact_with(self, animal2):
        self.happiness += self.interact_increment
        print(f"Yay happy fun time with {animal2.name}")

class Dog(Animal):
    """
    >>> spot = Dog("Spot", 5, 20)
    >>> spot.name
    'Spot'
    >>> spot.age
    5
    >>> spot.weight
    20
    >>> spot.calories_needed
    400
    >>> puppy = Dog("Poppy", 1, 7)
    >>> puppy.name
    'Poppy'
    >>> puppy.age
    1
    >>> puppy.weight
    7
    >>> puppy.calories_needed
    140
    """
    species_name = "Domestic dog"
    scientific_name = "Canis lupus familiaris"
    calories_needed = 200
  
    def __init__(self, name, age, weight):
      #  Call the super class to set name and age
      #  Set the weight attribute
      #  Set calories_needed to 20x the weight
      super().__init__(name, age)
      self.weight = weight
      self.calories_needed = 20 * self.weight


# Adding layers of inheritance
# defining the new classes
class Herbivore(Animal):

    def eat(self, food):
        if food.type == "meat":
            self.happiness -= 5
        else:
            super().eat(food)

class Carnivore(Animal):

    def eat(self, food):
        if food.type == "meat":
            super().eat(food)

# then change the base classes for the subclasses:
"""
class Rabbit(Herbivore):
class Panda(Herbivore):
class Elephant(Herbivore):

class Vulture(Carnivore):
class Lion(Carnivore):
"""

# multiple inheritance
"""
A class may inherit from multiple base classes in Python.
"""
#* First we define the new base classes:
class Predator(Animal):

    def interact_with(self, other):
        if other.type == "meat":
            self.eat(other)
            print("om nom nom, I'm a predator")
        else:
            super().interact_with(other)

class Prey(Animal):
    type = "meat"
    calories = 200

#* Then we inherit from them by putting both names in the parentheses:
"""
class Rabbit(Prey, Herbivore):
class Lion(Predator, Carnivore):
"""

# referencing other instances
class Animal:

    def mate_with(self, other):
        if other is not self and other.species_name == self.species_name:
            self.mate = other
            other.mate = self

mr_wabbit = Rabbit("Mister Wabbit", 3)
jane_doe = Rabbit("Jane Doe", 2)
mr_wabbit.mate_with(jane_doe)


# inheritance and composition
"""
composition means that one class has the other as an attribute.
"""
class Account:
        """A bank account that has a non-negative balance."""
        interest = 0.02
        def __init__(self, account_holder):
            self.balance = 0
            self.holder = account_holder

        def deposit(self, amount):
            """Increase the account balance by amount and return the new balance."""
            self.balance = self.balance + amount
            return self.balance

        def withdraw(self, amount):
            """Decrease the account balance by amount and return the new balance."""
            if amount > self.balance:
                return 'Insufficient funds'
            self.balance = self.balance - amount
            return self.balance

class Bank:
    """A bank *has* accounts.
    >>> bank = Bank()
    >>> john = bank.open_account('John', 10)
    >>> jack = bank.open_account('Jack', 5, CheckingAccount)
    >>> john.interest
    0.02
    >>> jack.interest
    0.01
    >>> john.balance
    10.2
    >>> too_big_too_fail()
    True
    """
    def __init__(self):
        self.accounts = []
    
    def open_account(self, holder, amount, kind= Account ):
        account = kind(holder)
        account.deposit(amount)
        self.accounts.append(account)
        return account
    
    def pay_interest(self):
        for a in self.accounts:
            a.deposit(a.balance*a.interest)

    def too_big_too_fail(self):
        return len(self.accounts) > 1


# Inheritance and Attribute Lookup
class A:
    z = -1
    def f(self, x):
        return B(x-1)

class B(A):
    n = 4
    def __init__(self, y):
        if y:
            self.z = self.f(y)
        else:
            self.z = C(y+1)

class C(B):
    def f(self, x):
        return x

a = A()
b = B(1)
b.n = 5

"""
>>> C(2).n
4
>>> a.z == C.z
True
>>> a.z == b.z
False
>>> b.z  -->a B instance
>>> b.z.z -->a B instance
>>> b.z.z.z 
1
>>> b.z.z.z  #---> AttributeError
"""
