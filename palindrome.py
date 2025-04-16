string  = 'mom'
revString = ''

for i in string:
    revString = i + revString
print("Reversed String:", revString)

if(string == revString) :
    print(string,"is a palindrome")
else:
    print(string,"is not a palindrome")
