# procedural
# OOP: behavioural, data (attributes,fields,properties)

# dynamically typed
# a.k.a. untyped/weakly

# Java - strongly - typed, statically typed

# variable names in Python are normally snake_cased
# Classnames start with a capital
# creating an instance of an object is instantiation

# int, string, float, boolean, list, set dictionary, tuple
# None, True / False
# set is unique
# lists are sequences
# dicts have key, value pairs
# tuples are immutable

# string
greeting = 'hello'

#integer
high_score = 10

#float
tax_rate = 99.9

#boolean
active = True

# list
classmates = ['Ilia','Abdul Bari','Aiman']

# set - will only have three items
transaction_ID = {45849,492304,48394,48394}

# tuple
purchase_record = ('apples', 'bananas','coke','chocolate')

# dictionary
leaderboard_dict = {'Ilia':50, 'Abdul Bari': 23, 'Aiman': 15}

class Cat:
    # double underscore dunda built in attribute
    # instantiate
    def __init__(self):
        self.name = ("Victoria's cat")
    def meow(self):
        print(self.name + " says meow")

cat = Cat()
cat.meow()
# tells the object to run its meow method