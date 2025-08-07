a = ["name", "age", "city"]  
b = [["Alice", 25, "New York"], ["Bob", 30, "Los Angeles"], ["Charlie", 22, "Chicago"]] 

result = [dict(zip(a, values)) for values in b]
print(result)

# result1 = [{b[i]: value[i] for i in range(len(b))} for value in a]
result1 = list(map(lambda x: dict(zip(a, x)), b))

print(result1)