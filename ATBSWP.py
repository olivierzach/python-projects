# -*- coding: utf-8 -*-
"""
Created on Thu Mar 15 15:53:10 2018

@author: zolivier
"""

# https://automatetheboringstuff.com/chapter0/


print("hello world")


2 + 3
#Out[18]: 5

(2 + 3) * 6
#Out[19]: 30


2+2
#Out[20]: 4

'Hello World!'
#Out[21]: 'Hello World!'

'Zach' + 'Olivier'
#Out[22]: 'ZachOlivier'

'Zach' * 10
#'ZachZachZachZachZachZachZachZachZachZach'

spam = 40
spam
#Out[25]: 40

eggs = 2
eggs
#Out[27]: 2


spam + eggs
#Out[28]: 42

spam + eggs + spam*2
#Out[29]: 122

spam = spam + 2
spam
#Out[31]: 42

spam = 'Hello'
spam
#Out[33]: 'Hello'

spam = 'Goodbye'
spam
#Out[35]: 'Goodbye'

# this program says hello and asks for my name
print('Hello!')
print('What is your name?')

# more printing with inputs
myName = input()
print('It is good to meet you,' +myName)

# calculations with inputs
print('the length of your name is:')
print(len(myName))

# more inputs - age
print('What is your age?')
myAge = input()
print('you will be ' + str(int(myAge) + 1) + ' in a year!')


## lets go through the above script

# input function
myName = input() # user inputs name in console
myName # myName variable will now have user inputted name stored inside it
#Out[43]: 'zach'


# we can use the input as a variable in other calculations
print('it is good to meet you, ' + myName)
#it is good to meet you, zach

# length
len('hello')
#Out[40]: 5

len('my very energetic monster just scarfded nachos')
#Out[41]: 46

# printing with inputs
len(myName)
#Out[45]: 4

# data types with str() int() and float()
str(29)
#Out[46]: '29'

print('I am ' + str(29) + ' year old')
#I am 29 year old

str(0)
#Out[48]: '0'

str(-3.14)
#Out[49]: '-3.14'

int('42')
#Out[50]: 42

int('-99')
#Out[51]: -99

int(1.99)
#Out[52]: 1

float('3.14')
#Out[53]: 3.14

float(10)
#Out[54]: 10.0

# all user inputs will be stored as strings unless otherwise told
spam = input() # user inputs 101
spam
#Out[56]: '101'

# using int
spam = int(spam)
spam
#Out[58]: 101

spam * 10 / 5
#Out[59]: 202.0


# rounding up
int(7.7)
#Out[60]: 7

# rounding down
int(7.7) + 1
#Out[61]: 8


print('what is your age?')
myAge = input()
print('you will be ' + str(int(myAge) + 1) + ' in one year')

#print('what is your age?')
#myAge = input()
#print('you will be ' + str(int(myAge) + 1) + ' in one year')
#what is your age?
#105
#you will be 106 in one year



# text and number equivalence
42 == '42'
#Out[63]: False

42 == 42.0
#Out[64]: True

42 == 0042.0000000000
#Out[65]: True



# comparison operators - evaluates to true or false
42 == 42
#Out[66]: True

42 == 99
#Out[67]: False

2!= 3
#Out[68]: True

2 != 2
#Out[69]: False

'hello' != 'hello'
#Out[70]: False

'hello' == 'Hello!'
#Out[71]: False

'dog' != 'cat'
#Out[72]: True

# less than or greater than operators
42 < 100
#Out[75]: True

42 > 100
#Out[76]: False

42 < 42
#Out[77]: False

eggCount = 42
eggCount > 42
#Out[79]: False

myAge = 29
myAge >= 10
#Out[85]: True

# difference between == and =
# the == operator (equal to) asks whether two values are the same as each other
# the = operator (assignment) puts the value on the right into the variable on the left
# the != operator also consists of two characters

# binary boolean operators
# "and" and "or"
True and True
#Out[86]: True

False and True
#Out[87]: False

True or False
#Out[88]: True

False or True
#Out[89]: True

# not operator
not True
#Out[90]: False

not not not not True
#Out[91]: True

# mixing boolean and comparison operators
(4 < 5) and (5 < 6)
#Out[92]: True

2 + 2 == 4 and not 2 + 2 == 5 and 2 * 2 == 2 + 2
#Out[93]: True


# flow control - blocks of code
name = 'Zach'
password = 'olivier'

if name == 'Zach':
    print('Hello Zach')
    if password == 'olivier':
        print('access granted')
    else:
        print('wrong password')

#Hello Zach
#access granted

# flow control statements
# conditional statements
 
# if statements    
name = 'zach'    
if name == 'zach':
    print('hi, zach')       
#hi, zach
    

# else statements
name = 'bob'

if name == 'alice':
    print('hi alice')
else:
    print('hello stranger')
#hello stranger
    
# elif statements = ELSE IF statements

name = 'bob'
age = 5

if name == 'Alice':
    print('hi alice')
elif age < 12:
    print('you are not alice')
#you are not alice

# combining these all together
name = 'dracula'
age = 40000

if name == 'Alice':
    print('hi alice')
elif age < 12:
    print('you are not alice')
elif age >2000:
    print('you are dracula')
elif age >100:
    print('you are just old')
#you are dracula
    
# remember order matters in an if else statement
# the conditions will evaluate based on the first TRUE statement
# in our previous code if we switched lines we would evalute to the wrong statement
name = 'dracula'
age = 40000

if name == 'Alice':
    print('hi alice')
elif age < 12:
    print('you are not alice')
elif age >100:
    print('you are just old')
elif age >2000:
    print('you are dracula')
#you are just old

# using the else statement with elif    
name = 'Bob'
age = 30

if name == 'Alice':
    print('Hi, Alice.')
elif age < 12:
    print('You are not Alice, kiddo.')
else:
    print('You are neither Alice nor a little kid.')
#You are neither Alice nor a little kid.


# while loop statements
spam = 2 
if spam < 5:
    print('hello world')
    spam = spam + 1

spam































