#Literals in python
# The literals are the data which is given in a variable or constant. In python, there are various types of literals which we will learn in this file.
# Literals is a raw data given in a variable. In Python, there are four types of literals they are as follows:
# 1) Numeric literals
# 2) String literals
# 3) Boolean literals
# 4) Special literals
# -----------------------------Numeric literals----------------------------------------->
# Numeric literals are immutable (unchangeable). Numeric literals can belong to 3 different numerical types: int, float, complex. They are defined as follows:
a = 0b1010 #Binary Literals (Used in rasberry pi and microcontroller programming where we need to use binary literals to control pins by sending 1 and 0 patterns)
b = 100 #Decimal Literal
c = 0o310 #Octal Literal (0o is used to represent octal literals)
d = 0x12c #Hexadecimal Literal (0x is used to represent hexadecimal literals)
# --------------------------------Float Literal------------------------------
float_1 = 10.5
float_2 = 1.5e2 #1.5*10^2=150.0 (Making scientific notation in python, e is used to represent the power of 10)
float_3 = 1.5e-3 #1.5*10^-3=0.0015 (Making scientific notation in python, e is used to represent the power of 10)
# ------------------------------Complex Literal------------------------------
x = 3.14j #j is used to represent complex literals
print(a, b, c, d)
print(float_1, float_2, float_3)
print(x, x.imag, x.real) #x.imag is used to get the imaginary part of complex number and x.real is used to get the real part of complex number

#Note----------------x------------------x---->
# --------------#String literals: String literals in python are surrounded by either single quotation marks, or double quotation marks. We can use either single or double quotes to represent string literals. They are defined as follows:
single_quote = 'Single Quote'
double_quote = "Double Quote"


# X------------------------------------------x----------------------------------------------------------------------------------------------X
#Boolean literals: Boolean literals in python are either True or False. They are defined as follows:
bool_1 = True
bool_2 = False
#Special literals: Special literals in python are None. They are defined as follows:
none_literal = None 

# ----x-----x------>Above is just extra knowledge for you, you can skip it if you want to. It is not important for now, we will learn about it in detail in upcoming chapters.



print(single_quote, double_quote, bool_1, bool_2, none_literal)
#STRING LITERALS
#String literals in python are surrounded by either single quotation marks, or double quotation marks. We can use either single or double quotes to represent string literals. They are defined as follows:
string = 'This is Python'
strings = "This is Python"
char = "C" #In python there is no char data type, so we can use string data type to represent char data type.
multiline_string = """This is a multiline string with more than one line code."""
unicode = u"\U0001F600\U0001F606\U0001F923" #Unicode string literals are used to represent unicode characters in python. Unicode is a standard for representing text in different languages and scripts
raw_string = r"Raw \n string" #Raw string literals are used to represent raw strings in python. Raw strings are used to represent strings with special characters like \n, \t, etc. In raw strings, the backslash is treated as a literal character and not as an escape character.
print(string, strings, char, multiline_string, unicode, raw_string)

#------------------------------BOOLEAN LITERALS------------------------------>
#Boolean literals in python are either True or False. They are defined as follows:
a = True + 4
b = False + 10
print("a:", a) #a will be 5 because True is considered as 1 in python and False is considered as 0 in python.
print("b:", b) #b will be 10 because False is considered as 0 in python and True is considered as 1 in python.
#------------------------------SPECIAL LITERALS------------------------------>
#Special literals in python are None. They are defined as follows:
a = None
print(a) #a will be None because None is a special literal in python which represents the absence of a value or a null value.
# Variable declaration with none value
k = None # Declaring a variable with None value
print(k) #k will be None because None is a special literal in python which represents the absence of a value or a null value.