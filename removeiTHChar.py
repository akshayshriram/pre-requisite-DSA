myStr = "This is String"

myStr = myStr.replace("s", "")

print(myStr)

removeChar = input()

for char in myStr:
    if char == removeChar:
        myStr = myStr.replace(removeChar,"")

print(myStr)


myNewStr = "".join([ch for ch in myStr if ch != 'i'])

print(myNewStr)

myv2Str = "".join(filter(lambda ch: ch != "n", myNewStr))

print(myv2Str)