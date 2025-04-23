import random
secretNumber = random.randint(1, 100)
number = 1

def guessInputFunc():
    return int(input("Guess a Secret Number : "))


userInput = guessInputFunc()
count = 1
while userInput != secretNumber:
    count += 1
    if(userInput > secretNumber):
        print("Entered guess number is greater than the secret number")
        userInput = guessInputFunc()
        continue
    elif(userInput < secretNumber):
        print("Entered guess number is smaller than the secret number")
        userInput = guessInputFunc()
        continue
print("secretNumber -", secretNumber)
print("count -", count)

    