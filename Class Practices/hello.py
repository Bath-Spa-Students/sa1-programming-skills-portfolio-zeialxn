print("Name: Zhealene Lucero")
print("Father's name: Alvin Lucero")
print("Mother's name: Jenna Lucero")
print("Current address: Sharjah, United Arab Emirates")
print("Age: 18")
print("Birthday: December 8")
print("Favorite color: Pink")
print("Hobby: Dancing")
print("Favorite fruit: Mango")
print("Favorite food: Chicken Alfredo")
print("Favorite dessert: Ice cream")
#Welcome Msg
print(""" The wheels on the bus go round and round
      Round and round
      Round and round
      The wheels on the bus go round and round
      All day long. """)
""" This is a comment
        This is another comment """
print(""" One last time,
      I need to be the one who takes you home.
      One more time,
      I promise after that,
      I'll let you go. """)
print(""" Row, row, row your boat,
      Gently down the stream
      Merrily, merrily, merrily, merrily,
      Life is but a dream.""")
#Variables
a = "Happy"
b = "19th"
c = "Birthday,"
d = "My"
e = "Dearest"
f = "Axl!"
g = "Wish"
h = "You"
i = "The"
j = "Best!"
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)
print(g)
print(h)
print(i)
print(j)
print(a,b,c,d,e,f)

name = "zhealene"
name = "lucero"
print(name)

z = "bathspa"
print(type(z))

x = 5
y = "Axl"
print(x)
print(y)

x = 4
x = "Axl"
print(x)

x = str(10)
y = int(10)
z = float(10)

x = 5
y = "Axl"
print(type(x))
print(type(y))

x = "Axl"
x = 'Axl'
print(x)

ah = 4
AH = "Soriano"
print(ah)
print(AH)

myvar = "Axl"
my_var = "Axl"
_my_var = "Axl"
myVar = "Axl"
MYVAR = "Axl"
myvar2 = "Axl"

#Camel case
myVariableName = "Axl"

#Pascal case
MyVariableName = "Axl"

#Snake case
my_variable_name = "Axl"

x, y, z = "Axl", "Malibiran", "Soriano"
print(x)
print(y)
print(z)

x = y = z = "Vonnie"
print(x)
print(y)
print(z)

name = ["Axl", "Malibiran", "Soriano"]
x, y, z = name
print(x)
print(y)
print(z)

x = "Python is awesome"
print(x)

x = "Python"
y = "is"
z = "awesome"
print(x, y, z)

x = "Python"
y = "is"
z = "awesome"
print(x + y + z)

#ito may space after
x = "Python "
y = "is "
z = "awesome"
print(x + y + z)

x = 5
y = 10
print(x + y)

x = 5
y = "Axl"
print(x, y)

#Global variables
x = "awesome"

def myfunc():
    print("Python is " + x)

myfunc()

#Example 2
x = "awesome"

def myfunc():
    x = "fantastic"
    print("Python is " + x)

myfunc()

print("Pyhton is " + x)

#example 3
def myfunc():
    global x
    x = "fantastic"

myfunc()

print("Python is " + x)

#example 4
x = "awesome"

def myfunc():
    global x
    x = "fantastic"

myfunc()

print("Python is " + x)

#String concatenation through variable
message = 'Axl ' + 'Soriano'
print(message)

message = 'Happy ' + 'birthday!'
print(message)

#String concatenation through print statement
print('Hello ' + 'world')

#String concatenation through Diff variables
a = "Axl"
b = "Soriano"
c = a + " " + b
print(c) 

# To get Input from User  --------------- Input take by default string from user
name = input ("Enter First_name : ")
print(name)
name = input ("Enter Last_name : ")
print(name)

# We have to mention (Type cast) to get an integer value
age = input("Enter age : ")
print(age)

# Type Cast with integer
age = int(input("Enter Age : "))
print(age)

# Performing Calculations
print(4 + 5)
print(10-6)
print(20*3)
print(40/2)       # For floating Point
print(60//2)      # For integer

# practice
print(4+1)
print(15-5)
print(5*3)
print(200/10)
print(2000//10)

# Operator Precedence BODMAS (Bracker, order, division, multiplication, addition, subtraction)
print((2*3)/8 +(23+5))

# To write formula in multiple line we need back slash \
result = 6 * 2 + 4 * 3 + \
         3 * 4 + 2 + 5

# end delmiiter to remove new line, by default prin will stitch to another statement
         #before
name = "Axl Soriano"
print(name)
print("New print line message ")
         #after
name = "Axl Soriano"
print(name , end =" ")
print("New print line message ")

# \n and \t these are also known as escape sequence
print ("\n this line will print on next line")
print ("\t this is tabbed in ")

# formatted output
name = "Axl"
print(f" My name is {name}")

# if-else
y = 33
z = 200

if y > z:
    print("z is greater than y")