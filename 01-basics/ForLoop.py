# range function is used to generate a sequence of numbers. It can take one, two, or three arguments. 
# When called with one argument, it generates numbers from 0 up to (but not including) that number. When called with two arguments, it generates numbers from the first argument up to (but not including) the second argument. 
# When called with three arguments, it generates numbers from the first argument up to (but not including) the second argument, incrementing by the third argument.
list(range(1,11)) # this will return a list of numbers from 1 to 10 (inclusive) [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list(range(5)) # this will return a range object which is an iterable that generates numbers from 0 to 4 (inclusive) [0, 1, 2, 3, 4]
list(range(1,11,2)) # this will return a list of numbers from 1 to 10 (inclusive) with a step of 2 [1, 3, 5, 7, 9]
list(range(1,11,3)) # this will return a list of numbers from 1 to 10 (inclusive) with a step of 3 [1, 4, 7, 10]
list(range(10,0,-1)) # this will return a list of numbers from 10 to 1 (inclusive) in reverse order [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
# Sequence
# Any thing in order is called sequence. In python we have different types of sequence like list, tuple, string, range etc.
# We can use for loop to iterate through the sequence and perform operations on each element of the sequence.
"Kolkata" # this is a string sequence
["Kolkata", "Delhi", "Mumbai"] # this is a list sequence
for i in range(1,11,2): # this is a for loop that will iterate through the range of numbers from 1 to 10 (inclusive)
    print(i) # this will print the value of i in each iteration
for i in "Kolkata":
    print(i) # this will print each character of the string "Kolkata" in each iteration
for i in [1, 2, 3, 4, 5]:
    print(i) # this will print each element of the list [1, 2, 3, 4, 5] in each iteration
for i in (1, 2, 3, 4, 5):
    print(i) # this will print each element of the tuple (1, 2, 3, 4, 5) in each iteration
for i in {1, 2, 3, 4, 5}:
    print(i) # this will print each element of the set {1, 2, 3, 4, 5} in each iteration
# if we know beforehand that loop will run this specific time, then use for loop, if we don't know how many times loop will run then use while loop.