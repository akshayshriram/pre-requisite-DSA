list1 = [1,2,4]
list2 = [1,3,4]

mergeList = list(filter(lambda x: x, list1)) + list(filter(lambda x: x ,list2))
mergeList.sort()
print(mergeList)