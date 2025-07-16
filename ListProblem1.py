# Count Strings with Same Start and End

# Write a Python program to count the number of strings from a given list of strings. The string length is 2 or more and the first and last characters are the same.
# Sample List : ['abc', 'xyz', 'aba', '1221']
# Expected Result : 2

myList = ['abc','aba','121', '1331', 'wdsr','3344']
count = 0
for val in myList:
    print(val[0], val[-1])
    if val[0] == val[-1]:
        count += 1

print("count: ", count)