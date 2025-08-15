myStr = "amaama"
# myStr = "amadama"
isPalindrom = True
isSymmetric = True
for i in range(len(myStr)//2):

    if myStr[i] != myStr[ - i - 1]:
        isPalindrom = False
    if myStr[i] != myStr[(len(myStr)//2) + i]:
        print(myStr[i])
        print(myStr[i])
        isSymmetric = False

if isPalindrom:
    print("String is Palindrome")
else:
    print("String is not palindrome")
if isSymmetric:
    print("String is Symmetric")
else:
    print("String is not Symmetric")