myStr = "This is String"

# using Stack
list = myStr.split()


print(list)
revStr = ""
for val in reversed(list):
    revStr += val + " "

revStr.rstrip()
print(revStr)

print(" ".join(myStr.split()[::-1]))