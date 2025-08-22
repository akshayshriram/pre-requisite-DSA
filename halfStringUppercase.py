myStr = "Python is powerful language"

mid = len(myStr)//2

myUpperStr = myStr[:mid] + myStr[mid:].upper()

print(myUpperStr)

# using loop
myUpperV2 = ""
for ch in range(len(myStr)):
    if ch >= mid:
        myUpperV2 += myStr[ch].upper()
    else:
        myUpperV2 += myStr[ch]


print(myUpperV2)

myUpperV3 = ""
res = "".join([myStr[i].upper() if i >= mid else myStr[i] for i in range(len(myStr))])
print(res)