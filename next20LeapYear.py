from datetime import datetime

currentYear = datetime.now().year

count = 20

while count > 0:
    if(currentYear % 4) == 0:
        print(currentYear)
        count -= 1
    currentYear += 1