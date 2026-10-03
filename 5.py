'''list
a list is a collection of items tht is orderd mutable  , it allow duplicate elements and can have different data types
my_list=[apple,banana,fruit]'''

'''Accessing list elements'''
name=["amulya","sinchu","sushma","divya","muniraju"]
print(name[1:])

# can access list using zero index
items=["bru","sugar","coffee","tea","chicken"]
print(items[0])

#when we use pop in list it will remove last element
items=["bru","sugar","coffee","tea","chicken"]
items.pop(0)
print(items)

#when we need to add element to the list we can use append method
items=["bru","sugar","coffee","tea","chicken"]
items.append("biscuit")
print(items)

#when we need to remov element from tht list we use remove method
items=["bru","sugar","coffee","tea","chicken"]
items.remove("chicken")
print(items)

#we use insert method to insert the element between the element we can use append also but when we use append it stores element in last but in insert we can insert the element where ever we need
items=["bru","sugar","coffee","tea","chicken"]
items.insert(2,"milk")
print(items)

#we use clear function to clear all elements in the list
items.clear()
print(items)

#in this we can change a specific element
items=["bru","sugar","coffee","tea","chicken"]
items[3]="cherry"
print(items)

#slicing lists
l=[100,200,300,400,500,600,700,800,900]
l2=l[1:3]
print(l2)

#list functions
#len
l=[100,200,300,400,500,600,700,800,900]
print(len(l))

#sort function
items=["bru","sugar","coffee","tea","chicken"]
print(sorted(items))

#sum function
l=[100,200,300,400,500,600,700,800,900]
print(sum(l))

#list methods
#indexing element
items=["bru","sugar","coffee","tea","chicken"]
print(items.index("coffee"))

#we can reverse the elements in the list using reverse method
items.reverse()
print(items)

#Lists can contain other lists, allowing you to create nested lists. This can be useful for storing matrix-like data structures.
numbers = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
print(numbers[0][2])

#Create a list of five numbers: 10, 20, 30, 40, 50. Print the first element.
numbers=[10,20,30,40,50]
print(numbers[0])

#Create a list of fruits: apple, mango, banana, orange. Print the third fruit.
fruits = ["apple", "mango", "banana", "orange"]
print(fruits[2])

#Create a list of colors. Print the last element using a negative index.
colours=["red", "blue", "green", "yellow"]
print(colours[-1])

#Given numbers = [10, 20, 30, 40], change 20 to 25 and print the list.
numbers = [10,20,30,40]
numbers [1]=25
print(numbers)

#Given fruits = ['apple', 'mango', 'banana'], replace 'banana' with 'grapes'.
fruits = ['apple', 'mango', 'banana']
fruits[2] = 'grapes'
print(fruits)

#Create a list of three animals. Add 'tiger' at the end using append() and print the list.
animals = ["wolf","lion", "fox"]
animals.append("tiger")
print(animals)

#. Given numbers = [10, 30, 40], insert 20 at index 1.
numbers = [10, 30, 40]
numbers.insert(1,20)
print(numbers)

#Given a = [1, 2] and b = [3, 4], add all elements of b to a using extend().
a=[1,2]
b=[3,4]
a.extend(b)
print(a)

#Given fruits = ['apple', 'mango', 'banana'], remove 'mango' by its value.
fruits = ['apple', 'mango', 'banana']
fruits.remove('mango')
print(fruits)

#Given numbers = [10, 20, 30, 40], remove the element at index 2 using pop().
numbers = [10, 20, 30, 40]
numbers.pop(2)
print(numbers)

#Given numbers = [10, 20, 30, 40, 50, 60], print the first three elements using slicing.
numbers = [10, 20, 30, 40, 50, 60]
print(numbers[:3])


#Given numbers = [10, 20, 30, 40, 50, 60], print the first three elements using slicing.Using the same list, print [30, 40, 50] using slicing.
numbers = [10, 20, 30, 40, 50, 60]
print(numbers[3:6])
print(numbers)

#Print the last three elements using slicing.
numbers = [10, 20, 30, 40, 50, 60]
print(numbers[3:])

#Reverse the list [1, 2, 3, 4, 5] using slicing only.
numbers = [10, 20, 30, 40, 50, 60]
print(numbers[::-1])


#Given numbers = [10, 20, 30, 40, 50], delete the element at index 1 using del.
numbers = [10, 20, 30, 40, 50]
del numbers[1]
print(numbers)

#Given fruits = ['apple', 'mango', 'banana'], remove and print the last element using pop().
fruits = ['apple', 'mango', 'banana']
print(fruits.pop())
print(fruits)

#Given numbers = [1, 2, 3, 4], remove all elements using clear().
numbers = [1, 2, 3, 4]
print(numbers.clear())

#18. Given numbers = [5, 2, 8, 1, 9], use reverse() to reverse the list. Print the result.
numbers = [5, 2, 8, 1, 9]
numbers.reverse()
print(numbers)

#Given numbers = [10, 20, 30, 40, 50], find the number of elements using len().
numbers = [10, 20, 30, 40, 50]
print(len(numbers))

#Given numbers = [5, 2, 8, 1, 9], print the list in ascending order using sorted().
numbers = [5, 2, 8, 1, 9]
print(sorted(numbers))

#sing the same list, print it in descending order using sorted().
numbers = [5, 2, 8, 1, 9]
print(sorted(numbers,reverse=True))

#Given numbers = [10, 20, 30, 40], calculate the total using sum().
numbers = [10, 20, 30, 40]
print(sum(numbers))

#Given fruits = ['apple', 'mango', 'banana', 'mango'], find the index of 'banana' using index().
fruits = ['apple', 'mango', 'banana', 'mango']
print(fruits.index('banana'))

#Given numbers = [2, 5, 2, 8, 2, 9], count how many times 2 occurs using count().
numbers = [2, 5, 2, 8, 2, 9]
print(numbers.count(2))


#Given numbers = [45, 12, 78, 23, 9], find the smallest and largest values using min() and max().
numbers = [45, 12, 78, 23, 9]
print(min(numbers))
print(max(numbers))

#Given numbers = [4, 1, 7, 2], print the sorted list and then print the original list. Observe whether sorted() changes the original list.
numbers = [4, 1, 7, 2]
print(sorted(numbers))
print(numbers)

#Create a nested list containing three students, with each student's name and age. Print the entire list.
students = [
    ["Amulya", 20],
    ["Ravi", 21],
    ["Priya", 19]
]
print(students)

#Using the students list above, print 'Ravi' by accessing the correct indexes.
print(students[1][1])

#Using the students list above, print Priya's age.
print(students[2][1])

#Given matrix = [[1, 2], [3, 4], [5, 6]], print the number 4.
matrix = [[1, 2], [3, 4], [5, 6]]
print(matrix[1][1])

#Given matrix = [[10, 20], [30, 40]], change 20 to 25 and print the nested list.
matrix = [[10, 20], [30, 40]]
matrix[0][1] = 25
print(matrix)

#Create a nested list representing two shopping carts. Each cart should contain three items. Print the first item in the second cart.
carts = [
    ["apple", "banana", "orange"],
    ["milk", "bread", "eggs"]
]
print(carts[1][0])

#Create a list of five numbers. Print its length, sum, smallest number, and largest number.
numbers = [45, 12, 78, 23, 9]
print(len(numbers))
print(sum(numbers))
print(min(numbers))
print(max(numbers))

#Create a list of five fruits. Add one fruit, remove one fruit, and print the final list.
fruits = ['apple', 'mango', 'banana', 'goa', 'grapes']
fruits.append('kiwi')
fruits.remove('goa')
print(fruits)

#Given numbers = [10, 20, 30, 40, 50], print the second and fourth elements, then print the list in reverse using slicing.
numbers = [10, 20, 30, 40, 50]
print(numbers[1], numbers[3])
print(numbers[::-1])

#Given marks = [78, 45, 92, 66, 88], sort the marks in ascending order and print their total.
marks = [78, 45, 92, 66, 88]
print(sorted(marks))
print(sum(marks))