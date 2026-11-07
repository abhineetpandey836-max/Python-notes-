# Editing String
c = "Hello"
print(c)
# c[0] = 'X'
# Strings are a Immutable Data Type, IF WE MAKE STRING IN PYTHON WE CAN'T EDIT
# you can see error in there saying error in line 4 if you remove that comment.
c = "world"
print(c)
# c[5] = "X"
# You also can't add characters
# you will see error saying error in line 8 if you remove that comment.
# Deleting String
del c
print (c)
# you see you can't find string as it is now deleted
c = "hello"
print(c)
# Here is one more case here:
del c[0]
# here we see error because you can't delete particular character as it will creates changes in string because strings are immutable so it can't/
del c[:3:2] 
# we can't portion of string
# in portion of string you can't delete because it is immutable
# Conclusion---->>>
# In string we can't edit string,can't delete partially, can't add new characters in string, you can reassign characters in string and can delete string completely 