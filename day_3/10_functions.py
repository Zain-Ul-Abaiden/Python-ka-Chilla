# functions in python

# simple function defination
def greet():
    print("Good Morning!")
    print("Good Morning!")
    print("Good Morning!")
    print("Good Morning!")
    print("Good Morning!")
    print("Good Morning!")


greet()


# another step
def greet():
    greetings = "Good Evning!"
    print(greetings)
    print(greetings)
    print(greetings)
    print(greetings)


greet()


# function defination with arguments

def greet(name):
    print("Hello, " + name + "!")


greet("zain")

# advance


def age_fun(age):
    if age >= 18:
        print("You are an adult")
    elif age >= 14:
        print("You are a teenager")
    else:
        print("You are a kid")


age = int(input("What's your age? "))
age_fun(age)
