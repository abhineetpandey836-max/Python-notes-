#Operators are used to perform operations on variables and values. Python has the following operators:
# 1) Arithmetic operators
# 2) Comparison operators
# 3) Logical operators
# 4) Bitwise operators
# 5) Assignment operators
# 6) Identity operators
# 7) Membership operators

# -------------------------1)Arithmetic operators------------------------------>
# Arithmetic operators are used to perform mathematical operations like addition, subtraction, multiplication, division, etc
x = 10
y = 3
print(x + y) #addition operator
print(x - y) #subtraction operator
print(x * y) #multiplication operator
print(x / y) #this will return float value, division operator
print(x // y) #this will return integer value, integer division operator
print(x % y) #this will return remainder, modulus operator
print(x ** y) #this will return x raised to the power of y, power operator
# -------------------------2) Comparison Operator------------------------------>
print(x < y) #this will return False, comparison operator, less than operator
print(x > y) #this will return True, comparison operator, greater than operator
print(x == y) #this will return False, comparison operator, equal to operator
print(x != y) #this will return True, comparison operator, not equal to operator
print(x <= y) #this will return False, comparison operator, less than or equal to operator
print(x >= y) #this will return True, comparison operator, greater than or equal to operator
# -------------------------3)Logical operators------------------------------>
# Logical operators are used to combine conditional statements. They are and, or, not
x = True
y = False
print(x or y) #or operator
print(x and y) #and operator
print(not x) #not
# --------------------------4)Bitwise Operator-------------------------------->
#Bitwise Operator are the operators which 
x = 2
y = 3
print(x & y) #Bitwise AND Operator
# 010
# 110
# ---
# 010
print(x | y)
print(x >> 2)
print(y << 3)
# --------------------------5)Assignment Operator------------------------------>
a = 3
print(a)
a += 3
# a = a + 3
print(a)
a -= 3
a *= 3
a &= 3
# --------------------------6)Identity Operator-------------------------------->
# This check if any two variable is on same memory location or not
a = 3
b = 3
print(a is b)
# Output: True (Is operator tells us about memory location.This means a and b is on same memory location so they are identical)
a = "Hello"
b = "Hello"
print(a is b)
# Output--> True (Is operator tells us about memory location.This means a and b is on same memory location so they are identical)
a = [1,2,3]
b = [1,2,3]
# Output: False (Is operator tells us about memory location.This is stored in different memory location therefore false)
a = "Hello-world"
b = "Hello-world"
print(a is b)
# Output: False (Stored in two different memory location)
# --------------------------7)Membership Operator-------------------------------->
# Membership operator helps us get to know if there is something present in input value or not. Quite useful and specific to python:)
x = "Delhi"
print("D" in x) #Output: True
print("D" not in x) #output: False