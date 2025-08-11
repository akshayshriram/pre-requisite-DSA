mystr = "Banana"
print(mystr)

print(mystr.count("a"))
print(mystr.count("a", 0,4))

mystr2 = "Banana is a my fav fruit."
print(mystr2.split("a"))

# It checks from the first and last string and 
# helps to remove the blank spaces at the start and end

mystr3 = "nabanana is banana"
print(mystr3.strip("na"))
mystr4 = "    bnaa asd anasdad   "
print(mystr4.strip())