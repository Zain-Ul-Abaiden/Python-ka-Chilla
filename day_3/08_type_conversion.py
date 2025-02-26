# data types

x = 5  # int
y = 5.5  # float
z = "Hello"  # string
a = [1, 2, 3]  # list of integers
b = ['Saima', 'Fatima', 'Ayesha']  # list of strings
c = (1, 2, 3)  # tuple of integers
d = {'name': 'Saima', 'age': 25}  # dictionary
e = {1, 2, 3}  # set of integers
f = True  # boolean

# type conversion
# int() - converts to integer
# float() - converts to float
# str() - converts to string
# bool() - converts to boolean

age = input("What's your age? ")
print(type(age))  # <class 'str'>
age = int(age)
print("Now type of age become int", type(age))  # <class 'int'>

name = input("What's your name? ")
print(type(name))  # <class 'str'>
