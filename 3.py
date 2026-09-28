'''1. Personal Introduction

Write a program that asks the user for:

Name
Age
College'''

print("My name is amulya")
print("I am 54 years old")
print("I study at cbit")

'''2. Favorite Things

Ask the user for their:

Favorite color
Favorite food
Favorite movie

Print all three in one sentence.'''
favourite_colour = input("favourite_colour : ")
favourite_food = input("favourite_food : ")
favourite_movie = input("favourite_movie : ")
print(f" My favourite colour is {favourite_colour}, my favourite food is {favourite_food}, and my favourite movie is {favourite_movie}")

'''3. Greeting

Ask the user's name and print:'''
user_name=input("enter u r name :")
print(f"Hello {user_name} ! ")
print("welcome to python programming")

'''4. Name in Different Ways

Ask for the user's name.

Print it using:

+ operator
f-string'''
user_name=input ("enter u r name :")
print("Hello "  + " " + user_name)
print(f" hello {user_name}")

'''5. Simple Profile

Ask for:

Name
Age
City'''
print("---- My profile ----")
name=input(" name :")
age=input(" age :")
city=input(" city :")
print("-----------------------")



'''String Manipulation


Ask for first name and last name separately.'''

first_name=input("enter your first name :")
last_name=input("enter your last name :")
print(f" my full name is {first_name} {last_name}")

'''College Email

Ask the user for:

Name
College name'''
name=input("enter your name :")
college_name=input("enter your college name :")
print(f"Hello  {name}")
print(f" your studying at {college_name} college") 


'''Sentence Maker

Ask the user for:

Name
Favorite hobby
Favorite food'''

name=input("enter your name :")
hobby=input("enter your favourite hobby :")
food=input("enter your favourite food :")
print(f"{name} likes coding and her hobby is {hobby} and her favourite food is {food}")


'''Swap First and Last Name'''
first_name=input("enter u r first name :")   
last_name=input("enter u r last name :")
print(f"{last_name} {first_name}")


'''About Me

Ask the user for:

Name
Age
Course
College
use\n'''

name=input("enter your name :")
age=input("enter your age :")
course=input("enter your course :")
college=input("enter your college name :")
print(f"hello ! my name is {name} \n i am {age} years old \n i am studying BE in {course} \n my college is {college} college")


'''Restaurant Menu

Print this exactly:

----- MENU -----
1. Pizza
2. Burger
3. Pasta
4. Sandwich
---------------

Use \n.'''
print("-----MENU-----")
print("pizza", "\n", "burger", "\n", "pasta", "\n", "sandwich")


'''Shopping List

Print:

Shopping List:
    Milk
    Bread
    Eggs
    Rice

Use \t for the spaces before the items.'''
print("Shopping List:")
print("Milk" "\t" "rice")
print("\tBread")
print("\tEggs")


'''Quotation

Print:

He said, "Python is easy to learn."

Use an escape sequence for the quotation marks.'''
name=input("python :")
print(f" He said,\t {name}")


'''File Path

Print:

C:\Users\Amulya\Desktop\Python

Use \\ where necessary'''

print("C:\\Users\\Amulya\\Desktop\\Python")

