myStr = "1010110100"

isBinary = True

for ch in range(len(myStr)):
    if(myStr[ch] != "0" and myStr[ch] != "1"):
        isBinary=False
        exit

print(isBinary)


print(all([False if myStr[i] != "0" and myStr[i] != "1" else True for i in range(len(myStr))]))

print(all([ch in "01" for ch in myStr]))