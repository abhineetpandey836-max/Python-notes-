#static software where there is no exchange of conversation between user and interface, we can't converse or put our inputs in that software. Examples are Govt website, Uni interface
#Then there is dynamic software, where we put inputs in software like zomato in that we share our location, numbers, details for certain service
#99% software we use today is dynamic software
#In all programming language there is mechanism given functionality for user input to have dynamic software.
# examples---
input("Apna naam batao") #this is a function which takes input from user and returns it to the program
first_num = input("Enter the first number")
second_num= input("Enter the second number")
print(first_num)
print(second_num)
result = first_num + second_num
print(result) #this will give output as 12 if we enter 1 and 2, so IF WE ENTER 12, 13: output is 1213 here because input function takes input as string, so we need to convert it into integer or float to get the correct output.
#So we can use int() or float() to convert the input into integer or float
#CORRECTION-------
result = int(first_num) + int(second_num)
print(result) #this will give output as 3 if we enter 1 and 2, it gives output as 25 if we enter 12 and 13, so now it is correct output.
#to fix above issue we use type conversion that we will learn in next file names Type Conversion in Python.
#----------------IMPORTANT NOTE: input function takes input Using the input function the user input will always be in a string format because there is no other way to take input,and why python thought to take it in string because string is the universal format which can hold other data types, so we need to convert it into integer or float to get the correct output.
#type function it is used to check the data type of a variable or value, it returns the data type of the variable or value.
type(15) #this will return <class 'int'> because 15 is an integer. Don't worry about <class 'int'>, it is just a representation of data type, we will learn about it in detail in upcoming chapters. And practice it by opening separate python file and writing type(15) and run it, you will get the same output.
type(first_num) #this will return <class 'str'> because first_num is a string, it is a variable which holds the value of input function which is always in string format.
