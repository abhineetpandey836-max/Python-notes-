#In previous input function file, We were learning to take user input but unfortunately we got to know that the input function takes input in string format, so we need to convert it into integer or float to get the correct output.
#So in this file we will learn about type conversion in python.
# First we will learn about type conversion in python, it is a process of converting one data type into another data type.
# There are two types of type conversion in python, implicit and explicit.
#implicit type conversion happens when  python automatically converts one data type into another data type, it is also known as type casting. It happens when we perform operations on different data types, python automatically converts the data type of one operand into another data type to perform the operation.
#examples of implicit type conversion
from numpy import take


4 + 5.0 #this will return 9.0 because python automatically converts the integer 4 into float 4.0 to perform the operation, so the result is float 9.0
5 + 6+7j #this will return (11+7j) because python automatically converts the integer 5 into complex 5+0j to perform the operation, so the result is complex (11+7j)
4.5 + 5+5j #this will return (9.5+5j) because python automatically converts the float 4.5 into complex 4.5+0j to perform the operation, so the result is complex (9.5+5j)
#explicit type conversion happens when we manually convert one data type into another data type, it is also known as type casting. It happens when we use built-in functions like int(), float(), str() to convert one data type into another data type.
#example of explicit type conversion
#we did first_num + second_num in these cases we have to do explicit type conversion to get the correct output, so we will use int() or float() to convert the input into integer or float.
#int function
int("10") #this will return 10 because we are converting string "10" into integer 10
int('10') #this will return 10 because we are converting string '10' into integer 10
int(10.5) #this will return 10 because we are converting float 10.5 into integer 10, it will remove the decimal part and return the integer part only.
float(4) #this will return 4.0 because we are converting integer 4 into float 4.0
float("4.5") #this will return 4.5 because we are converting string "4.5" into float 4.5
str(6) #this will return '6' because we are converting integer 6 into string '6'
bool(1) #this will return True because we are converting integer 1 into boolean True, any non-zero integer is considered as True in boolean.
complex(4) #this will return (4+0j) because we are converting integer 4 into complex (4+0j)
list('Hello') #this will return ['H', 'e', 'l', 'l', 'o'] because we are converting string 'Hello' into list ['H', 'e', 'l', 'l', 'o']
a = 4.5
int(a) #this will return 4 because we are converting float 4.5 into integer 4, it will remove the decimal part and return the integer part only.
print(a) #this will return 4.5 because we are not changing the value of a, we are just converting it into integer and printing it, so the value of a remains same.
print(int(a)) #this will return 4 because we are converting float 4.5 into integer 4, it will remove the decimal part and return the integer part only.
# Solution of our previous problem
first_num = input("Enter the first number")
second_num= input("Enter the second number")
result = int(first_num) + int(second_num)
print(result) #this will give output as 3 if we enter 1 and 2, it gives output as 25 if we enter 12 and 13, so now it is correct output.
#effective coding
first_num = int(input("Enter the first number"))
second_num= int(input("Enter the second number"))
result = first_num + second_num
print(result) #this will give output as 3 if we enter 1 and 2, it gives output as 25 if we enter 12 and 13, so now it is correct output.
# This is useful when we want to take input from user and convert it into integer or float in one line of code, so that we don't have to write two lines of code for taking input and converting it into integer or float.
Abhineet= "Happy learning open next chapter"
print(Abhineet)