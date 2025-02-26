# if statement
# if True, then execute
age = int(input("What's your age? "))
if age == 18:
    print("You are an adult")
print("Your age is ", age)
# if_else statement
# if condition is true, then execute the code in the if block
# if condition is false, then execute the code in the else block

age = int(input("What's your age? "))
if age >= 18:
    print("You are an adult")
else:
    print("You are not adult")

# if_elif_else statement
# if condition is true, then execute the code in the if block
# if condition is false, then check the elif condition
# if elif condition is true, then execute the code in the elif block
# if elif condition is false, then execute the code in the else block
age = int(input("What's your age? "))
if age >= 18:
    print("You are an adult")
elif age >= 14:
    print("You are a teenager")
else:
    print("You are a kid")
