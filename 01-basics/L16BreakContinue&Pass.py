# Break statement
# It breaks the running LOOP and transfers the control to the next statement after the loop.
# example
for i in range(1, 11):
    if i == 5:
        break
    print(i)
print("Loop ended.")
# Continue statement
# It skips the current iteration of the loop and transfers the control to the next iteration of the loop.
# example
for i in range(1, 11):
    if i == 5:
        continue
    print(i)
print("Loop ended.")
# Pass statement
# It is a null statement in python. It is used when a statement is required syntactically but you do not want any command or code to execute.
# example
for i in range(1, 11):
    if i == 5:
        pass
    print(i)
print("Loop ended.")