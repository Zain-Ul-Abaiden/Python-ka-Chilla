# loops in python
# for loop
# while loop
# break and continue statements

# while loop
print("while loop")

x = 0
while x < 5:
    print(x)
    x = x+1
print("done")
# output: 0,1,2,3,4,done

# for loop
print("for loop")
for x in range(5, 10):
    print(x)
print("done")
# output: 5,6,7,8,9,done

# another example
print("for loop with an array")
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
# output: apple,banana,cherry

# break and continue statements
# break statement
# The break statement is used to terminate the loop prematurely.
# It stops the execution of the loop and passes the control to the next statement after the loop.
# The break statement can be used with both for and while loops.

# example of break statement
print("break statement")
for x in range(5, 10):
    if x == 7:
        break
    print(x)
# output: 5,6

# continue statement
# The continue statement is used to skip the rest of the code inside a loop for the current iteration
# only and to move on to the next iteration.
# The continue statement can be used with both for and while loops.

# example of continue statement
print("continue statement")
for x in range(5, 10):
    if x == 7:
        continue
    print(x)
# output: 5,6,8,9
