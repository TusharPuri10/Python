''' Indentation refers to the spaces at the beginning of a code line.

Where in other programming languages the indentation in code is
 for readability only, the indentation in Python is very important.

Python uses indentation to indicate a block of code.

In Python, variables are created when you assign a value to it:

x = 5
y = "Hello, World!"

x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0

x = 5
y = "John"
print(type(x))
print(type(y))

A variable name must start with a letter or the underscore character
A variable name cannot start with a number
A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
Variable names are case-sensitive (age, Age and AGE are three different variables)

x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

x = y = z = "Orange"
print(x)
print(y)
print(z)

fruits = ["apple", "banana", "cherry"]   elements in list and the items to unpack should be equal
x, y, z = fruits
print(x)
print(y)
print(z)

x = "Python is awesome"
print(x)

x = "Python"
y = "is"
z = "awesome"
print(x, y, z) Python is awesome

x = "Python"
y = "is"
z = "awesome"
print(x + y + z) Pythonisawesome

x = 5
y = "John"
print(x + y) # error
print(x,y) 5 john
print(str(x)+y) 5John


Variables that are created outside of a function 
(as in all of the examples above) are known as global variables.

Global variables can be used by everyone, both inside of functions and outside.

x = "awesome"

def myfunc():
  print("Python is " + x) Python is awesome

myfunc()

x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x) Python is fantastic

myfunc()

print("Python is " + x) Python is awesome

global keyword

    def myfunc():
        x = "fantastic"

    myfunc()

    print("Python is " + x) # error

    def myfunc():
        global x
        x = "fantastic"

    myfunc()

    print("Python is " + x) Python is fantastic

DATA TYPES

In programming, data type is an important concept.

Variables can store data of different types, and different types can do different things.

Python has the following data types built-in by default, in these categories:

Text Type:	str
Numeric Types:	int, float, complex
Sequence Types:	list, tuple, range
Mapping Type:	dict
Set Types:	set, frozenset
Boolean Type:	bool
Binary Types:	bytes, bytearray, memoryview
None Type:	NoneType

You can get the data type of any object by using the type() function:

x = ["apple", "banana", "cherry"]
print(type(x)) list

x = ("apple", "banana", "cherry")
print(type(x)) tuple

x = {"name" : "John", "age" : 36}
print(type(x)) dict

x = True
print(type(x)) bool

 **** see image for types of data types****
 
range(0, 6) 5 baar chalega 0 se 5

x = str("Hello World")	str	
x = int(20)	int	
x = float(20.5)	float	
x = complex(1j)	complex	
x = list(("apple", "banana", "cherry"))	list	
x = tuple(("apple", "banana", "cherry"))	tuple	
x = range(6)	range	
x = dict(name="John", age=36)	dict	
x = set(("apple", "banana", "cherry"))	set	
x = frozenset(("apple", "banana", "cherry"))	frozenset	
x = bool(5)	bool	
x = bytes(5)	bytes	
x = bytearray(5)	bytearray	
x = memoryview(bytes(5))	memoryview

things about numbers in images in photos.

STRINGS are immutable

a = "Hello"
print(a) Hello

a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""  three double quotes or single quotes
print(a)


Strings are Arrays
Like many other popular programming languages,
 strings in Python are arrays of bytes representing unicode characters.

However, Python does not have a character data type,
 a single character is simply a string with a length of 1.

Square brackets can be used to access elements of the string.

a = "Hello, World!"
print(a[1]) e

for x in "banana":
  print(x)
  b
  a
  n
  a
  n
  a
a = "Hello, World!"
print(len(a)) 13

txt = "The best things in life are free!"
print("free" in txt) True

fruits = ["apple", "banana"]
print("apple" in fruits) True

txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")

  txt = "The best things in life are free!"
print("expensive" not in txt) True

txt = "The best things in life are free!"
if "expensive" not in txt:
  print("No, 'expensive' is NOT present.") 

  Slicing keval usi line x
You can return a range of characters by using the slice syntax.

b = "Hello, World!"
print(b[2:5]) llo

b = "Hello, World!"
print(b[:5]) Hello

b = "Hello, World!"
print(b[2:]) llo, World!

b = "Hello, World!"
print(b[-5:-2]) last ka -1 se start hota hai
orld

String = 'ASTRING'
 
# Using slice constructor
s1 = slice(3) 012
s2 = slice(1, 5, 2) 13
s3 = slice(-1, -12, -2) -1 -3 -5 -7
 
print("String slicing")
print(String[s1]) AST
print(String[s2]) SR
print(String[s3]) GITA

arr[start:stop]         # items start through stop-1
arr[start:]             # items start through the rest of the array
arr[:stop]              # items from the beginning through stop-1
arr[:]                  # a copy of the whole array
arr[start:stop:step]    # start through not past stop, by step

a = "Hello, World!"
print(a.upper()) HELLO, WORLD
print(a) Hello, World! because strings are immutable


a = "Hello, World!"
print(a.lower())

a = " Hello, World! "
print(a
print(a.strip()) # returns "Hello, World!"
print(a.rstrip()) # returns "Hello, World! "
print(a.lstrip()) # returns " Hello, World!"

a = "Hello, World!"
print(a.replace("H", "J"))


The split() method returns a list where the text between the specified separator becomes the list items.

Example
The split() method splits the string into substrings if it finds instances of the separator:

a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']

a = "Hello"
b = "World"
c = a + b
print(c) HelloWorld
c = a + " " + b
print(c) Hello World

txt = "We are the so-called \"Vikings\" from the north."

+	Addition	x + y	
-	Subtraction	x - y	
*	Multiplication	x * y	
/	Division	x / y	
%	Modulus	x % y	
**	Exponentiation	x ** y	
//	Floor division	x // y

and 	Returns True if both statements are true	x < 5 and  x < 10	
or	Returns True if one of the statements is true	x < 5 or x < 4	
not	Reverse the result, returns False if the result is true	not(x < 5 and x < 10)

is 	Returns True if both variables are the same object	x is y	
is not	Returns True if both variables are not the same object	x is not y

in 	Returns True if a sequence with the specified value is present in the object	x in y	
not in	Returns True if a sequence with the specified value is not present in the object	x not in y

x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is z)

# returns True because z is the same object as x

print(x is y)

# returns False because x is not the same object as y, even if they have the same content

print(x == y)

# to demonstrate the difference betweeen "is" and "==": this comparison returns True because x is equal to y

List are mutable
Lists are used to store multiple items in a single variable.

Lists are one of 4 built-in data types in Python used to store collections of data, the other 3 are Tuple, Set, and Dictionary, all with different qualities and usage.

Lists are created using square brackets:

List items are ordered, changeable, and allow duplicate values.

List items are indexed, the first item has index [0], the second item has index [1] etc.

When we say that lists are ordered, it means that the items have a defined order, and that order will not change.

If you add new items to a list, the new items will be placed at the end of the list

thislist = ["apple", "banana", "cherry"]
print(len(thislist)) 3

list constructor
thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)

range of index is same as string slicing

thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)

thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
thislist = thislist + tropical
print(thislist)

list me append-pop,insert-remove

thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)

Remove the first item:

thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)

thislist = ["apple", "banana", "cherry"]
del thislist
delete entire list

thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)




tuple is same as list only tuple is immutable and syntax()

set is mutable but cannot have repeated elements and syntax{}
set me accessing is same but

thisset = {"apple", "banana", "cherry"}

thisset.add("orange")

print(thisset)

thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}

thisset.update(tropical)

print(thisset)

thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]

thisset.update(mylist)

print(thisset)

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict["brand"])

As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.
Dictionaries are changeable, meaning that we can change, add or remove items after the dictionary has been created.


 '''
