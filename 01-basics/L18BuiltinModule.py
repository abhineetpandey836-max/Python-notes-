# What are Modules?
# Consider a module to be the same as a code library.
# A file containing a set of function you want to include in your application.
# Examples of python modules
# · MATH
# · RANDOM
# · OS
# · TIME
# help('modules')
# In C Programming
# include <stdio.h>
import math
math.pi
# this gives us value of pi
math.factorial(6)
# this gives us factorial of 6
math.ceil(6.3)
# this gives us 7
math.floor(6.9)
# this gives us 6
math.sqrt(100)
# this gives us square root of 100 is 10
import random
random.randint(1,100)
# from 1 to 100, this gives random integer is selected between 1 to 100
a = [1,2,3,4,5]
random.shuffle(a)
# this is permanent shuffling so we have to put value in variable (a). And this shuffle that values like we do card
# output:[2,3,4,1,5]
import.time
time.time()
# this is time stamps, this tells about 1 jan to till this moment total seconds it tells us in real time
time.ctime()
# this tells current time according to your geo location
print("Hello")
time.sleep(1)
print("World")
# Output- Hello
# Output- World
# in time.sleep(1) module we get output 1 first and then after delay of 1 second, next module print
import os
os.getcwd()
# this gives our current working directory
os.listdir()
# this list our current files and other files together