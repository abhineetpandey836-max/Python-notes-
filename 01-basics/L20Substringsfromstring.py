# Accessing Substrings from a String
# Concept of Indexing
c = "hello"
print(c)
# h index position is 0, and o index position is 4
print(c[0])
# in a way i am saying is to give me the first character of this string "hello"
print(c[1])
print(c[2])
print(c[3])
print(c[4])
# Types of Indexing
# 1) Positive Indexing
# 2) Negative Indexing
print(c[-5])
# Slicing
c = "Hello World"
print(c)
print(c[0:1])
# you can slice the words in way by writing 0:1 you slice H with ello World, with 5 you slice World
print(c[2:])
# output is llo World
print(c[:4])
# output is Hell
print(c[:])
# output is Hello World
print(c)
# output is Hello World
print(c[2:6:2])
# here we are saying from character 2 to 5 we want all character but because of last 2, it skips 1
# so output will be ---  lo
# so from Hello World, we started from l then skips one l because of 2 and output is o and then space, after 2 to 6 it doesn't print/
print(c[0:8:3])
# so output is --HlW because it starts from first word H and till 8 characters, it skips 2.
print(c[0:6:-1])
# output--(Empty)
# We can't take negative indexing when we are working with positive indexing
# for negative indexing-
print(c[-5:-1:2])
# in this we starts at l(l is -2) and ends with W(W is -5)
# we skips 1 letter because of 2 so output is
# Wr
print(c[::-1])
# this reverse the entire input
# output- dlroW olleH