import random

start = [1,2,3,4,5]


squares = [item**2 for item in range(1,6)]

print(start, squares)

print(squares[:-3])

odds = [oddNumber for oddNumber in squares if oddNumber%2 != 0]


print(odds)


setA = ['a','b','c','d','e']
setB = ['c','d','e']

intersectionAB = [element for element in setA if element in setB]

print(intersectionAB)

# dict comprehension

old_dict = {'kevin':'sad', 'money':'gone', 'self':'silence'}

new_dict = {oldKey:oldVal for (oldKey,oldVal)in old_dict.items()}

print(new_dict)


# enumerating all reals 
numDict = {str(number):random.random() for number in range(0,5) if number > 1}

print(numDict)