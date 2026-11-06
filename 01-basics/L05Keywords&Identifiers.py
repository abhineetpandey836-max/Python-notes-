# -------KEYWORDS
#Python is a case sensitive programming language
#Programming, a keyword is a word that is reserved by a program
# because the world has a special meaning. Keywords can be commands or parameters.
#Every programming language has a set of keywords that cannot be used as variable names.
#python has 33 keywords
import keyword
print(keyword.kwlist)
#-------iDENTIFIER
#A Python identifier is a name used to identify a variable, function,class,module or other object.
# -------RULES for setting identifiers
# 1 )can only start with an alphabet or __
# 2)followed by 0 or more letter, _ and digits
# 3)keywords cannot be used as an identifiers
#EXAMPLES--------------->
first_name = "Abhi"
print(first_name)
__="Abhi"
print(__) #You can do it with __(this) but not with --(this) or any other symbols, apart from alphabet
#False = "Ab"
# print(False) #keywords cannot be used as an identifier, you can check it by removing comments, it will show error/
fir0000= "A" #can do it with alphabet at first followed by digit as mentioned above. Read/
print(fir0000) 
Happy_learning = "Happy learning open next chapter"
print(Happy_learning)