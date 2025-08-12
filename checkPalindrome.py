inpstr = input()
mystr = inpstr.lower()
print(mystr)

isPalindrome = True

for i in range(len(mystr) // 2):
    if mystr[i] != mystr[len(mystr) - i -1]:
        isPalindrome = False

if isPalindrome:
    print("Given string is palindrome")
else:
    print("Given String is not palindrome")