import operator
from collections import Counter

myList = [1, 3, 2, 6, 3, 2, 8, 2, 9, 2, 7, 3]

# count func
print("Using count func",myList.count(2))

# Using a loop
count = 0
for val in myList:
    if val == 2:
        count += 1
    
print("Using Loop",count)

# The countOf() function is equivalent to using the count() method of a list, but it comes from the operator module.
print("Using CountOf operator",operator.countOf(myList,2))


# The Counter class from the collections module can count occurrences for all elements and returns the results as a dictionary.
res = Counter(myList)
print("Using Counter which returns in dictonary",res[2])