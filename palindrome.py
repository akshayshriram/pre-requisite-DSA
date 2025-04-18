string  = 'mOom'
revString = ''

lowerstring = string.lower();

for i in lowerstring:
    revString = i + revString
print("Reversed String:", revString)

if(lowerstring == revString) :
    print(string,"is a palindrome")
else:
    print(string,"is not a palindrome")
