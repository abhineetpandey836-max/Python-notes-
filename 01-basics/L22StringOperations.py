# String Operations
# There are 5 types of operations on string
# 1) Arithmetic Operations
# 2) Relational Operations
# 3) Logical Operations
# 4) Loops on Strings
# 5) Membership Operations

# Arithmetic Operator- There are two operators we use one is addition which is "Concatenation" and another is "Multiplication"
# 1) Plus Operator or Concatenation
print("Hello" + "-" + "world")
# 2) Multiplication
print("*"*50)
print("Hello"*4)
# Relational Operations
"Hello"=="WOrld"
"Hello"!="World"
"Mumbai" > "Pune"
# Output- False
# This output false coming from Lexiographically 
"Goa" < "Kolkata"
# Output - True
# 3) Logical Operations
"hello" and "world"
# Empty string-"" ko python False bolta hai
# "wr" non empty string ko python True bolta hai
"" and "Hello"
# output- ''
"" or "world"
# output-'world
"hello" or "world"
# output-'hello'
"hello" and "world"
# output- 'world'
not "hello"
# Output- False, because opposite of non empty string is empty string and empty string is False
not ""
# output- True
# 4) Loops on Strings
c = "hello world"
for i in c[2:7]:
    print(i)
    # slicing in loop
# 5) Membership Operator
# in and not in
c="hello world"
'h' in c
# output- True
'H' in c
# output - False
'world' not in c
# output- False