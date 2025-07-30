myList = [-10, 15, 0, 20, -5, 30, -2]

postiveNumbers = []
negativeNumbers = []

postiveCount = 0
negativeCount = 0

for val in myList:
    if val > 0:
        postiveNumbers.append(val)
        postiveCount += 1
    elif val < 0:
        negativeNumbers.append(val)
        negativeCount += 1

print("Using loop PostiveNumber", postiveNumbers)
print("Using loop negativeNumbers", negativeNumbers)

# Using list comprehension
print("Using list compreshension positive:",[val for val in myList if val > 0])
print("Using list compreshension negative:",[val for val in myList if val < 0])

# Using filter() and lambda func

print("Using fitler() positive",list(filter(lambda val: val > 0, myList)))
print("Using fitler() negative",list(filter(lambda val: val < 0, myList)))

# Count positive and negative numbers using loop in the above loop

print("Positive Count", postiveCount)
print("Negative Count", negativeCount)

# Using List comperhension

print("Using List comprenhension positive count",len([val for val in myList if val > 0]))
print("Using List comprenhension negative count",len([val for val in myList if val < 0]))

# Using Filter()

print("Using Fitler positive count",len(list(filter(lambda val : val > 0, myList))))
print("Using Fitler negative count",len(list(filter(lambda val : val < 0, myList))))

