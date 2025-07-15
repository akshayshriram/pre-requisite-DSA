myList = input().split()

print(myList)

statement = ''

for val in myList:
    statement += ' ' + val

# Remove trailing spaces ' ' + val it adds space at the start
result = statement.strip()
print(result)

# Build in func

print(' '.join(myList))