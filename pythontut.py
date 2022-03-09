import sys
import math
import random
import threading
import time
from functools import reduce

# ----- INTRO -----
# Python files end with the extension .py
# Print to the console
# Python statements terminate with a newline
print("Hello World")

# Accept user input and store it in a variable
# name = input("What is your name ")
# print("Hi ", name)

# If you want to extend a statement to multiple
# lines you can use parentheses or \
v1 = (
        1 + 2
        + 3
)
v1 = 1 + 2 \
     + 3

# Put multiple statements on 1 line
v1 = 5;
v1 = v1 - 1

"""
Multi-line
Comment
"""

# ----- VARIABLES -----
# Variables are names assigned to values
# The 1st character must be _ or a letter
# Then you can use letters, numbers or _
# Variable names are type sensitive
v2 = 1
V2 = 2  # v1 is different from V1

# You can assign multiple variables
v3 = v4 = 20

# ----- DATA TYPES -----
# Data in Python is dynamically typed and that
# data type can change
# All data is an object which I cover later
# The basic types are integers, floats,
# complex numbers, strings, booleans
# Python doesn't have a character type

# How to get the type
print(type(10))

# There is no limit to the size of integers
# This is a way to get a practical max size
print(sys.maxsize)

# Floats are values with decimal values
# This is how to get a max float
print(sys.float_info.max)

# But, they are accurate to 15 digits
f1 = 1.1111111111111111
f2 = 1.1111111111111111
f3 = f1 + f2
print(f3)

# Complex numbers are [real part]+[imaginary part]
cn1 = 5 + 6j

# Booleans are either True or False
b1 = True

# Strings are surrounded by ' or "
str1 = "Escape Sequences \' \t \" \\ and \n"

str2 = '''Triple quoted strings can contain ' and "'''

# You can cast to different types with int, float,
# str, chr
print("Cast ", type(int(5.4)))  # to int
print("Cast 2 ", type(str(5.4)))  # to string
print("Cast 3 ", type(chr(97)))  # to string
print("Cast 4 ", type(ord('a')))  # to int

# ----- OUTPUT -----
# You can define a separator for print
print(12, 21, 1974, sep='/')

# Eliminate newline
print("No Newline", end='')

# String formatting %e for exponent
print("\n%04d %s %.2f %c" % (1, "Derek", 1.234, 'A'))

# ----- MATH -----
print("5 + 2 =", 5 + 2)
print("5 - 2 =", 5 - 2)
print("5 * 2 =", 5 * 2)
print("5 / 2 =", 5 / 2)
print("5 % 2 =", 5 % 2)
print("5 ** 2 =", 5 ** 2)
print("5 // 2 =", 5 // 2)

# Shortcuts
i1 = 2
i1 += 1
print("i1 ", i1)

# Math Functions
print("abs(-1) ", abs(-1))
print("max(5, 4) ", max(5, 4))
print("min(5, 4) ", min(5, 4))
print("pow(2, 2) ", pow(2, 2))
print("ceil(4.5) ", math.ceil(4.5))
print("floor(4.5) ", math.floor(4.5))
print("round(4.5) ", round(4.5))
print("exp(1) ", math.exp(1))  # e**x
print("log(e) ", math.log(math.exp(1)))
print("log(100) ", math.log(100, 10))  # Base 10 Log
print("sqrt(100) ", math.sqrt(100))
print("sin(0) ", math.sin(0))
print("cos(0) ", math.cos(0))
print("tan(0) ", math.tan(0))
print("asin(0) ", math.asin(0))
print("acos(0) ", math.acos(0))
print("atan(0) ", math.atan(0))
print("sinh(0) ", math.sinh(0))
print("cosh(0) ", math.cosh(0))
print("tanh(0) ", math.tanh(0))
print("asinh(0) ", math.asinh(0))
print("acosh(pi) ", math.acosh(math.pi))
print("atanh(0) ", math.atanh(0))
print("hypot(0) ", math.hypot(10, 10))  # sqrt(x*x + y*y)
print("radians(0) ", math.radians(0))
print("degrees(pi) ", math.degrees(math.pi))

# Generate a random int
print("Random", random.randint(1, 101))

# ----- NaN & inf -----
# inf is infinity
print(math.inf > 0)

# NaN is used to represent a number that can't
# be defined
print(math.inf - math.inf)

# ----- CONDITIONALS -----
# Comparison Operators : < > <= >= == !=

# if, else & elif execute different code depending
# on conditions
age = 30
if age > 21:
    # Python uses indentation to define all the
    # code that executes if the above is true
    print("You can drive a tractor trailer")
elif age >= 16:
    print("You can drive a car")
else:
    print("You can't drive")

# Make more complex conditionals with logical operators
# Logical Operators : and or not
if age < 5:
    print("Stay Home")
elif (age >= 5) and (age <= 6):
    print("Kindergarten")
elif (age > 6) and (age <= 17):
    print("Grade %d", (age - 5))
else:
    print("College")

# Ternary operator in Python
# condition_true if condition else condition_false
canVote = True if age >= 18 else False

# ----- STRINGS -----
# Raw strings ignore escape sequences
print(r"I'll be ignored \n")

# Combine strings with +
print("Hello " + "You")

# Get string length
str3 = "Hello You"
print("Length ", len(str3))

# Character at index
print("1st ", str3[0])

# Last character
print("Last ", str3[-1])

# 1st 3 chrs
print("1st 3 ", str3[0:3])  # Start, up to not including

# Get every other character
print("Every Other ", str3[0:-1:2])  # Last is a step

# You can't change an index value like this
# str3[0] = "a" because strings are immutable
# (Can't Change)
# You could do this
str3 = str3.replace("Hello", "Goodbye")
print(str3)

# You could also slice front and back and replace
# what you want to change
str3 = str3[:8] + "y" + str3[9:]
print(str3)

# Test if string in string
print("you" in str3)

# Test if not in
print("you" not in str3)

# Find first index for match or -1
print("You Index ", str3.find("you"))

# Trim white space from right and left
# also lstrip and rstrip
print("    Hello    ".strip())

# Convert a list into a string and separate with
# spaces
print(" ".join(["Some", "Words"]))

# Convert string into a list with a defined separator
# or delimiter
print("A, string".split(", "))

# Formatted output with f-string
int1 = int2 = 5
print(f'{int1} + {int2} = {int1 + int2}')

# To lower and upper case
print("A String".lower())
print("A String".upper())

# Is letter or number
print("abc123".isalnum())

# Is characters
print("abc".isalpha())

# Is numbers
print("abc".isdigit())

# ----- LISTS -----
# Lists can contain mutable pieces of data of
# varying data types or even functions
l1 = [1, 3.14, "Derek", True]

# Get length
print("Length ", len(l1))

# Get value at index
print("1st", l1[0])
print("Last", l1[-1])

# Change value
l1[0] = 2

# Change multiple values
l1[2:4] = ["Bob", False]

# Insert at index without deleting
# Also l1.insert(2, "Paul")
l1[2:2] = ["Paul", 9]

# Add to end (Also l1.extend([5, 6]))
l2 = l1 + ["Egg", 4]

# Remove a value
l2.remove("Paul")

# Remove at index
l2.pop(0)
print("l2", l2)

# Add to beginning (Also l1.append([5, 6]))
l2 = ["Egg", 4] + l1

# Multidimensional list
l3 = [[1, 2], [3, 4]]
print("[1, 1]", l3[1][1])

# Does value exist
print("1 Exists", (1 in l1))

# Min & Max
print("Min ", min([1, 2, 3]))
print("Max ", max([1, 2, 3]))

# Slice out parts
print("1st 2", l1[0:2])
print("Every Other ", l1[0:-1:2])
print("Reverse ", l1[::-1])

# ----- LOOPS -----
# While : Execute while condition is True
w1 = 1
while w1 < 5:
    print(w1)
    w1 += 1

w2 = 0
while w2 <= 20:
    if w2 % 2 == 0:
        print(w2)
    elif w2 == 9:
        # Forces the loop to end all together
        break
    else:
        # Shorthand for i = i + 1
        w2 += 1
        # Skips to the next iteration of the loop
        continue
    w2 += 1

# Cycle through list
l4 = [1, 3.14, "Derek", True]
while len(l4):
    print(l4.pop(0))

# For Loop
# Allows you to perform an action a set number of times
# Range performs the action 10 times 0 - 9
# end="" eliminates newline
for x in range(0, 10):
    print(x, ' ', end="")
print('\n')

# Cycle through list
l4 = [1, 3.14, "Derek", True]
for x in l4:
    print(x)

# You can also define a list of numbers to
# cycle through
for x in [2, 4, 6]:
    print(x)

# You can double up for loops to cycle through lists
num_list = [[1, 2, 3], [10, 20, 30], [100, 200, 300]]

# ----- ITERATORS -----
# You can pass an object to iter() which returns
# an iterator which allows you to cycle
l5 = [6, 9, 12]
itr = iter(l5)
print(next(itr))  # Grab next value

# ----- RANGES -----
# The range() function creates integer iterables
print(list(range(0, 5)))

# You can define step
print(list(range(0, 10, 2)))

for x in range(0, 3):
    for y in range(0, 3):
        print(num_list[x][y])

# ----- TUPLES -----
# Tuples are just like lists except they are
# immutable
t1 = (1, 3.14, "Derek", False)

# Get length
print("Length ", len(t1))

# Get value / values
print("1st", t1[0])
print("Last", t1[-1])
print("1st 2", t1[0:2])
print("Every Other ", t1[0:-1:2])
print("Reverse ", t1[::-1])

# Everything you can do with lists you can do with
# tuples as long as you don't change values

# ----- DICTIONARIES -----
# Dictionaries are lists of key / value pairs
# Keys and values can use any data type
# Duplicate keys aren't allowed
heroes = {
    "Superman": "Clark Kent",
    "Batman": "Bruce Wayne"
}

villains = dict([
    ("Lex Luthor", "Lex Luthor"),
    ("Loki", "Loki")
])

print("Length", len(heroes))

# Get value by key
# Also heroes.get("Superman")
print(heroes["Superman"])

# Add more
heroes["Flash"] = "Barry Allan"

# Change a value
heroes["Flash"] = "Barry Allen"

# Get list of tuples
print(list(heroes.items()))

# Get list of keys and values
print(list(heroes.keys()))
print(list(heroes.values()))

# Delete
del heroes["Flash"]

# Remove a key and return it
print(heroes.pop("Batman"))

# Search for key
print("Superman" in heroes)

# Cycle through a dictionary
for k in heroes:
    print(k)

for v in heroes.values():
    print(v)

# Formatted print with dictionary mapping
d1 = {"name": "Bread", "price": .88}
print("%(name)s costs $%(price).2f" % d1)

# ----- SETS -----
# Sets are lists that are unordered, unique
# and while values can change those values
# must be immutable
s1 = set(["Derek", 1])

s2 = {"Paul", 1}

# Size
print("Length", len(s2))

# Join sets
s3 = s1 | s2
print(s3)

# Add value
s3.add("Doug")

# Remove value
s3.discard("Derek")

# Remove random value
print("Random", s3.pop())

# Add values in s2 to s3
s3 |= s2

# Return common values (You can include multiple
# sets as attributes)
print(s1.intersection(s2))

# All unique values
print(s1.symmetric_difference(s2))

# Values in s1 but not in s2
print(s1.difference(s2))

# Clear values
s3.clear()

# Frozen sets can't be edited
s4 = frozenset(["Paul", 7])


# ----- FUNCTIONS -----
# Functions provide code reuse, organization
# and much more
# Add 2 values using 1 as default
# You can define the data type using function
# annotations
def get_sum(num1: int = 1, num2: int = 1):
    return num1 + num2
print(get_sum(5, 4))

# Accept multiple values
def get_sum2(*args):
    sum = 0
    for arg in args:
        sum += arg
    return sum
print(get_sum2(1, 2, 3, 4))

# Return multiple values
def next_2(num):
    return num + 1, num + 2
i1, i2 = next_2(5)
print(i1, i2)

# A function that makes a function that
# multiplies by the given value
def mult_by(num):
    # You can create anonymous (unnamed functions)
    # with lambda
    return lambda x: x * num
print("3 * 5 =", (mult_by(3)(5)))

# Pass a function to a function
def mult_list(list, func):
    for x in list:
        print(func(x))
mult_by_4 = mult_by(4)
mult_list(list(range(0, 5)), mult_by_4)

# Create list of functions
power_list = [lambda x: x ** 2,
             lambda x: x ** 3,
             lambda x: x ** 4]

# ----- MAP -----
# Map is used to execute a function on a list
one_to_4 = range(1, 5)
times2 = lambda x: x * 2
print(list(map(times2, one_to_4)))

# ----- FILTER -----
# Filter selects items based on a function
# Print out the even values from a list
print(list(filter((lambda x: x % 2 == 0), range(1, 11))))

# ----- REDUCE -----
# Reduce receives a list and returns a single
# result
# Add up the values in a list
print(reduce((lambda x, y: x + y), range(1, 6)))

# ----- EXCEPTION HANDLING -----
# You can handle errors that would otherwise
# crash your program
# By giving the while a value of True it will
# cycle until a break is reached
while True:

    # If we expect an error can occur surround
    # potential error with try
    try:
        number = int(input("Please enter a number : "))
        break

    # The code in the except block provides
    # an error message to set things right
    # We can either target a specific error
    # like ValueError
    except ValueError:
        print("You didn't enter a number")

    # We can target all other errors with a
    # default
    except:
        print("An unknown error occurred")

print("Thank you for entering a number")

# ----- FILE IO -----
# We can save and read data from files
# We start the code with with which guarantees
# the file will be closed if the program crashes
# mode w overwrites file
# mode a appends
with open("mydata.txt", mode="w", encoding="utf-8") \
        as myFile:
    # You can write to the file with write
    # It doesn't add a newline
    myFile.write("Some random text\nMore random text\nAnd some more")

# Open a file for reading
with open("mydata.txt", encoding="utf-8") as myFile:
    # Use read() to get everything at once
    print(myFile.read())

# Find out if the file is closed
print(myFile.closed)

# ----- CLASSES OBJECTS -----
# Real world objects have
# attributes : height, weight
# capabilities : run, eat

# Classes are blueprints for creating objects
class Square:
    # init is used to set values for each Square
    def __init__(self, height="0", width="0"):
        self.height = height
        self.width = width

    # This is the getter
    # self is used to refer to an object that
    # we don't possess a name for
    @property
    def height(self):
        print("Retrieving the height")

        # Put a __ before this private field
        return self.__height

    # This is the setter
    @height.setter
    def height(self, value):

        # We protect the height from receiving
        # a bad value
        if value.isdigit():

            # Put a __ before this private field
            self.__height = value
        else:
            print("Please only enter numbers for height")

    # This is the getter
    @property
    def width(self):
        print("Retrieving the width")
        return self.__width

    # This is the setter
    @width.setter
    def width(self, value):
        if value.isdigit():
            self.__width = value
        else:
            print("Please only enter numbers for width")

    def get_area(self):
        return int(self.__width) * int(self.__height)

# Create a Square object
square = Square()
square.height = "10"
square.width = "10"
print("Area", square.get_area())

# ----- INHERITANCE & POLYMORPHISM-----
# When a class inherits from another it gets all
# its fields and methods and can change as needed
class Animal:
    def __init__(self, name="unknown", weight=0):
        self.__name = name
        self.__weight = weight

    @property
    def name(self, name):
        self.__name = name

    def make_noise(self):
        return "Grrrrr"

    # Used to cast to a string type
    def __str__(self):
        return "{} is a {} and says {}".format (self.__name, type(self).__name__, self.make_noise())

    # Magic methods are used for operator
    # overloading
    # Here I'll define how to evaluate greater
    # than between 2 Animal objects
    def __gt__(self, animal2):
        if self.__weight > animal2.__weight:
            return True
        else:
            return False
    # Other Magic Methods
    # __eq__ : Equal
    # __ne__ : Not Equal
    # __lt__ : Less Than
    # __gt__ : Greater Than
    # __le__ : Less Than or Equal
    # __ge__ : Greater Than or Equal
    # __add__ : Addition
    # __sub__ : Subtraction
    # __mul__ : Multiplication
    # __div__ : Division
    # __mod__ : Modulus

# Dog inherits everything from Animal
class Dog(Animal):
    def __init__(self, name="unknown", owner="unknown", weight=0):
        # Have the super class handle initializing
        Animal.__init__(self, name, weight)
        self.__owner = owner

    # Overwrite str
    def __str__(self):
        # How to call super class methods
        return super().__str__() + " and is owned by " + \
        self.__owner

animal = Animal("Spot", 100)
print(animal)

dog = Dog("Bowser", "Bob", 150)
print(dog)

# Test the magic method
print(animal > dog)

# Polymorphism in Python works differently from
# other languages in that functions accept any
# object and expect that object to provide the
# needed method

# This isn't something to dwell on. Just know
# that if you call on a method for an object
# that the method just needs to exist for
# that object to work.

# ----- THREADS -----
# Threads are blocks of code that takes turns
# executing
def execute_thread(i):
    # strftime or string formatted time allows you to
    # define how the time is displayed.
    # You could include the date with
    # strftime("%Y-%m-%d %H:%M:%S", gmtime())

    # Print when the thread went to sleep
    print("Thread {} sleeps at {}".format(i,
                                          time.strftime("%H:%M:%S", time.gmtime())))

    # Generate a random sleep period of between 1 and
    # 5 seconds
    rand_sleep_time = random.randint(1, 5)

    # Pauses execution of code in this function for
    # a few seconds
    time.sleep(rand_sleep_time)

    # Print out info after the sleep time
    print("Thread {} stops sleeping at {}".format(i,
                                                  time.strftime("%H:%M:%S", time.gmtime())))

for i in range(10):
    # Each time through the loop a Thread object is created
    # You pass it the function to execute and any
    # arguments to pass to that method
    # The arguments passed must be a sequence which
    # is why we need the comma with 1 argument
    thread = threading.Thread(target=execute_thread, args=(i,))
    thread.start()

    # Display active threads
    # The extra 1 is this for loop executing in the main
    # thread
    print("Active Threads :", threading.activeCount())

    # Returns a list of all active thread objects
    print("Thread Objects :", threading.enumerate())

# Regular expressions allow you to locate and change
# strings in very powerful ways.
# They work in almost exactly the same way in every
# programming language as well.

# Regular Expressions (Regex) are used to
# 1. Search for a specific string in a large amount of data
# 2. Verify that a string has the proper format (Email, Phone #)
# 3. Find a string and replace it with another string
# 4. Format data into the proper form for importing for example

# import the Regex module
import re

# ---------- Was a Match Found ----------

# Search for ape in the string
if re.search("ape", "The ape was at the apex"):
    print("There is an ape")

# ---------- Get All Matches ----------

# findall() returns a list of matches
# . is used to match any 1 character or space
allApes = re.findall("ape.", "The ape was at the apex")

for i in allApes:
    print(i)

# finditer returns an iterator of matching objects
# You can use span to get the location

theStr = "The ape was at the apex"

for i in re.finditer("ape.", theStr):

    # Span returns a tuple
    locTuple = i.span()

    print(locTuple)

    # Slice the match out using the tuple values
    print(theStr[locTuple[0]:locTuple[1]])

# Here I'll show you how to work with SQLite databases
# in Python

# A database makes it easy for you to organize your
# data for storage and fast searching
import sqlite3
import sys
import csv
def printDB():
    # To retrieve data from a table use SELECT followed
    # by the items to retrieve and the table to
    # retrieve from

    try:
        result = theCursor.execute("SELECT id, FName, LName, Age, Address, Salary, HireDate FROM Employees")

        # You receive a list of lists that hold the result
        for row in result:
            print("ID :", row[0])
            print("FName :", row[1])
            print("LName :", row[2])
            print("Age :", row[3])
            print("Address :", row[4])
            print("Salary :", row[5])
            print("HireDate :", row[6])

    except sqlite3.OperationalError:
        print("The Table Doesn't Exist")

    except:
        print("Couldn't Retrieve Data From Database")

# ---------- END OF FUNCTIONS ----------

# connect() will open an SQLite database, or if it
# doesn't exist it will create it
# The file appears in the same directory as this
# Python file
db_conn = sqlite3.connect('test.db')

print("Database Created")

# A cursor is used to traverse the records of a result
theCursor = db_conn.cursor()

# execute() executes a SQL command
# We organize our data in tables by defining their
# name and the data type for the data

# We define the table name
# A primary key is a unique value that differentiates
# each row of data in our table
# The primary key will auto increment each time we
# add a new Employee
# If a piece of data is marked as NOT NULL, that means
# it must have a value to be valid

# NULL is NULL and stands in for no value
# INTEGER is an integer
# TEXT is a string of variable length
# REAL is a float
# BLOB is used to store binary data

# You can delete a table if it exists like this
# db_conn.execute("DROP TABLE IF EXISTS Employees")
# db_conn.commit()

try:
    db_conn.execute("CREATE TABLE Employees(ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, FName TEXT NOT NULL, LName TEXT NOT NULL, Age INT NOT NULL, Address TEXT, Salary REAL, HireDate TEXT);")

    db_conn.commit()

    print("Table Created")

except sqlite3.OperationalError:
    print("Table couldn't be Created")


# To insert data into a table we use INSERT INTO
# followed by the table name and the item name
# and the data to assign to those items

db_conn.execute("INSERT INTO Employees (FName, LName, Age, Address, Salary, HireDate)"
"VALUES ('Derek', 'Banas', 41, '123 Main St', '500,000', date('now'))")

db_conn.commit()

print("Employee Entered")

# Print out all the data in the database
printDB()

# Closes the database connection
db_conn.close()

# ——- myfunc.py ——-

# ---------- RECURSIVE FUNCTIONS ----------
# A function that refers to itself is a recursive function

# Calculating factorials is commonly done with a recursive
# function 3! = 3 * 2 * 1
def factorial(num):
    # Every recursive function must contain a condition
    # when it ceases to call itself
    if num <= 1:
        return 1
    else:

        result = num * factorial(num - 1)
        return result

# 1st : result = 4 * factorial(3) = 4 * 6 = 24
# 2nd : result = 3 * factorial(2) = 3 * 2 = 6
# 3rd : result = 2 * factorial(1) = 2 * 1 = 2

# ——— MODULES ———
import myfunc
print(myfunc.factorial(4))

# OR

from myfunc import factorial
print(factorial(4))

# ——— GUI DEVELOPMENT WITH TKINTER ———

from tkinter import *
from tkinter import ttk

class Calculator:

    # Stores the current value to display in the entry
    calc_value = 0.0

    # Will define if this was the last math button clicked
    div_trigger = False
    mult_trigger = False
    add_trigger = False
    sub_trigger = False

    # Called anytime a number button is pressed
    def button_press(self, value):

        # Get the current value in the entry
        entry_val = self.number_entry.get()

        # Put the new value to the right of it
        # If it was 1 and 2 is pressed it is now 12
        # Otherwise the new number goes on the left
        entry_val += value

        # Clear the entry box
        self.number_entry.delete(0, "end")

        # Insert the new value going from left to right
        self.number_entry.insert(0, entry_val)

        # Returns True or False if the string is a float
    def isfloat(self, str_val):
        try:

            # If the string isn't a float float() will throw a
            # ValueError
            float(str_val)

            # If there is a value you want to return use return
            return True
        except ValueError:
            return False

    # Handles logic when math buttons are pressed
    def math_button_press(self, value):

        # Only do anything if entry currently contains a number
        if self.isfloat(str(self.number_entry.get())):

            # make false to cancel out previous math button click
            self.add_trigger = False
            self.sub_trigger = False
            self.mult_trigger = False
            self.div_trigger = False

            # Get the value out of the entry box for the calculation
            self.calc_value = float(self.entry_value.get())

            # Set the math button click so when equals is clicked
            # that function knows what calculation to use
            if value == "/":
                print("/ Pressed")
                self.div_trigger = True
            elif value == "*":
                print("* Pressed")
                self.mult_trigger = True
            elif value == "+":
                print("+ Pressed")
                self.add_trigger = True
            else:
                print("- Pressed")
                self.sub_trigger = True

            # Clear the entry box
            self.number_entry.delete(0, "end")

    # Performs a mathematical operation by taking the value before
    # the math button is clicked and the current value. Then perform
    # the right calculation by checking what math button was clicked
    # last
    def equal_button_press(self):

        # Make sure a math button was clicked
        if self.add_trigger or self.sub_trigger or self.mult_trigger or self.div_trigger:

            if self.add_trigger:
                solution = self.calc_value + float(self.entry_value.get())
            elif self.sub_trigger:
                solution = self.calc_value - float(self.entry_value.get())
            elif self.mult_trigger:
                solution = self.calc_value * float(self.entry_value.get())
            else:
                solution = self.calc_value / float(self.entry_value.get())

            print(self.calc_value, " ", float(self.entry_value.get())," ", solution)

            # Clear the entry box
            self.number_entry.delete(0, "end")

            self.number_entry.insert(0, solution)


    def __init__(self, root):
        # Will hold the changing value stored in the entry
        self.entry_value = StringVar(root, value="")

        # Define title for the app
        root.title("Calculator")

        # Defines the width and height of the window
        root.geometry("430x220")

        # Block resizing of Window
        root.resizable(width=False, height=False)

        # Customize the styling for the buttons and entry
        style = ttk.Style()
        style.configure("TButton",
        font="Serif 15",
        padding=10)

        style.configure("TEntry",
        font="Serif 18",padding=10)

        # Create the text entry box
        self.number_entry = ttk.Entry(root,
        textvariable=self.entry_value, width=50)
        self.number_entry.grid(row=0, columnspan=4)

        # ----- 1st Row -----

        self.button7 = ttk.Button(root, text="7", command=lambda: self.button_press('7')).grid(row=1, column=0)

        self.button8 = ttk.Button(root, text="8", command=lambda: self.button_press('8')).grid(row=1, column=1)

        self.button9 = ttk.Button(root, text="9", command=lambda: self.button_press('9')).grid(row=1, column=2)

        self.button_div = ttk.Button(root, text="/", command=lambda: self.math_button_press('/')).grid(row=1, column=3)

        # ----- 2nd Row -----

        self.button4 = ttk.Button(root, text="4", command=lambda: self.button_press('4')).grid(row=2, column=0)

        self.button5 = ttk.Button(root, text="5", command=lambda: self.button_press('5')).grid(row=2, column=1)

        self.button6 = ttk.Button(root, text="6", command=lambda: self.button_press('6')).grid(row=2, column=2)

        self.button_mult = ttk.Button(root, text="*", command=lambda: self.math_button_press('*')).grid(row=2, column=3)

        # ----- 3rd Row -----

        self.button1 = ttk.Button(root, text="1", command=lambda: self.button_press('1')).grid(row=3, column=0)

        self.button2 = ttk.Button(root, text="2", command=lambda: self.button_press('2')).grid(row=3, column=1)

        self.button3 = ttk.Button(root, text="3", command=lambda: self.button_press('3')).grid(row=3, column=2)

        self.button_add = ttk.Button(root, text="+", command=lambda: self.math_button_press('+')).grid(row=3, column=3)

        # ----- 4th Row -----

        self.button_clear = ttk.Button(root, text="AC", command=lambda: self.button_press('AC')).grid(row=4, column=0)

        self.button0 = ttk.Button(root, text="0", command=lambda: self.button_press('0')).grid(row=4, column=1)

        self.button_equal = ttk.Button(root, text="=", command=lambda: self.equal_button_press()).grid(row=4, column=2)

        self.button_sub = ttk.Button(root, text="-", command=lambda: self.math_button_press('-')).grid(row=4, column=3)

# Get the root window object
root = Tk()

# Create the calculator
calc = Calculator(root)

# Run the app until exited 
root.mainloop()