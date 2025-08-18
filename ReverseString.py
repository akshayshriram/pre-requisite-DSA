myStr = "This_is_String"
revStr = ""
for i in range(len(myStr) - 1, -1, -1):
    revStr += myStr[i]

print("Reverse String:", revStr)

# using Slicing

print("Reverse String using slicing:", myStr[::-1])

