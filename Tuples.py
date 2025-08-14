myTuple = (1,2,3,"asd")
print(myTuple, type(myTuple))

# List, Tuples have indexing, dict and sets do not have indexing


print(myTuple[1:]) 

for values in myTuple:
    print(values)


# Same as Lists but Lists are mutable and tuples are immutable
# myTuple[2] = "as"  --> Gives errror
# Workaround is convert the Tuple into List and change the values then convert back to tuple

temp = list(myTuple) 
temp[0] = 5
myTuple = tuple(temp)

print(myTuple)

myTuple2 = (7,8)
myTuple += myTuple2

print(myTuple)

# destructure the tuples

(first, second, *third) = myTuple
print(first,second,third, type(first) ,type(myTuple))