n = int(input())
m = int(input())

# matrix = []
# for i in range(n):
#     tempList = input().split()
#     for j in range(m):
#         tempList[j] = int(tempList[j])
#     matrix.append(tempList)


# print(matrix)


# using list comprehension
matrix2 = []
for i in range(n):
    tempList = [int(item) for item in input().split()]
    matrix2.append(tempList)

print(matrix2)