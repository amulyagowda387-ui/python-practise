'''1. Arithmetic Operators

Practice +, -, *, /, %, //, **.

Q1. Take two numbers as input and print:

Addition
Subtraction
Multiplication
Division'''
a=int(input("a = " ))
b=int(input("b = " ))
print(a)
print(b)
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a%b)
print(a//b)
print(a**b)

'''Take a number and print its:

Square
Cube'''
num=int(input("enter u r number : "))
print("square =", num **2)
print("cube ", num**3)


'''Q3. Take two numbers and print the remainder and floor division result.'''
a=int(input("enter u r number :"))
b=int(input("enter u r number :"))
print(a%b)
print(a//b)

#4.  A student scored marks in 3 subjects. Take the marks as input and print the total and average.
marks1=int(input("enter u r marks in subject1 :"))
marks2=int(input("enter u r marks in subject2 :"))
marks3=int(input("enter u r marks in subject3 :"))
print("total ", = marks1+marks2+marks3)
average=total/3 '''

'''2. Assignment Operators

Practice =, +=, -=, *=, /=, %=.

Q5. Create a variable x = 10. Increase it by 5 using +=.

Q6. Create x = 50. Decrease it by 20 using -=.

Q7. Create x = 10. Multiply it by 3 using *=.

Q8. Create x = 100. Divide it by 4 using /=.

Q9. Create x = 25. Find the remainder when divided by 4 using %=''''''

x=10
x+=5
print(x)

x=50
x-=20
print(x)

x=10
x*=3
print(x)

x=100
x/=4
print(x)

x=25
x%=4
print(x)


'''3. Comparison Operators

Practice ==, !=, >, <, >=, <=.

Q10. Take two numbers and check whether they are equal.

Q11. Take two numbers and check whether the first number is greater than the second.

Q12. Take two numbers and check whether the first number is smaller than the second.

Q13. Take your age as input and check whether it is greater than or equal to 18.

Q14. Take two numbers and print the results of:

>
<
==
!=

x=10
y=20
print(x==y)
print(x<y)
print(x>y)'''

age=int(input("enter u r age :"))
print(age>=18)

num1=int(input("enter u r number :"))
num2=int(input("enter u r number :"))
print(num1>num2)        
print(num1<num2)
print(num1==num2)
print(num1!=num2)

'''4. Logical Operators

Practice and, or, not.

Q15. Take your age and check:

age >= 18 and age <= 60

Q16. Take two numbers and check whether:

both are greater than 10.

Q17. Take a number and check whether it is either less than 10 or greater than 50.

Q18. Create two Boolean variables:

a = True
b = False

Print the results of:

a and b
a or b
not a
not b'''

age=int(input("enter u r age :"))
print(age >= 18 )
print(age <= 60)

num1=int(input("enter num1 :"))
num2=int(input("enter num2 :"))
print(num1>10 and num2>10)

num=int(input("enter u r number :"))
print(num<10 or num>50)

is_student=True
is_weather=False

'''5. Membership Operators

Practice in and not in.

Q19. Take a name as input and check whether "a" is present in the name.

Q20. Check whether "Python" is present in:

text = "I am learning Python"

Q21. Check whether "Java" is not present in the same string.

Q22. Create:

fruits = "apple banana mango orange"

Check whether "mango" is present.'''

name=input("enter u r name :")
print("a" in name)

text="Iam learning python"
print("python" in text)
print("java" not in text)

fruits = "apple banana mango orange"
print("mango" in fruits)

'''6. Bitwise Operators

Practice:

& | ^ ~ << >>

Q23. Take two numbers and find their bitwise AND.

Q24. Take two numbers and find their bitwise OR.

Q25. Take two numbers and find their bitwise XOR.

Q26. Take a number and apply the bitwise NOT operator.

Q27. Take a number and perform:

Left shift by 1
Right shift by 1'''

num1=int(input("enter u r number1 :"))
num2=int(input("enter u r number2 :"))
print(num1 & num2)
print(num1 | num2)
print(num1 ^ num2)
print(~num1)

num=int(input("enter u r number :"))
print(num<<1)
print(num>>1)

'''Accessing String Characters

Q28. Create:

name = "Amulya"

Print:

First character
Last character
Third character
name = "Amulya"
print(name[0])
print(name[-1])
print(name[2])'''

'''Q29. Take a word as input and print its first character.

Q30. Take a word as input and print its last character.

Q31. For:

text = "Python"

Print each character using its index.'''

word=input("enter u r word :")
print(word[0])
print(word[-1])
text='python"' 
print(text[0], text[1], text[2], text[3], text[4], text[5])

'''String Slicing

Q32. For:

text = "Python"

Print:

Pyt

using slicing.'''
text="python"
print(text[:3])

'''Print:

hon

using slicing.

Q34. Print the first 4 characters.

Q35. Print the last 3 characters.

Q36. Reverse the string using slicing.'''

text="python"
print(text[3:6])
print(text[:4])
print(text[-3:])
print(text[::-1])

'''practice these methods:

upper()
lower()
capitalize()
title()
strip()
replace()
find()
count()
startswith()
endswith()'''

text = "python programming"
print(text.upper())
print(text.lower())
print(text.capitalize())
print(text.title())
print(text.strip())
print(text.replace("python", "java"))
print(text.find("programming"))
print(text.count("python"))
print(text.startswith("python"))
print(text.endswith("python"))
      
