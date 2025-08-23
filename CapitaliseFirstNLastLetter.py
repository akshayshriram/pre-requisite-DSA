myStr= "this is string"

myList = myStr.split()

myV2Str = ""
for wd in myList:
    myV2Str += wd[0].upper() + wd[1:-1]  + wd[-1].upper() +" "

print(myV2Str.strip(" "))