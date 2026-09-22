# Write a Python program that performs basic arithmetic operations
#  (addition, subtraction, multiplication, and division) on two numbers.
x=10
y=20
print(x+y)
print(x-y)
print(x*y)
print(x/y)


# Define the two numbers as variables within the code and print the results for each operation.
x=2
y=2
print(x)
print(y)

'''Write a Python program that swaps the values of two variables with and without 
using a third variable
using a third variable'''
x=10
y=20

temp=x
x=y
y=temp

print(x)
print(y)

#without using third variable

x=10
y=20
x,y = y,x
print(x)
print(y)

#2. Create two variables a and b and store 15 and 25. Print both values.
a=15
b=25
print(a)
print(b)

#Create variables for your name, age, and college and print all three
name="amulya"
age=20
college="cbit"
print(name)
print(age)
print(college)

#Create two variables length = 10 and width = 5. Print both values.
length=10
width=5
print(length)
print(width)

'''5. Create variables containing:

an integer
a float
a string
a boolean

Print all four.'''
words=20
weight=2.5
name="amulya"
student=True
print(words)
print(weight)
print(name)
print(student)

#7. Create a variable marks = 85 and print its data type using type().
marks=85
print(type(marks))

'''Type Conversion

8. Convert the following string into an integer and print it:'''
num="100"
num=int(num)

'''Convert this integer into a float:

x = 10'''
x=10
x=float(x)
print(x)

'''Convert this integer into a string:

age = 20'''
age=20
age=str(age)
print(age)

'''12. Take a number as a string, convert it into an integer,
 and add 10 to it'''
num="100"
num=int(num)
num+=10
print(num)

'''Level 5 — Assigning Values to Multiple Variables

18. Assign the values 10, 20, and 30 to three variables a, b, and c in a single line.

19. Write Python code to assign the same value 100 to three variables x, y, and z in a single line.

20. What will be the output?

21. Assign your name, age, and marks to three variables in a single line and print them.'''

a,b,c=10,20,30
x,y,z=100,
name,age,marks=amulya,20,25
print(name)
print(age)
print(marks)