#Create a tuple containing:
number=(10,20,30,40,50)
print(number)

'''Q2. Access an element

Given:

fruits = ("apple", "banana", "mango", "orange")

Print "mango" using its index.'''

fruits = ("apple", "banana", "mango", "orange")
print(fruits[2])

'''Q3. Negative indexing

Given:

numbers = (10, 20, 30, 40, 50)

Print the last element using negative indexing.'''
numbers = (10, 20, 30, 40, 50)
print(numbers[-1])

'''Q4. One-element tuple

Create a tuple containing only "Python".

Important: Make sure it is actually a tuple.'''
program=("Python",)
print(program)

'''Q5. Find length

Given:

colors = ("red", "blue", "green", "yellow")

Find and print the number of elements.'''
colors = ("red", "blue", "green", "yellow")
print(len(colors))

'''Slice a tuple

Given:

numbers = (10, 20, 30, 40, 50, 60)

Print:

(20, 30, 40)'''
numbers = (10, 20, 30, 40, 50, 60)
print(numbers[1:4])

'''Q7. First three elements

Given:

numbers = (5, 10, 15, 20, 25, 30)

Use slicing to print the first three elements.'''

numbers = (5, 10, 15, 20, 25, 30)
print(numbers[:3])

'''Q8. Last three elements

Using slicing, print the last three elements.'''
print(numbers[3:])

'''Q9. Reverse a tuple

Given:

numbers = (1, 2, 3, 4, 5)

Reverse it using slicing only.

Expected:

(5, 4, 3, 2, 1)'''
numbers = (1, 2, 3, 4, 5)
print(numbers[::-1])

'''Q10. Every second element

Given:

numbers = (10, 20, 30, 40, 50, 60)

Use slicing to print:

(10, 30, 50)'''
numbers = (10, 20, 30, 40, 50, 60)
print(numbers[::2])

'''Level 3 — Tuple Operations
Q11. Concatenation

Given:

a = (1, 2, 3)
b = (4, 5, 6)

Join both tuples and print the result.

Expected:

(1, 2, 3, 4, 5, 6)'''

a = (1, 2, 3)
b = (4, 5, 6)
c=a+b
print(c)

'''Q12. Repetition

Given:

numbers = (1, 2)

Repeat the tuple 3 times.

Expected:

(1, 2, 1, 2, 1, 2)'''

numbers = (1, 2) * 3
print(numbers) 

'''Q13. Membership

Given:

fruits = ("apple", "banana", "mango")

Check whether "banana" exists in the tuple.'''
fruits = ("apple", "banana", "mango")
print("banana" in fruits)

'''Q14. not in

Check whether "orange" is not present in the tuple.'''
print("orange" not in fruits)

'''Q15. Combine operations

Given:

a = (10, 20)
b = (30, 40)

Concatenate them and then repeat the resulting tuple 2 times.'''
a = (10, 20)
b = (30, 40)
c=(a+b)
print(c*2)

'''🔵 Level 4 — Tuple Methods

Remember, tuples have fewer methods than lists because tuples cannot be changed.

Q16. count()

Given:

numbers = (10, 20, 10, 30, 10, 40)

Count how many times 10 appears.'''
numbers = (10, 20, 10, 30, 10, 40)
print(numbers.count(10))

'''Q17. index()

Given:

fruits = ("apple", "banana", "mango", "orange")

Find the index of "mango".'''
fruits = ("apple", "banana", "mango", "orange")
print(fruits.index(("mango")))

'''Q18. Both methods

Given:

numbers = (5, 10, 5, 20, 5, 30)

Find:

How many times 5 appears
The index of the first 5'''

numbers = (5, 10, 5, 20, 5, 30)
print(numbers.count(5))
print(numbers.index(5))