# We are gonna study loops also called iteration control blocks. In programming, if we need to do
# something repeatedly, we can use loops.
# Loops are used to execute a block of code multiple times until a certain condition is met.
# There are different types of loops in programming, such as for loops and while loops.
# In loop examples, for flipkart or zomato, we have lakhs of products or items or food in these sites, 
# Question -so should we make lakhs of containers for each product or food item? 
# No, we can use loops to iterate through the list of products or food items and display them one by one.
# We make single container and use loops to iterate through the list of products or food items and display them one by one. This way, we can efficiently handle large amounts of data without creating unnecessary containers for each item.
# We fetch data from the database and use loops to iterate through the list of products or food items and display them one by one. This way, we can efficiently handle large amounts of data without creating unnecessary containers for each item.
# Zomato use similar format to display food items in their app. They fetch data from the database and use loops to iterate through the list of food items and display them one by one. This way, they can efficiently handle large amounts of data without creating unnecessary containers for each item.
# In python we have two types of loops - for loop and while loop. In this lesson, we will focus on the while loop.
# WHILE LOOP - A while loop is a control flow statement that allows code to be executed repeatedly based on a given Boolean condition. The while loop can be thought of as a repeating if statement. The while loop will continue to execute the block of code as long as the specified condition evaluates to True. Once the condition becomes False, the loop will terminate, and the program will continue with the next statement after the loop.
number= int(input("Enter a number: "))
i = 1
while i < 11:
    print(number, "*", i, "=", number*i)
    i+=1