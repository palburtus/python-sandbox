mylist = []
mylist.append(11)
mylist.append(222)
mylist.append(34235)

print(mylist[0])
print(mylist[1])
print(mylist[2])

for x in mylist:
    print(x)

mylist = [7, 77, 14, 8]

for x in mylist:
    print(x)

print("Colors:")
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'pink', 'purple', 'blue']
print("Times in list", colors.count('blue'))
print("Zero when not in list", colors.count('indigo'))
print("Index of yellow", colors.index('yellow'))
print("Since the first blue's index is 4 the index of the second blue is", colors.index('blue', 5))
print("unsorted", colors)
colors.sort()
print("sorted", colors)
colors.reverse()
print("reversed ", colors)
colors.pop()
print("after pop ", colors)


stack = [1,2,3,4,5]
print(stack)
stack.append(6)
print(stack)
stack.pop()
stack.pop()
print(stack)

from collections import deque
queue = deque([6,7,8,9,10])
print(queue)
queue.append(11)
print(queue)
queue.popleft()
queue.popleft()
print(queue)

squared = []
for x in range(5):
    squared.append(x**2)

print(squared)

lambdaSqares = list(map(lambda  x: x**2 + 100, range(10)))
print(lambdaSqares)

betterSquares = [x**2 for x in range(20)]

print(betterSquares)

forList = [(x,y) for x in [1,2,3] for y in [1,4,6] if x != y and x != 2 and y != 4]
print(forList)

vec = [1,2,6,7,8,9,10]
twos = [x for x in vec if x/2 == 1]
print(twos)

from math import pi

pie = [str(round(pi,i)) for i in range(1,6)]
print(pie)

threeFour = [
    [1,2,3],
    [4,5,6,7],
    [8,9,10,11]
]

outThreeFour = [[row[i] for row in threeFour] for i in range(3)]
print(outThreeFour)

builtInThreeFour = list(zip(*threeFour))
print(builtInThreeFour)

print(vec)
del vec[2]
print(vec)
del vec[1:3]
print(vec)
del vec[:]
print(vec)

del vec
"""
print(vec)
 would cause an error is not defined because we deleted it  
 """
 
 