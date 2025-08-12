mystr = input() #"101100"
mid = len(mystr) // 2  # integer division"

result = list(map(lambda val: val == "0" or val == "1", mystr))

if len(mystr)%2 != 0:
    print("Equal split is not possible")
# elif for val in mystr:
elif not all(result):
    print("Only Binary Inputs are allowed")

else:
    part1 = mystr[:mid]    # first half
    part2 = mystr[mid:]    # second half
    print(part1)  # "101"
    print(part2)  # "100"