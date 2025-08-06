n = int(input())

matrix = []

for i in range(n):
    matrix.append([int(item) for item in input().split()])

print(matrix)

trace = []
for i in range(n):
    for j in range(n):
        if i == j:
            trace.append(matrix[i][j])

print(trace)
trace2 = []
# As we tracing n-n --> [i][i=j]
for i in range(n):
    trace2.append(matrix[i][i])
print(trace2)
# using list comprehension
trace3 = [matrix[i][i] for i in range(n)]
print(trace3)
