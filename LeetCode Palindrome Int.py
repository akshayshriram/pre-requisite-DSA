n = 11
originalNumber = n
reversedNumber = 0

while n > 0:
    digit = n % 10
    reversedNumber = reversedNumber * 10 + digit
    n = n // 10
print("originalNumber",originalNumber)
print(reversedNumber)
print(True if reversedNumber == originalNumber else False)
    