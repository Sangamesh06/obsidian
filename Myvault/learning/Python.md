in obsidian always count 3 lines less for code error than given in syntax error warning
sometime proper error warning are not given

```run-python
price = 10
print(price)

```


```run-python
print("sangamesh")  
print("2nd line")  
print("*" * 10)  
```
  
# variable  
```run-python
price = 10 #number are stored as binary 10101 
price = 20  
print(price) 
rating = 4.9
name = "san"
is_done = True
print(is_done)

```

  Integer : number without decimal part
 float : number with decimal part
 string : sequence of character enclosed in double or single quotes
 boolean : True , False
 python is case sensitive


```run-python
name = "john smith"
age = 20
is_old = false
```

# getting Input
```run-python
name = input('What is your name ') #add space after #question so that after question we have some space
print('hi ' + name) 
#add space after hi  so that after hi we have some space
```




expression : piece of code that outputs a value 

'hi' + name : we are concatenation name and hi string
it returns concatenated string

```run-python
name = input("what is your name ")
color = input("what is your favourite color ")
print(name + " likes " + color)
```


# Type conversion
```run-python
birth_year = input("Birth year : ")
age = 2024 - int(birth_year)
print(type(birth_year))
print(type(age)) #type is a funcction that gives us a type of variable
#int() : converts  string to integer
#float() : converts  string to float
#bool() : converts  string to bool
print(age)
```


```run-python
weight = input("enter your weight")
kg = int(weight) * 0.45
print("your weight in kg is ")
print(kg)
```

we can not concatenate string and int or float we can only concatenate string with string itself
so code 
```run-python
kg  = 10
print("your weight in kgs " + kg) #gives error
```

whatever input we take from input it is considered as string in the above programme birth year we entered is considered ast "2001" and not 2001 so we need to convert that string to integer before doing mathematical operation

# diffrent cases for single and double quotes
if there is apostrophe in the string that we want to print then we need to use double quotes for the same otherise it will give error

```run-python
print("sangu's books")
print('sangu's books')
```

if there is a need to have double quote in a string that we want to print we use single quoyes overall

ex
```run-python
print('python for "begineers"')

```

## triple quote string

```run-python
course = '''Hi JOhn ,
here is our first email to you

Thank you ,
the Support team 
'''
print(course)
```

# indexes
indexes start at 0 in python 
index 0 gives the first character of string
```run-python
course = "hello sangamesh"
print(course[0])
print(course[5])
```


## negative indexes
```run-python
course = "python for beginers"
print(course[-1]) #first charectar from last
print(course[-2]) #second character from last

```


# slicing
```run-python
course = "python for beginners"
print(course[0:3])
#first integer is inclusive and second is exclusive prints. charecter of index  0 , 1 , 2
#function aslo has some default value so i f you dont give them it takes default value like
print(course[0:]) #prints from index 0 to last charecter(default if on integer is given for second
print(course[:4]) #takes 0 as intitial index if no value is given
print(course[:])
another = course[:]
name = "jennifer"
print(name[1:-1])

```


```run-python
first = "john"
last = "smith"
message = first + '[' + last + '] is a code '
print(message)


```

# formatted string

```run-python
msg = f'{first} [{last}] is a coder'
print(msg)

```


```run-python
course = "Sangameh"
print(len(course))
print(course.upper())
print(course)
print(course.lower())
```

upper function do not change the string it just capitalises the string and prints the same it does not change the original string

len  is a general purpose 
find is a function it return the index of first character appearance in string of given character
replace is a fuction that replace given string in a string with given string
in is a function that telll whether particcular string is in a longer string or not
in is also case sensitive

```run-python
name = "sangamesh somashetti"
print(name.find('a'))
print(name.find('me'))
print(name.replace("sangamesh", "sangu"))
print("soma" in name)
print("Soma" in name)
```



replace is also case sensitive
it can also be used to replace single character
find is case sensitive
in can be used to find single character also


# Arithmetic operations

```run-python
print(10/3)
print(10//3)
print(10%3)
print(10**3)
```

/ : gives float or int
// : gives int as output
% : gives remainder as a result
** : exponent operator

augumented assignment operator

```run-python
x = 10
x = x + 3
print(x)
x +=3 
print(x)
x -= 3
print(x)
```

# operator precedence

```run-python
x = 10 + 3 * 2
print(x)
y = 10 + 3 * 2 ** 2
print(y)
z = (10 + 3) * 2 ** 2
print(z)
```

order  of operator
paranthesis
exponentiation
multiplication or division
addition or subtraction

## builtin function to work with numbers

```run-python
x = 2.9
print(abs(-2.9))
print(round(x))  
```

module contain reusable functions
math is a python module in order to use function inside it we. need to import the same using statement 
import modulename

 
```run-python
import math
x = 2.9
print(math.ceil(2.9))
print(math.floor(x))
```

link to read about pyhton3 math library functions
https://docs.python.org/3/library/math.html

use python3 and not python2 since it is chaged

# if statements

```run-python
is_hot = True

if is_hot :
	print("it is a hot day")
	print("drink plenety of water")
else :
	print("it is a lovely day")
```



```run-python
is_hot = False
is_cold = False
if is_hot :
	print("it is a hot day")
	print("drink plenety of water")
elif is_cold :
	print("it is a cold day")
	print("wear warm clothes")
else :
	print("it is a lovely day")
```

```run-python
good_credit = True
price = 1000
if good_credit :
	amount = 1000 * 10/100

else :
	amount = 1000 * 20/100
print(amount)

```

# logical operator in python

```run-python

high_income = True
high_credit = True
if high_income and high_credit :
	print("eligible for loan")

```


and : both condition true
or : at least one
not : negates the value

```run-python

high_income = True
high_credit = True
criminal_record = False
if high_income and not criminal_record :
	print("eligible for loan")
```



# comparison operator 

```run-python
temp = 30
if temp > 30 :
	print("it is a hot day")
else :
	print("it is not a hot day")

```


```
comparison operator
> , >= , <,  <= , == , !=
```

```run-python
name = "sangamesh"
if len(name) < 3 :
	print("name is short")
elif len(name) > 50:
	print("name is long")
else :
	print("name looks good")
	
```

generally methods are return like this using dot operator like upper and lower and replce
name = "sangamesh"
name.lower()
name.upper()

but generi c funcctions are applied like this 
len(name)

```run-python
weight = int(input("weight : "))
unit = input('(l)bs or (k)g: ')
if unit.upper() == "L":
	converted = weight * 0.45
	print(f"youy are {converted} kilos")
else :
	converted = weight / 0.45 
	print(f"you are {converted} pounds")
	

```

# loops

## while loops
```run-python
i = 1
while i <= 5 :
	print('*' * i)
	i = i + 1


```

### guess game
```run-python
secret_number = 9  
guess_count    = 0  
guess_limit = 3  
  
while guess_count < guess_limit :  
    guess = int(input("guess: "))  
    guess_count += 1  
    if guess == secret_number :  
        print("you won! ")  
        break  
    else :  
        pass
        
else :
	print("soryy you failed")
```

break will break the outermost loop and comes program comes out of the loop

while can also have else part it executes after while condition is false here if break condition hits and programme comes out of while loop then else will not be executed otherwise else is executed

### car game
```run-python
command = ""  
started = False  
while True:  
    command = input("> ").lower()  
    if command == "start" :  
        if started == True :  
            print("car is already started")  
        else :  
            started = True  
            print("car started")  
    elif command == "stop":  
        if not started == True:  
            print("car is already stopped")  
        else :  
            started = False  
            print("car stopped")  
    elif command == "help":  
        print("start : to start the car")  
        print("stop : to stop  the car")  
        print("quit : to quit the game")  
    elif command == "quit" :  
        break  
    else :  
        print("i do not understand that")

```


## for loops
it is used to iterate over item of collection

```run-python
for item in "python" :
	print(item)


```

```run-python
for item in ["sangu" , "sai" , "vijay"]:
	print(item)
```

range is builtin function in python that is used to give number in sequence with starting , ending , jump
starting point : 5(inclusive)(default : 0)
ending point : 10(exclusive)
step or jump :  default(1)

```run-python
for item in range(5):
	print(item)
```
```

```


```run-python
for item in range(5,10):
	print(item)

```

```run-python
for item in range(5,10,2):
	print(item)

```


```run-python
prices = [10,20,30]  
total = 0  
for price in prices:  
    total += price  
print(f"total : {total}")

```


## nested loops
loop inside loop

```run-python
a = 10
if a == 10:
	b = 5
print(b)

```

In Python, variables defined within an `if`, `while`, or `for` block are available outside of their respective blocks. This behavior is different from some other programming languages where variables defined within a block are limited to that block's scope.
but this is not the case in java , javascript

challenge
```run-python
num = [5,2,5,2,2]
for item in num:
	print("x" * item)

```


```run-python
num = [5,2,5,2,2]
for item in num:
	output = ""
	for count in range(item):
		output += 'x'
	print(output)

```


```run-python
num = [2,2,2,2,5]
for item in num:
	output = ""
	for count in range(item):
		output += 'x'
	print(output)
```


```run-python
names = ["john" , "sangu" , "sai"]  
print(names)  
print(names[2])  
print(names[-2])  
print(names[0:2])  
print(names[2:0])  #empty bracket
print(names[2:-1]) #empty bracket
print(names[1:-1])  
print(names[:])
```

original list names is not modified




```run-python
names = ["john" , "sangu" , "sai"]  
names[0] = "jon"  
print(names)

```


```run-python
numbers = [3,25,5,565]  
max = numbers[0]  
for i in numbers:  
    if (i > max):  
        max = i  
print(max)

```


```run-python
matrix = [
[1,2,3],
[4,5,6],
[7,8,9]
]
matrix[0][1] = 4
for row in matrix :
	for col in row :
		print(col)

```

```run-python

numbers = [5,2,1,5,7,4]
numbers.append(20)
print(numbers)
numbers.insert(0,10)
print(numbers)
numbers.index(5)
print(numbers)
#numbers.index(50)
print(numbers)
numbers.in(50)
print(numbers)
numbers.remove(5)
print(numbers)
numbers.pop()
print(numbers)
print(numbers.count(5))
print(numbers.sort())
print(numbers)
numbers.reverse()
print(numbers)
numbers2 = numbers.copy()
print(numbers2)
numbers.append(10)
print(numbers)
numbers.clear()
print(numbers)
```


programme to remove duplicate in list
```run-python
numbers = [1,2,2,3,4]
unique = []
for num in numbers :
	if num not in unique:
		unique.append(num)
print(unique)
```



tuples
immutable list
defined using ()
less functions available 
can not be changed 
```
listnumbers = [1,2,3]
tupnumbers = (1,2,3)

```
unpacking numbers 
can be used for both list and tuple

```run-python
coordinates = (1,2,3)
#x = coordinates[0]
#y = coordinates[1]
#z = coordinates[2]

x , y, z = coordinates
print(x)
print(y)
print(z)

```

dictionary
in dictionary keys has to be unique 
we get key error or unavailable keys
we can do same using get
try to use get since if we can handle exceptions using cust.get("date", default-value)

```run-python
cust = {
    "name" : "john",
    "age":30,
    "is_verified":True
}
print(cust["name"])
#print(cust["date"])
print(cust.get("date"))
```


programme to interpret numbers

```run-python
cust["name"] = "sangu"
cust["date"] = "100"
print(cust["name"])
#print(cust["date"])
print(cust.get("date"))

numb = input("give a number")
numbers = {
        "1" : "one",
        "2": "two",
        "3" : "three",
        "4" : "four"
}
output = ""
for ch in numb :
    output = output + numbers.get(ch, "!") + " "
print(output)
```

```run-python
message  = input(">")
output = ""
words = message.split(' ')
emojis = {
        ":)" : "😀",
        ":(":"😁"
}
for word in  words:
    output += emojis.get(word , word) + "  "
print(output)
```



# functions

syntax 
def function_name



def : keyword to define function
function_name(): use underscore if it has more than one word
use expressive name for function
indent function body
print("hi there")
function is called using function_name()
call function after defining otherwise it will throw error 
parameter : placeholder for holding info
arguments : value passed to function while calling function
function can have zero or more parameters and while calling the same we need to pass the respective arguments otherwise it will raise the error
## positional arguments : the order of argument matter (1st argument is applied to first parameter and second argument is applied to second argument)

```run-python
def greet_user():
	print("hello")
	print("welcocme abroad")
print("start")
greet_user()
print("finish")
def greet_username(name):
	print(f'hello {name}')
	print("welcocme abroad")
print("start")
greet_username("sangu")
print("finish")
def greet_users(name, surname):
	print(f'hello {name}')
	print(f'hello {surname}')
	print("welcocme abroad")
print("start")
greet_users("mona" , "darling")
print("finish")
```


## keyword argument : arguments when order of argument does not matter
example 
```run-python
def greet_users(name, surname):
	print(f'hello {name}')
	print(f'hello {surname}')
	print("welcocme abroad")
greet_users(surname = "mona" , name = "darling")
```

we write respective parameter name before argument  while calling for functions so order does not matter
generally use keyword arguments when passing numeric as arguments

calc_cost(total = 50 , shipping = 5 , disc = 0.1)


keyword argument should always come after positional arguments

```run-python
greet_users(first_name = "mona" , "darling")

```


```run-python
greet_users( "mona" ,surname =  "darling")
```


## return statement
by default all the function return  none if there is no return statement


```run-python
print(greet_user())
```

emoji converter
```run-python
def emoji(message):  
    output = ""  
    words = message.split(' ')  
    emojis = {  
        ":)": "😀",  
        ":(": "😁"  
    }  
    for word in words:  
        output += emojis.get(word, word) + "  "  
    return output  
print(emoji("hello :)"))

```

# errors and exceptions

in programming exit code is zero success other than that it is crash
exceptions
try and except blocks
```run-python
try :  
    age = int(input('age: '))  
    income = 2000  
    risk = income/age  
    print(age)  
except ZeroDivisionError:  
    print("age can not be zero")  
except ValueError:  
    print("invalid value")

```
 ZeroDivisionError : raised when there is case of division by zero
  ValueError : raised when the data obtained is not propertype 
  example 
	  expected : integer
	  got : string
write except cases for all the exception you see can occur

# comments
single line comments : 

dont use comment to explain code if code changed you to change respective comments
use code to explain about assumptions you have made

```run-python
#single line comments
"""
"hello sangamesh"

"""
print("hello sangamesh")

```


# classes in python

use pascal naming convention for naming classes
every first letter of word is capital
class is keyword to define new class
methods are functions defined in the class
attributes the variables present in the class
python does not like empty classes
after defining class write some properties or  function write pass otherwise you will get indentation error 
```run-python
class Point:  
    def move(self):  
        print("move")  
  
    def draw(self):  
        print("draw")

```

## objects
objects are instances of class
we reate a new object of class by calling class like this objectcname = className()


```run-python
#class EmailClient  
class Point:  
    def move(self):  
        print("move")  
  
    def draw(self):  
        print("draw")  
  
  
point1 = Point()  
point1.x = 10  
point1.y = 20  
print(point1.x)  
point1.draw()  
  
point2 = Point()  
print(point2.x) #throws error

```


## constructor
it is a function that is called during creating an object
it has name __init__

```run-python
class Point:
	def __init__(self,x,y):
		self.x = x
		self.y = y
point1 = Point(10,20)
print(point1.x)
point1.x = 30
print(point1.x)
```


## self keyword
it is reference to current object
```run-python
class Person:  
    def __init__(self , name):  
        self.name = name  
  
    def talk(self):  
        print(f'my name is {self.name}')  
  
jon = Person("john smith")  
bob = Person("bob smith")
print(jon.name)  
print(bob.name)  
jon.talk()
bob.talk()
```

after defining class write some properties or  function write pass otherwise you will get indentation error 


## inheritance

```run-python
class Mammal:  
    def walk(self):  
        print("walk")  
  
class Dog(Mammal):  
    def bark(self):
	    print("bark") 
  
class Cat(Mammal):  
    def be_annoying(self):
	    print("annoying")  
  
san = Dog()  
sun = Cat()
san.walk()
san.bark()
sun.be_annoying()

```



# Modules

modules in python is basically file with code

they have related functions in one file 
we can import all the functions in that module using import statement

generally in ide if the function is builtin they will have same as color as print
it is not good to use builtin function name in code so refactor the same 
we can refactor variable name in pycharm using shortcut shift + f6


modulename.py file

```run-python
def laugh():  
    print("heeheehee")  
  
def cry():  
    print("uuuuuu")  
  
  
def maximum(arr):  
    max = arr[0]  
    for i in arr:  
        if i > max:  
            max = i  
    print(max)
```


test.py file

```run-python
# import whole module  
import modulename  
  
# import specific functions from  module  
from modulename import cry  
  
cry()  
modulename.laugh()  
  
modulename.maximum([1,2,3,6,5,4])
```


# packages
package is a directory or folder that contain similar module

to create a package 
create a new directory and create a new file inside it name __init__.py then python considers it as package

otherwise in pycharm we can do using the same usng shortcut
in order for us to import module from package we need to use package.modulename  rather than just modulename

```run-python
import ecommerce.shopping
ecommerce.shopping.calc_shipping()


```


to access function calc_shipping defined inside shipping module of ecommerce package  
we have to access using ecomerce.shipping.calc_shipping  
  
another convention  
import individual function from shipping module from ecommerce package  
from ecommerce.shipping import  calc_shipping, calc_tax  
calc_shipping()  
  
import whole shipping module from package ecommerce  
from ecommerce import shipping  
shipping.calc_shipping()

# builtin modules in python
link for builtin modules in python3 
https://docs.python.org/3/py-modindex.html

we can use builtin modules using just import statement no need to have package in
locally containing builtin module because python knows that it is. a builtin module
```run-python
import random

for i in range(3):
	print(random.random())
for i in range(3):
	print(random.randint(10,20))
names = ["sukanya", "jyoti", "suma" ]
for i in range(3):
	print(random.choice(names))
```



random.random() function gives random number between zero and one
if we want random number in particular range we need to use random.randdint()
random.choice() gives the random value from iterable given to it

in pycharm they are located in 

external libraries
	python version
		python version




```run-python
class dice:  
 def roll(self):  
  self.x = random.randint(1,6)
  self.y = random.randint(1,6)
  return self.x , self.y  
a = dice()  
print(a.roll())  
print(a.roll())
```



if you are using x and y as variable name in method of a class do not use elf.x to assign value to the same if you do return the self.x and self.y and if you use x and y to assign value then return the same or print the same using print(x) or print(y) rather than print(self.x)
in python if we do just return two comma seperated variable it will be returned as tuple
ex return x , y



## files and directories

 link for python library to work with directories
 https://docs.python.org/3/library/pathlib.html#module-pathlib

## pathlib


```run-python
from pathlib import Path
```
pathlib is a package and Path is a module 
### exists
```run-python
from pathlib import Path
path = Path("ecommerce")  
print(path.exists())

```

exists function will tell if a path is available or not
### mkdir
```run-python
from pathlib import Path
path = Path("emails")  
print(path.mkdir())
```

path.mkdir() creates a new directory
above code will create email directory


### rmdir 
```run-python
from pathlib import Path
path = Path("emails")  
print(path.rmdir())

```

path.rmdir() removes a directory named with which path is instantiated with Path variable
above code will remove emails directory

### glob
it is used to search all the subdirectories and files within directory
for creating an object of Path class referring to current directcory do not give anything in parameter for Path class while creating path object
```run-python
import pathlib import path
path = Path()
for file in path.glob('*.py):
	print(file)
```

will create a path objet referring to current directory you are in
path.glob(*.py) : gives generator object that can be traversed 
it takes regex expression that gives instruction on what type of files to be selected and gives an iterator that contain files that match regex



above code gives all python files

```run-python
from pathlib import Path

```

run-python

you can serach for any library in this url
https://pypi.org/

Just type related keyword and it will show packages related to same

site packages 
all the pacckages that are installed using pip are stored in
external libraries
	python version name
		python version name
			site-pakages

excel spreadsheets

When you find out that you’re a little shaky on this point or that, you can review the material, then re-do the exercise. That’s all it takes to master this book
25 minutes a day
	 5 to 10 minutes reading
	 15 minutes coding
	 
do it on physical keyboard
