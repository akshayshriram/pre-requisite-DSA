myStr = "Python is a great Coding Language"
words = myStr.split()
print("Using List Comprehension:", " ".join(list([item for item in words if len(item)%2 == 0])))

print("Using Filter", " ".join(filter(lambda wd: len(wd)%2 == 0, words )))

# Using for loop
newStr = ""

for wd in words:
    if len(wd)%2 == 0:
        newStr += wd + " "

print("Using Loop", newStr.strip(" "))