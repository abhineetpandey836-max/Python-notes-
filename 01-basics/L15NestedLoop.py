# Nested Loops
# in short, a nested loop is a loop inside another loop. The "inner loop" will be executed one time for each iteration of the "outer loop". Nested loops are often used to iterate over multi-dimensional data structures, such as lists of lists or matrices. They can also be used to generate combinations or permutations of elements.
# A nested loop is a loop inside another loop. The "inner loop" will be executed
# the time complexity of nested loops is O(n^2) because for each iteration of the outer loop, the inner loop runs n times. This means that the total number of iterations is n * n = n^2. As a result, the time complexity of nested loops is quadratic, which can lead to performance issues for large input sizes. 
# It is important to be mindful of the time complexity when using nested loops and to consider alternative approaches if necessary.
# But sometimes you have to use nested loops, like building social media platforms like facebook etc which need loop for users and 2nd loop for friends of users, so in this case we have to use nested loops. 
# But we can also use other data structures like hash tables or sets to reduce the time complexity of nested loops. 
# For example, if we need to check if an element exists in a list, we can use a set instead of a list, which has an average time complexity of O(1) for lookups, compared to O(n) for lists.
# This can significantly improve the performance of our code and reduce the need for nested loops.
# Pascal triangle of asterisk(*) is a triangle of numbers where each number is the sum of the two numbers directly above it. 
# The first row of the triangle is 1, and each subsequent row contains one more number than the previous row. 
# The triangle is named after the French mathematician Blaise Pascal, who studied its properties in the 17th century.
rows = int(input("Enter the number of rows: "))
for i in range(1, rows + 1):
    for j in range(0, i):
        print("*", end="")
    print("")