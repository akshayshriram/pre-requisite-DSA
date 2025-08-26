s = ["Lion", "Li", "Tiger", "Tig"]
a = "Lion"

for string in s:
    if string.startswith(a) or a.startswith(string):
        print(string)


