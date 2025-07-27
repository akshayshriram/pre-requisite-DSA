import math
from functools import reduce
from operator import mul

myList = [1,2,3,4,5]

total = 1
for val in myList:
    total *= val

print("Using Loop",total)

print("Using Math Prod",math.prod(myList))

# Using reduce() and mul()

# We can use reduce() function from the functools module, which can apply a function to an iterable in a cumulative way. We can use the operator.mul() function to multiply the elements together.

print("Using Reduce() and mul()",reduce(mul, myList))