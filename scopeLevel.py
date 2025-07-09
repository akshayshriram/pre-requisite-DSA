myVar = 10

def myFunc():
    myVar = 7 #Overrides the value
    print("Func Var:",myVar)

print("Global Var:", myVar)
myFunc()

#Override the global var in func

myNewVar = 20
def myGlobalFunc():
    global myNewVar
    myNewVar +=1
    print("Func in Var:", myNewVar)

print("Global New Var:",myNewVar)
myGlobalFunc()

