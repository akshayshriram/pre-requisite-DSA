mystr = "aDDeS"

ans = ""

for i in range(len(mystr)):
    if (ord(mystr[i]) > 90):
        ans += mystr[i]
    else:
        ans += chr(ord(mystr[i]) + (ord('a') - ord('A')))


print(ans)