def permute(s, choosen=""):
    if len(s) == 0:
        print(choosen)
        return

    for i in range (len(s)):
        ch = s[i]
        rest = s[:i] + s[i+1:] 
        print("ch",ch)
        print("rest",rest)
        print("choosen",choosen)
        permute(rest, choosen + ch)

myStr = "LOP"
permute(myStr)

