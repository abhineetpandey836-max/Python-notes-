# Built in Functions
# It is build in fx in python which is already defined in python and 
# we use them in our program to perform specific tasks.
# Some of the built-in functions in python are:
# print(), input(), len(), type(), int(), float(), str(), list(), tuple(), set(), dict(), range(), sum(), min(), max(), abs(), round(), sorted(), reversed(), enumerate(), zip(), map(), filter(), reduce() etc.
# 1) PRINT FUNCTION
print("Hello World") # this will print Hello World on the console
# 2) INPUT FUNCTION
name = input("Enter your name: ") # this will take input from the user and store it in the variable name
print("Hello", name) # this will print Hello followed by the user's name
# 3) len() FUNCTION
length = len(name) # this will return the length of the string name
print("Length of your name is:", length) # this will print the length of the user's name
# 4) type() FUNCTION
print(type(name)) # this will return the data type of the variable name, which is <class 'str'> because name is a string.
# 5) int() FUNCTION
num = int(input("Enter a number: ")) # this will take input from the user and convert it into an integer and store it in the variable num
print("You entered:", num) # this will print the number entered by the user
# and in Int FUNCTION WE HAVE float() function which is used to convert a string or a number into a float data type and str() function which is used to convert a number and list and tuple into a string data type.
# 6) abs() FUNCTION (Absolute function which means print absolute value of a number)
abs_num = abs(num) # this will return the absolute value of the number num
print("Absolute value of the number is:", abs_num) # this will print the absolute value of the number entered by the user
abs_num = abs(-4) # this will return 4 because the absolute value of -4 is 4
print("Absolute value of -4 is:", abs_num) # this will print the absolute value of -4
# 7) Power function
pow_num = pow(2, 3) # this will return 8 because 2 raised to the power of 3 is 8
print("2 raised to the power of 3 is:", pow_num) # this will print the result of 2 raised to the power of 3
# 8) Min and Max function
min_val = min(1, 2, 3, 4, 5) # this will return 1 because it is the minimum value among the given numbers
max_val = max(1, 2, 3, 4, 5) # this will return 5 because it is the maximum value among the given numbers
print("Minimum value is:", min_val) # this will print the minimum value
print("Maximum value is:", max_val) # this will print the maximum value
# 9) Round function
round_num = round(3.14159, 2) # this will return 3.14 because it rounds the number 3.14159 to 2 decimal places
print("Rounded value of 3.14159 to 2 decimal places is:", round_num) # this will print the rounded value of 3.14159 to 2 decimal places
# 10) divmod() function
divmod_result = divmod(10, 3) # this will return a tuple (3, 1) because 10 divided by 3 is 3 with a remainder of 1
print("Divmod of 10 and 3 is:", divmod_result) # this will print the result of divmod(10, 3)
# 11) bin/oct/hex function
bin_num = bin(10) # this will return '0b1010' because 10 in binary is 1010
oct_num = oct(10) # this will return '0o12' because 10 in octal is 12
hex_num = hex(10) # this will return '0xa' because 10 in    hexadecimal is a
print("Binary of 10 is:", bin_num) # this will print the binary representation of 10
print("Octal of 10 is:", oct_num) # this will print the octal representation of 10
print("Hexadecimal of 10 is:", hex_num) # this will print the hexadecimal representation of 10
# 12) ID function
id_num = id(num) # this will return the unique identifier of the variable num
print("ID of the variable num is:", id_num) # this will print the unique identifier of the variable num
# 13) ORD function
ord_num = ord('A') # this will return 65 because the ASCII value of 'A' is 65
print("ASCII value of 'A' is:", ord_num) # this will print the ASCII value of 'A'
# 14) len() function
len_num = len("Hello World") # this will return 11 because the length of the string "Hello World" is 11
print("Length of the string 'Hello World' is:", len_num) # this will print the length of the string "Hello World"
# 15) sum() function
sum_num = sum([1, 2, 3, 4, 5]) # this will return 15 because the sum of the numbers in the list [1, 2, 3, 4, 5] is 15
print("Sum of the numbers in the list [1, 2, 3, 4, 5] is:", sum_num) # this will print the sum of the numbers in the list [1, 2, 3, 4, 5]
# 16) Help function
help('print')
# so help function tells the documentation of any function of python, if you want to know official documentation of python, this is really helpful.
# :)Happy, it's 10:39 night
# 6/11/26