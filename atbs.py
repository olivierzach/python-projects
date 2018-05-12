# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# comment out code with funtion 1
# run line with F9

# python can do math
2+2

# a single value with no operators is an expression
2 


# python has all the standard operators
2+3 *6
#Out[15]: 20

(2+3)*6
#Out[16]: 30

2**8
#Out[17]: 256

23/7
#Out[18]: 3.2857142857142856

23//7
#Out[19]: 3

23%7
#Out[20]: 2

# spacing doesn't matter
2     +      2
#Out[21]: 4

# order of operations
(5 -1) * ((7 + 1) / (3 - 1))
#Out[22]: 16.0


# expressions are just values combined with operators
# they will always evaluate down to a single value
# we have standard data types in python
# integers, floating point numbers, and strings

# strings
'Hello world!'

# string replication
'alice' + 'bob'


# can't combine certain classes
'alice' + 42
#TypeError: must be str, not int

# string replication
'alice' * 5
#Out[24]: 'alicealicealicealicealice'

# you can only replicate with integers and a string
'alice' * 'bob'
#TypeError: can't multiply sequence by non-int of type 'str'

'alice' * 5.0
#TypeError: can't multiply sequence by non-int of type 'float'


# storing values in variables
spam = 40
spam
#Out[28]: 40

eggs = 2

spam + eggs
#Out[30]: 42

spam + eggs + spam
#Out[31]: 82

spam = spam + 2
spam
#Out[33]: 42

spam = 'hello'
spam
#Out[35]: 'hello'

spam = 'goodbye'
spam
#Out[37]: 'goodbye'

# variable names can only be one word
# it can use only letters numbers and the underscore
# it cannot begin with a number


## our first program

# this program says hello and asks for my name
print('hello world')
print('what is your name?')

myName = input()

print('it is good to meet you, ' + myName)

print('the length of your name is:')
print(len(myName))

print('what is your age')
myAge = input()

print('you will be ' + str(int(myAge) + 1) + ' in one year')

#hello world
#what is your name?
#
#zach
#it is good to meet you, zach
#the length of your name is:
#4
#what is your age
#
#26
#you will be 27 in one year


## str(), int() and float() functions
# we may need to convert data types to perform operations

str(0)
#Out[45]: '0'

str(-3.4)
#Out[46]: '-3.4'

int('42')
#Out[47]: 42

int(-99)
#Out[48]: -99

int(1.25)
#Out[49]: 1

int(1.99)
#Out[50]: 1

float(10)
#Out[51]: 10.0

# input function gives the typed value as a string
spam = input()
spam
#Out[53]: '101'

# convert the input to a number
spam = int(input())
spam * 10 + 5
#Out[55]: 1015

# we cannot put strings into int
# we can use int on floating points

# round down
int(9.9)
#Out[56]: 9

# round up
int(9.9) + 1
#Out[57]: 10

# combining inputs in strings
print('what is your age?')
myAge = input()

print('you will be ' + str(int(myAge) + 1) + ' in a year')

#what is your age?
#
#25
#you will be 26 in a year



# text and number equivalance
# using the logical True and False equivalence
42 == '42'
#Out[59]: False

42 == 42.0
#Out[60]: True

42.0 == 0042.000
#Out[61]: True



## Flow Control
# we can execute code based on logical statements

# boolean values: true / false, 1 or 0
spam = True
spam
#Out[63]: True

# the correct way to initialize the boolean True is True
# the correct way to initialize the boolean False is False


# Comparison Operators
# using our comparisons operators we can reduce down to a boolean true or false

42 == 42
#Out[64]: True

42 == 99
#Out[65]: False

# not equal to comparison operator
2 != 3
#Out[67]: True

2 != 2
#Out[68]: False

# we can also work with strings

'hello' == 'hello'
#Out[69]: True

'hello' == 'Hello.'
#Out[70]: False

'dog' != 'cat'
#Out[71]: True

# we can also comparison combinations of data types

True == True
#Out[72]: True

True != False
#Out[73]: True

42 == 42.0
#Out[74]: True

42 == '42'
#Out[75]: False

# other comparison operators
# less than, greater than, or equal to

42 < 100
#Out[76]: True

42 > 100
#Out[77]: False

eggCount = 42
eggCount <= 42
#Out[79]: True

myAge = 29
myAge >= 10
#Out[82]: True

# the == operator wants to compare to expressions together
# the = operator is assigning the value to the left to the name on the right
# == has two character and compares two values together if they are TRUE or FALSE


# Boolean Operators with Set Operations
# AND, OR, XOR, NOT

True and True
#Out[83]: True

True and False
#Out[84]: False

False or True
#Out[85]: True

False or False
#Out[86]: False

# the not operator evaluates to the oppositve boolean

not True
#Out[87]: False

not not not not True
#Out[88]: True


# we can mix boolean and comparison operators

(4 < 5) and (5 < 6)
#Out[89]: True

(4 < 5) and (9 < 6)
#Out[90]: False

(1 == 2) or (2 == 2)
#Out[91]: True

2 + 2 == 4 and not 2 + 2 == 5 and 2 * 2 == 2 + 2
#Out[92]: True


# elements of flow control
# conditional statements

name = input()
password = input()

if name == 'mary':
    print('hello mary')
    if password == 'swordfish':
        print('access granted')
    else:
        print('wrong password')

#mary
#swordfish
#hello mary
#access granted


# conditional statements: the if statement

if name == 'alice':
    print('hi alice')
    
# conditional statements: the else statements

if name == 'alice':
    print('hi alice')
else:
    print("i don't know you")

 
# conditional statements: the if else statements
# use the elif keyword

name = 'alice'
age = 25
    
if name == 'alice':
    print('hi alice')
elif age < 12:
    print('you are not alice dude')


# long combined if else statements
if name == 'Alice':
    print('hi alice')
elif age < 12:
    print('you are not alice')
elif age > 2000:
    print('fuck off')
elif age == 25:
    print('what up dude')
#what up dude


# while loop statements
# uses the while keyword
# aiming to continue looping until a condition is met
# similiar to an if statement 

# if statement
spam = 0
if spam < 5:
    print('hello')
    spam = spam + 1
spam
#hello
#Out[118]: 1

# while statement
spam = 0
while spam < 5:
    print('hello')
    spam = spam + 1
spam
#hello
#hello
#hello
#hello
#hello
#Out[119]: 5

# the while loop will continue to iterate until the condition fails
# while spam is less than 5 print 'hello'
# this will continue to print until our spam variable increases past 5



## break statements
# there is a shortcut to stopping execution of a loop

while True:
    print('Please type your name')
    name = input()
    if name == 'your name':
        break
print('thank you!')


## continue statements
# continue statements are used inside loops
# when the program reaches a continue statement the program immediately 
# jumps back to the start of the loop and re-evaluates the loop condition

while True:
    print('who are you?')
    name = input()
    if name != 'Joe':
        continue
    print('Hello Joe - what is the password?')
    password = input()
    if password == 'swordfish':
        break
print('access granted')

## for loops and the range() function
# the while loop keeps looping until its condition is True
# what if we want to execute a block of code only a ceratin number of times?
# we can do this with a for loop statement and the range function

# a for statement looks like: for i in range(5) and will contain:
# the for keyword
# a variable name
# the in keyword
# a call to the range() method with up to three integers passed to it
# a colon :
# an indented block of code 

# example:
print('my name is')
for i in range(5):
    print('jimmy five times (' + str(i) + ')')

# we can use break and continue statements inside for loops as well
# we can only use continue and break statements inside while or for loops

# for loop example: Gauss example
total = 0
for num in range(101):
    total = total + num
print(total)

# an equivalent while loop
print('my name is')
i = 0
while i < 5:
    print('Jimmy five times (' + str(i) + ')')
    i = i + 1

# the starting, stopping and stepping arguements to range()
# some functions can be called with multiple agruements separated by a comma
# and range is one of them
# this lets you change the integer passed to range to follow any sequence

# example: print the range from 12 - 16 exclusive
for i in range(12, 16):
    print(i)

# the range function can also take 3 arguements
# the third is the step arguement
# this is the amount the variable will increase by after every iteration
# this will print 0 - 10 exclusive by 2
for i in range(0, 10, 2):
    print(i)

# we can use a negative number to count backwards
# code counts backwards from 5 by -1
for i in range(5, -1, -1):
    print(i)





## Importing Modules
# all python programs can call a basic set of functions that are "built-in"
# like print(), len(), input()
# python also comes with a set of modules called the standard library
# each module contains a group of related functions you can call

# to access modules in python we will need to import them
# we will need:
# the import keyword
# the name of the module

# random module
# randint function will calculate a random interger between the range we feed
# this code produces a randomint between 1-10 five times (the loop)
import random
for i in range(5):
    print(random.randint(1,10))

# we can import many different modules at the same time
# import random, sys, os, math all at the same time
# import random, sys, os, math


# ending a program early with sys.exit()
import sys
 
while True:
    print('type exit to exit')
    response = input()
    if response == 'exit':
        sys.exit()
    print('you typed ' + response + '!!!')


# summary
# by using expressions that evaluate to True or False (conditions)
# we can write programs that make decisions on what code to execute and what to skip
# we also learned out iterating code with loops
# we also learned flow control statements like break and continue
# we also learned how to import modules into python

spam = input()
    
if spam == 1:
    print('hello')
elif spam == 2:
    print('howdy')
else:
    print('greetings')

    
    
for i in range(11):
    print(i)
   

i = 1

while i  < 11:
    print(i)
    i = i + 1



### Chapter 3: Functions
# a function is a mini program within a program
# let's learn how to build them in python

def hello():
    print('howdy!')
    print('HOWDY!')
    print('hello there')
    
hello()
hello()

# we first take in a def statment - this defines a function names hello
# then we give our function a body - the code that the function will execute
# then we call the function to run the code we put in the body

# a major purpose of functions is to group code that gets executed multiple times
# without the function we would have to do a lot of copy / pasting
# never copy and paste more than three times!!

## def statements with parameters
# we can pass in arguements to our functions!
def hello(name):
    print('hello ' + name)
    
hello('zach')
hello('tiffy')

# a parameter is a variable that an agruement is stored in when the function is called


## Return values and return statements
# in general the value that a function call evaluates to is called the return value of a function
# we can use the return statement to to specify what the return value should be in your functions
# need a return() keyword, the value or expression that the function should return

# return values examples
import random

def getAnswer(answerNumber):
    if answerNumber == 1:
        return 'it is certain'
    elif answerNumber == 2:
        return 'it is so'
    elif answerNumber == 3:
        return 'yes'
    elif answerNumber == 4:
        return 'no'
    
r = random.randint(1,4)    
fortune = getAnswer(r)
print(fortune)

# we can shorten these lines by wrapping the call together
# expressions are composed of values and operators
# a function call can be used in an expression because it evalutes to its return value
print(getAnswer(random.randint(1,4)))


## The None Value
# in python there is the NONE value - it represents the absence of a value
# we type this with a capital N, None
spam = print('hello!')
None == spam

## Keyword Arguements and print()
# most arguements are identified by thier position in the function call
# however keyword arguements are identified by the keyword put before them in the function call
# here are some examples
print('hello')
print('world')

# specifying the end of the line
print('hello', end = '')
print('world')

# end skips the new line call the next print statement

# pass multiple strings to print()
print('cats', 'dogs', 'mice')

# comma seperator
print('cats', 'dogs', 'mice', sep = ',')

# functions have optional keyword arguements that can be specified when the function is called


## Local and Global Scope
# parameters and variables that are assigned in a called function are said to exist in the local scope
# variables that are assigned outside all functions are said to exist in global scope
# a variable that exists in a local scope is called a local variable
# varibles that exist in a global scope is called a global variable

# think of scope as a container for variables
# when a scope is destroyed the values stored in the scope are forgotten

# scopes matter
# code in the global scope cannot use any local variables
# a local scope can access global variables
# code in a function's local scope cannot use vairables in any other local scope
# you can use the same name for different variables if they are in different scopes
# it is a bad habit to rely on global variables as your programs get larger and larger

# local variables cannot be used in the global scope
def spam():
    eggs = 31337

spam()
print(eggs)

#Traceback (most recent call last):
#
#  File "<ipython-input-30-15da8c3dc934>", line 1, in <module>
#    print(eggs)
#
#NameError: name 'eggs' is not defined

# this error happens because the eggs variable exists only in the local scope created when spam() was called
# once the function is called that space is destroyed and we cannot access those local variables anymore

# local scopes cannot use variables in other local scopes
def spam():
    eggs = 99
    bacon()
    print(eggs)

def bacon():
    ham = 101
    eggs = 0

spam()

# global variables can be read from a local scope
# python uses eggs as a reference to 42 when spam() is called
def spam():
    print(eggs)

eggs = 42
spam()
print(eggs)


# local and global variables with the same name
def spam():
    eggs = 'spam local'
    print(eggs) 
    
def bacon():
    eggs = 'bacon local'
    print(eggs)
    spam()
    print(eggs) # prints bacon local
    
eggs = 'global'
bacon()
print(eggs)


# the global statement
# if we need to modify a global variable from within a function use the global statement
def spam():
    global eggs
    eggs = 'spam'
    
eggs = 'global'
spam()
print(eggs)

# get a better feel for these global statement rules
def spam():
    global eggs
    eggs = 'spam' # this is the global

def bacon():
    eggs = 'bacon' #this is a local
    
def ham():
    print(eggs) # this is the global
    
eggs = 42 # this is the global
spam()
print(eggs)

# in a function a variable will either always be global or always be local
# if we want to modify the value stored in a global variable from within a function...
# you must use a global statement on that variable!

# global variable without the global statement
def spam():
    print(eggs) #ERROR
    eggs = 'spam local'
    
eggs = 'global'
spam()

#Traceback (most recent call last):
#
#  File "<ipython-input-39-d97d23a8ba54>", line 7, in <module>
#    spam()
#
#  File "<ipython-input-39-d97d23a8ba54>", line 2, in spam
#    print(eggs) #ERROR
#
#UnboundLocalError: local variable 'eggs' referenced before assignment


# functions as 'black boxes'
# often all we will need to know about a function are its inputs and output value
# this high-level way of thinking is treating a function as a 'black box'


## Exception Handling
# getting an error is getting an exception
# the program you wrote crashed
# in real life you want the program to detect errors, handle them, and then continue

# divide by zero error
def spam(divideBy):
    return 42 / divideBy

print(spam(2))
print(spam(12))
print(spam(0))

'''
Traceback (most recent call last):

  File "<ipython-input-43-737e559b2995>", line 1, in <module>
    print(spam(0))

  File "<ipython-input-40-0f28aced8aa3>", line 2, in spam
    return 42 / divideBy

ZeroDivisionError: division by zero'''

# errors can be handled with try and except statements
# the code that could potentially have an error is put in the try clause
# the program execution moves to the start of the following except clause if an error happens

# we can put our divdeBy function is a try / except combo
def spam(divideBy):
    try:
        return 42 / divideBy
    except ZeroDivisionError:
        print('error: invalid arguement')

print(spam(2))
print(spam(12))
print(spam(0))


# example of a try block
def spam(divideBy):
    return 42 / divideBy

try:
    print(spam(2))
    print(spam(12))
    print(spam(0))
except ZeroDivisionError:
    print('error: invalid arguement')


## A Short Program: Guess the Number
# put all the basics together into one example
# guess the number examples
    
# this is the guess the number game
import random

secretNumber = random.randint(1,20)
print('i am thinking of a number between 1 and 20')

# ask the player to guess 6 times
for guessesTaken in range(1,7):
    print('take a guess')
    guess = int(input())

    if guess < secretNumber:
        print('too low - guess again!')
    elif guess > secretNumber:
        print('too high - guess again!')
    else:
        break # this condition is the correct guess
        
if guess == secretNumber:
    print('great job! i love you! you guessed the number in ' + str(guessesTaken) + ' guesses!')
else:
    print('nope - the number I was thinking of was ' + str(secretNumber) + '- still love you')


## Summary
# functions are the primary way to compartmentalize your code into logical groups
# variables executed are stored locally within the function and cannot break the global variables
# functions are a great tool to organize your code
# they have inputs that form parameters and outputs in the form of return values
# the code inside functions does not effect variables in other functions
# we can use try and except statements which can run code when the error has been detected
    
## Practice Exercises
# build your own function with the collatz sequence
# the simplest impossible math problem!
    
# define function
def collatz(number):
    
    if number % 2 == 0: # if number is even
        result = number // 2 # do this equation
        print(result) # print the result 
        return result  # return the result out of the function
    
    elif number % 2 == 1: # if number is odd
        result = 3 * number + 1 # do this equation
        print(result) # print the result to console
        return result  # return the result out of the function
        
collatz(5)
collatz(2)


# user input function
number  = input('give me a number: ') # ask for a number from user

while number != 1: # while our inputted number is NOT 1
    number = collatz(int(number)) # set number to the collatz of the the first inputted number
    

'''
Chapter 4: Lists

This chapter will cover lists in python
understanding lists and tuples are essential to programming
lists and tuples contain multiple values and make it easier to manipulate them
lists can contains list!
we can use them to organize heirarchical structures
in this chapter we will learn lists and methods
'''

# a list is a value that contains multiple values in an ordered sequence
# list value is the value in the list
# we can think of list values as: list = [cat, dog, bird]
# cat dog and bird are the list values of the list named list
# lists always begins with the square brackets []

# the values within the list are called items and are separeted by commas

# list examples
# lists can contain many differnt types of data!
[1,2,3]
['cat', 'bat', 'rat']
['hello', 3.145, True, None, 42]

# defining lists
# spam is still assign to one variable the list
# but the list actually contains multiple list values!
spam = ['cat', 'bat', 'rat']
spam

# Indexing or getting values from within a list
# we simply select the position of the list value we want from within the list
spam = ['cat', 'bat', 'rat']
spam[1]
spam[0]
spam[0:1]
spam[0:3]

'hello ' + spam[0]

'the ' + spam[1] + ' ate the ' + spam[0]

# python will give you an IndexError message if you use an index that exceeds the number of values in your list value
spam
spam[1000] # gives an error

# indexes can only be integer values not floats
spam[1.0] # also gives an error

## lists can also contain other list values!
# we can access these using multiple indexes
spam = [['cat', 'bat'], [10,20,30,40,50]]
spam[0] # cat and bat
spam[1] # list of numbers in list value 2

# we can select list values from within list values!
spam[0][1]  # bat  
spam[0][0]  # cat
spam[1][3]  # 30
spam[1][4]  # 50

# this first index dicates which list value to use...
# the second indicates the value within the list value

# negative indexes
# we can use negative indexes to get 'n from last' items of lists
spam = ['cat', 'bat', 'rat', 'elephant']
spam[-1] # last value
spam [-3] # third to last value in our list

'the ' + spam[-1] + ' is afraid of the ' + spam[-3]


# getting sublists with slices
# a slice can give you several values from a list and output a new list
# spam[2] is a list with an index
# spam[1:4] is a list with a slice (two integers)
# a slice goes up to but will not include the value of the second index!!
spam = ['cat', 'bat', 'rat', 'elephant']
spam[0:4]
spam[1:3]
spam[0:-1]

# as a shortcut we can leave out one or both of the indexes
# leaving out the first will be the same as using 0
# leaving out the second is using the length of the list
spam = ['cat', 'bat', 'rat', 'elephant']
spam[:2]
spam[1:]
spam[:]

# the len function will return the number of values in your list
spam = ['cat', 'dog', 'mouse']
len(spam)


# changing values in a list with indexes
# we can change the actual list values by assigining variables to the list
spam = ['cat', 'bat', 'rat', 'elephant']
spam[1] = 'aardvark'
spam
spam[2] = spam[1]
spam
spam[-1] = 12345
spam

# list concatenation and replication
# the plus operator can combine two lists together
# the * operator can be used to replicate lists
[1,2,3] + ['a','b','c']
['x', 'y', 'z'] * 3
spam = [1,2,3]
spam = spam + ['a','b','c']
spam

# remove list values with the del statement
spam = ['cat', 'bat', 'rat', 'elephant']
del spam[2]
spam
del spam[2]
spam


## Working with Lists
# instead of using multiple reptitive variables in our code...
# we can use a single variable that contains a list variable
# here is an example
catNames = []
while True:
    print('Enter name of cat ' + str(len(catNames) + 1) + ' (Or enter nothing to stop.):')
    name = input()
    if name == '':
        break
    catNames = catNames + [name]
    print('the cat names are')
    for name in catNames:
        print(' ' + name)

# using for loops with lists
# we can use for loops to loop through values within a list

# previous for loop example
for i in range(4):
    print(i)
        
# for loop with a list
for i in [0,1,2,3]:
    print(i)


# a common technique is to use range(len(someList)) with a for loop to iterate over the indexes of a list
supplies = ['pens', 'staples', 'flame throwers', 'binders']

# for loop over elements of a list
for i in  range(len(supplies)):
    print('Index ' + str(i) + ' in supplies is: ' + supplies[i])

# in this code we can access the index and the value of that index!
    
# the in and not in Operators
# determine whether a value is in or not in a list
# the result will reduce to a logical value
'howdy' in ['hello', 'hi', 'howdy', 'hey']
spam = ['hello', 'hi', 'howdy', 'hey']
'cat' in spam
'howdy' not in spam
'cat' not in spam


# putting the in and not in into a program
myPets = ['zophie', 'pooka', 'fat-tail']
print('enter a pet name:')
name = input()

if name not in myPets:
    print('i do not have a pet named ' + name)
else:
    print(name + ' is my pet')


# the multiple assignment trick
# this lets you assign multiple variables with the values in a list in one line

# instead of doing this:
cat = ['fat', 'black', 'loud']
size = cat[0]
color = cat[1]
disposition = cat[2]

# we can type this in one line of code
# we need to make sure the number of variables we are assigning and the names are the same elements
cat = ['fat', 'black', 'loud']
size, color, disposition = cat
size
color
disposition


## Augmented Assignment Operators
# this slight change in an operator allows you to combine statements together
# for example assigning a variable to 42 and then adding 1 to it

# we would do:
spam = 42
spam = spam + 1
spam

# with the augmented operators we could do:
spam = 42
spam += 1
spam

# we can do this renaming and some manipulation trick with multiple operators
# -=
# *=
# /=
# %=

# we can also do string concatenation
spam = 'hello'
spam += ' world!'
spam

bacon = ['zophie']
bacon *= 3
bacon


## Methods
# a method is the same thing as a function except it is 'called on' a variable!
# each data type has it's own set of methods

# finding a value in a list with the index() method
# list values have the index() method that can be passed to a value...
# and we get back the index of that value!!
spam = ['hello', 'hi', 'howdy', 'hey']
spam.index('hello') # gives us the index where 'hello' is in the list

spam.index('hey')
spam.index('howdy howdy howdy')

# when there are duplicates of the value in the list the index of its FIRST APPEARANCE IS RETURNED
spam = ['zophie', 'pooka', 'fat-tail', 'pooka']
spam.index('pooka')

# adding values to lists with the append() and insert() Methods
# to add new values to a list...
# we can use the append and insert methods
spam = ['cat', 'dog', 'bat']
spam.append('moose') # add moose to the end of our list
spam

# insert can put a value anywhere in our list
spam = ['cat', 'dog', 'bat']
spam.insert(1, 'chicken') # put chicken into the second element of the list
spam

# these methods modify the list in place
# methods belong to a single data type
# certain methods can only be called on certain data types
# error example:
eggs = 'hello'
eggs.append('world') # can't use append on a string needs a list!

bacon = 42
bacon.insert(1, 'world') # can't use insert on a int needs a list!


# removing values of a list with remove
spam = ['cat', 'bat', 'rat', 'elephant']
spam.remove('bat')
spam

# attempting to remove an element that is not there will throw an error
spam = ['cat', 'bat', 'rat', 'elephant']
spam.remove('chicken')

# if value appears multiple times only the first instance will be removed
spam = ['cat', 'bat', 'rat', 'cat']
spam.remove('cat')
spam

# the del statement is good when you know the index of the value that will be removed
# the remove method is good when you know the value you want to remove from the list

# sorting values in a list with the sort() Method
spam = [2,5,3.14, 1, -7]
spam.sort()
spam

spam = ['ants', 'badgers', 'cats', 'dogs', 'buffalo', 'elephants']
spam.sort()
spam

# we can also reverse the sorting with reverse = True
spam.sort(reverse = True)
spam

# we cannot sort lists with a combination of string and integers
# sort uses ASCIIbetical order - uppercase letters come before lowercase letters
# lowercase a comes AFTER uppercase Z!

# if we need to sort values in regular alphabetical order pass str.lower
# this will convert all values to lowercase
spam = ['a', 'z', 'A', 'Z']
spam.sort(key = str.lower) # treats all values as lowercase then sorts
spam # outputs the values as the originally appeared before the sort!!


## Example Program: Magic 8 Ball with a List
# using lists we can write a program to mimic an magic 8 ball program
# instead of several lines of identical ifelse statements...
# we can create a single line that the code works with

import random

messages = ['it is certain',
            'it is decidedly so',
            'yes definately',
            'reply hazy - try again later',
            'ask again later bitch',
            'concentrate and ask again',
            'my reply is no',
            'outlook doubtful',
            'very fucking doubtful']

print(messages[random.randint(0, len(messages) - 1)])



# List - like Types: Strings and Tuples
# lists aren't the only data types that represent ordered sequences of values
# a string is a list of ordered character variables
# many of the things we do with lists can be done with strings!
name = 'zophie'
name[0]
name[-2]
name[0:4]
'zo' in name
'Z' in name
'p' not in name

for i in name:
    print('*** ' + i + ' ***')
    
    
## Mutable and Imputatble Data Types
# lists and strings are different in an important way
# a list value is mutable data type: we can change values inside of it!
# a string value is immutable: it cannot be changed!!
name = 'zophie is a cat'    
name[7] = 'the' # error cannot change a string!

# the proper way to mutate a string is to use slicing and concatentation
# this will build a new string!
name = 'zophie a cat'
newName = name[0:7] + 'the' + name[8:12]
newName


# difference between mutating a list and overwritiing it completely
# this code does not change the list - rather is writes over it with completely new values
eggs = [1,2,3]
eggs = [4,5,6]
eggs

# this is how to actually mutate the code to match the above code
eggs = [1,2,3]
del eggs[2]
del eggs[1]
del eggs[0]
eggs # eggs is now empty

# add in values to the now empty eggs list
eggs.append(4)
eggs.append(5)
eggs.append(6)
eggs # eggs now has all the values in it


## The TUPLE data type
# the tuple data type is almost identical to the list type EXCEPT IT IS IMMUTABLE
# tuples are typed with paranthesis
eggs = ('Hello', 42, .5)
eggs[0]
eggs[1:3]
len(eggs)

# we cannot change a tuple!
eggs = ('Hello', 42, .5)
eggs[1] = 99

# indicating tuple with just one value needs a trailing comma
type(('hello',)) # tuple
type(('hello')) # string

# tuples can convey to anyone reading your code that you don't intend these values to change
# if we need an ordered sequence of values that never change use a tuple
# python can implement some optimizations that make code using tuples slightly faster

# converting types with the list() and tuple() functions
# we can convert to and from lists or tuples
tuple(['dog', 'cat', 5])
list(('dog', 'cat', 5))
list('hello')

# we can use these functions to change values in a tuple
# convert tuple to list - edit values - covert back to tuple

## References
# variables store strings and integer values
spam = 42
cheese = spam
spam = 100
spam
cheese

# cheese will not change if you update spam - it has already been assigned to the value 42
# LISTS DO NOT WORK THIS WAY!
# when you assign a list to a variable you are actually assigning a list reference to the variable!
# a reference value is a value that points to some bit of data
spam = [0,1,2,4,5]
cheese = spam
cheese[1] = 'hello' # changing the cheese list also changes the spam list!!
spam
cheese


## Passing References
# references are particularly important for understanding how arguements get passed to functions
# when a function is called the values of the arguements are copied to the parameter variables
# there are some consequences to this fact

def eggs(someParameter):
    someParameter.append('hello')

spam = [1,2,3]
eggs(spam)
print(spam)

# notice that a return value is not used to assign a new value to spam
# instead it modifies the list in place directly
# even though spam and someParameter contain separate references they refer to the same list!
# this is why the append('hello') method call inside the function affects the list even after the function has returned


## the copy Module's copy() and deepcopy() functions
# passing around references is often the handiest way to deal with lists and dictionaries
# if the function modifies the list or dictionary that is passed you may not want these changes made to the original list / dictionary
# for this python has a module called copy
# copy creates a copy of a list that can be modified independently of the original!!!
import copy
spam = ['A', 'B', 'C', 'D']
cheese = copy.copy(spam)
cheese[1] = 42
spam # spam is not modified!
cheese # cheese is modified!

# use the copy.deepcopy() if you want to copy the list and the lists inside the original list!!

## Summary
# lists are useful since they allow you to write code that works on a modifiable number of varibles
# lists are mutable - the meaning of thier contents can change
# variables do not store list values directly they store references to lists!
# any changes made to the list might impact another variable later down in the program
# use cop() and deepcopy() to change values in a list without modifying the original list


## Practice Exercises
# say you have a list value like this:
names = ['apples', 'bananas', 'tofu', 'cats']

# write a function that takes a list value as an arguement and returns a string with all the items separated by commas and space
# with and inserted before the last item
# passing our spam list to this function would give: apples, bananas, tofu and cats

def commaCode(items):
    for i in range(len(items) -2):
        print(items[i], end = ', ')
    print(items[-2] + ' and ' + items[-1])


commaCode(names)



'''
Chapter 5: Dictionaries and Structuring Data
Dictionaries provide a flexible way to structure and organize data
'''
# like a list a dictionary is a collection of many values
# but unlike indexes for lists, indexes of dictionaries can use many different data types
# indexes for dictionaries are called keys and a key with its associatated value is the key-value pair
# we use the {} to define a dictionary in python

# first dictionary
myCat = {'size': 'fat', 'color':'gray', 'disposition':'loud' }
myCat

# this assigns a dictionary to the myCat variable
# the dictionary keys are cat, color, and disposition
# the key value pairs are fat, gray and loud
# we can access the values using thier keys!!
myCat['size']
'My cat has ' + myCat['color'] + ' fur'

# dictionaries can still use integer values as keys
spam = {12345: 'Luggage Combo', 42: 'The Answer'}

## Dictionaries vs. Lists
# unlike lists dictionaries are unordered
# the first item in a list named spam would be spam[0]
# there is no first item in a dictionary
# while the order of items matters for determining whether two lists are the same
# it does not matter in what order the key-value pairs are typed in a dictionary

# list equivalence
spam = ['cats', 'dogs', 'moose']
bacon = ['dogs', 'moose', 'cats']
spam == bacon

# dictionary equivalence
eggs = {'name': 'Zophie', 'species':'cat', 'age':'8'}
ham2 = {'species':'cat', 'age':'8', 'name':'Zophie'}
eggs == ham2

# dictionaries cannot be sliced like lists they are unordered!
# trying to access a key that does not exist will throw an error
# though dictionaries are not ordered - we can organize data in powerful ways

# birthdays example:
birthdays = {'Alice':'Apr1', 'Bob':'Dec 12', 'Carol':'Mar 4'}

while True:
    print('enter a name: (blank to quit)')
    name = input()
    if name == '':
        break
    if name in birthdays:
        print(birthdays[name] + ' is the birthday of ' + name)
    else:
        print('I do not have birthday information for ' + name)
        print('what is their birthday?')
        bday = input()
        birthdays[name] = bday
        print('birthday database updated')


## They keys(), values(), and items() methods
# there are three dictionary methods that will return list-like values of the dictionary's keys, value or both
# keys(), value(), items()
# the values returned by these methods are not true lists they cannot be modified and do not have an append method
# but these data types can be used in for loops!

# here the for loop itierates over each of the values in spam dictionary        
spam = {'color':'red', 'age':42}
for v in spam.values():
    print(v)

# we can also iterate over each of the keys and both keys and values
for k in spam.keys():
    print(k)
    
for i in spam.items():
    print(i)

# using these methods a for loop can iterate over the keys, value and pairs in a dictionary
# notice that the value returned by the items() method are tuples of the key and value
    
# if you want a true list from one of these methods we need to conver the output into a list
spam = {'color':'red', 'age':42}
spam.keys()
list(spam.keys())

# we can also use the multiple assignment trick in a for loop to assign the key and value to separate variables
spam = {'color':'red', 'age':42}
for k, v in spam.items():
    print('key: ' + k + ' Value: ' + str(v))


## checking whether a key of value exists
# recall the in and not operators can check if a value exists
# we can also use these to check a dictionary
spam = {'name':'Zophie', 'age':17}
'name' in spam.keys()
'Zophie' in spam.values()
'color' in spam.keys()
'color' in spam
17 in spam.values()


## the get() Method
# it is tedious to check whether a key exists in a dictionary before accessing that key's value
# dictionaries have a get() method that takes two arguements: the key and a fallback value 
picnicItems = {'apples': 5, 'cups':2}
'I am bringing ' + str(picnicItems.get('cups',0)) + ' cups'
'I am bringing ' + str(picnicItems.get('eggs',0)) + ' eggs'

# this uses the fallback value of 0 when we try to find the value of the key eggs
# we have no eggs in our picnicItems dictionary!

## the setdefault() Method
# you will often have to set a value in a dictionary for a certain key only if that key doesn't already have a value
spam = {'name':'pooka','age':15}
if 'color' not in spam:
    spam['color'] = 'black'

# the setdeafult method does this in one line of code
# the first agruement passed to the method is they key to check for 
# and the second arguement is the value to set at that key if they key does not exists
# if the key does not exist the setdeafult() method returns the key's value
spam = {'name': 'pooka', 'age':5}
spam.setdefault('color', 'black')
spam

# in this case we already have a value for color so we will not overwrite!!
spam.setdefault('color', 'white')
spam

# here is a short program that counts the number of occurrences of each letter in a string
message = 'it was a bright cold day in April, and the clocks were striking'
count = {}

for character in  message:
    count.setdefault(character, 0)
    count[character] = count[character] + 1
    
print(count)

# the program loops over each character in the message variable's string
# it counts how often each character appears
# the setdefault() method call ensures that the key in the count dictionary
# so the program does not throw an error when count[character] = count[character] + 1 is executed


## pretty printing
# if you import the pprint module into your programs you will have access to the pprint and pformat functions
# these will 'pretty print' a dictionary's values
import pprint

message = 'it was a bright cold day in April, and the clocks were striking'
count = {}

for character in  message:
    count.setdefault(character, 0)
    count[character] = count[character] + 1
    
pprint.pprint(count)

# this function is especially helpful when the dictionary itself contains nested lists or dictionaries

# if you want to obtain the prettified text as a string value instead of displaying it on the screen
# we can use pprint.pformat() instead
# these two lines are equivalent to each other
pprint.pprint(spam)
print(pprint.pformat(spam))


## Using Data Structures to Model Real-World Things
# chess example
# we can use notation to define the moves of a chess game
# computers will use this notation to play chess without a chessboard
# we can tell the computer how to play certain games
# this is where lists and dictionaries come in

# simple tic tac toe example
# we can use simple strings to model what is going on in a game
# we can use a dictionary to do this

# completely clear tic tac toe board
theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
            'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
            'low-L': ' ', 'low-M': ' ', 'low-R': ' '}

# first move
theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
            'mid-L': ' ', 'mid-M': 'X', 'mid-R': ' ',
            'low-L': ' ', 'low-M': ' ', 'low-R': ' '}

# complete game
theBoard = {'top-L': 'O', 'top-M': 'O', 'top-R': 'O',
            'mid-L': 'X', 'mid-M': 'X', 'mid-R': ' ',
            'low-L': ' ', 'low-M': ' ', 'low-R': ' '}

# of course the player sees only whats printed on the screen not the variables
# let's modify to make this game real
theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
            'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
            'low-L': ' ', 'low-M': ' ', 'low-R': ' '}

def printBoard(board):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-+-+-')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-+-+-')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])
    
printBoard(theBoard)



# lets add code to let players make thier own moves
theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
            'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
            'low-L': ' ', 'low-M': ' ', 'low-R': ' '}

turn = 'X'
 
for i in range(9):
    printBoard(theBoard)
    print('turn for ' + turn + ' . Move to which space?')
    move = input()
    theBoard[move] = turn
    if turn == 'X':
        turn = 'O'
    else:
        turn = 'X'

printBoard(theBoard)


## Nested Dictionaries and Lists
# the board only needs a simple dictionary value with nine key-value pairs
# as we model more complicated things...
# we may find we need dictionaries and lists that contain other dictionaries and lists
# lists are useful to contain an ordered series of values
# dictionaries are useful for associating keys with values

# who is bringing what to the picnic?
allGuests = {'Alice': {'apples': 5, 'pretzels':12},
             'Bob': {'ham sandwiches': 3, 'apples': 2},
             'Carol': {'cups': 3, 'apple pies': 1}}

def TotalBought(guests, item):
    numBought = 0
    for k, v in guests.items():
        numBought = numBought + v.get(item, 0)
    return numBought

TotalBought(allGuests, 'apples')
TotalBought(allGuests, 'apple pies')    
TotalBought(allGuests.Bob, 'apples')

allGuests['Bob']['apples']
allGuests['Bob']['ham sandwiches']
    
# we learned about dictionaries in this chapter
# lists and dictionaries are values that can contain multiple values...
# including other lists and dictionaries
# dictionaries are useful because we can map one item (key) to another (value)
# values inside a dictionary are accessed using square brackets just like lists
# instead of an integer index: dictionaries can have keys of a variety of data types
# we can use dictionaries to represent real world objects

empty = {}
foo = {'foo':42}
foo['foo']
foo.get('foo')
foo.keys()
foo.values()
foo.setdefault('color', 'black')
foo


## fantasy game inventory
inv = {'arrows': 100, 'coin': 5000, 'torch': 2,
       'medicine': 3, 'lute': 1, 'sword': 1}

def fantasyInventory(inv):
    total_inv = 0
    for k in inv.keys():
        total_inv = total_inv + inv[k]
    return(total_inv)
    
inv['sword']
inv['medicine']
5000 in inv.values()

loot = {'coin': 500, 'dagger':2, 'axe':2}

def addInventory(loot, inv):
    for k in loot.keys():
        if k in inv.keys():
            inv[k] = inv[k] + loot[k]
        else:
            inv.setdefault(k, loot[k])
        
addInventory(loot, inv)

import pprint

pprint.pprint(inv)


import numpy as np
old = np.array([[1,1,1], [1,1,1]])

new = old
new[0, :2] = 0

print(old)

old = np.array([[1,1,1], [1,1,1]])

new = old.copy()
new[:,0] = 0

print(old)

['a','b','c'] + [1,2,3]

list_num = []

for i in range(0,36):
    list_num.append(i)

a = np.array(list_num)

a[::7]

a[2::2,2::2]
a[2:4,2:4]
a[::2,::2]
a[[2,3],[2,3]]
