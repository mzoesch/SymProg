import math
from copy import deepcopy

print(type('str'))
# String are immutable
# str[0] = 'a'  # Error

str = 'Hello World'
str = 'T' + str[1:]
print(str)

print('{} say "{}!"'.format('John', 'Hello World'))  # or
print('{0} say "{1}!"'.format('John', 'Hello World'))  # or
print('{name} say "{quote}!"'.format(name='John', quote='Hello World'))
# fstring
str = 'John'
print(f'{str} say "Hello World!"')

print(f'PI is approx: {math.pi:.3f}')


# Just some list stuff
myList = [3, 2, 6, 1, 8]
myList.reverse()
x = len(myList)
myList.sort()
myList.insert(2, 5)
myList.sort(reverse=True)
myList.append(3)
x = myList.count(3)
myList.remove(3)
x = myList.pop()
y = myList.pop()
z = 4 in myList
myList = myList + [7, 8, 9]
del myList[:]


# Creates copy of list objects
myList = ['a', 'b', 'c', 'd']
myList[0:3]
# ['a', 'b', 'c']
myList[2:3]
# ['c']
myList = ['a', 'b', 'c', 'd']
myList[2:4]
# ['c', 'd']
myList[1:]
# ['b', 'c', 'd']
myList[:3]
# ['a', 'b', 'c']
myList[:]
# ['a', 'b', 'c', 'd']


# Shallow copy
x = [1, 2, 3]
z = x
y = x[:]
print(y)
# is keyword : Checks for memory address
print(z is x)  # True
print(y is x)  # Fakse
# 03_recap_II for more on this
# Always check references

# Deep copy
y = deepcopy(x)
print(y)
# Can be quite slow and expensive in memory

# == vs is !!
# == checks for value
# is checks for memory address

# Comprehension
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
subset = [n for n in nums if n % 2 == 0]
print(subset)

# import sys
# print(sys.argv)
# better
# import argparse
# parser = argparse.ArgumentParser()
# parser.parse_args()
# parser.add_argument('name', help='Your name')
# args = parser.parse_args()
# print(args.name)
