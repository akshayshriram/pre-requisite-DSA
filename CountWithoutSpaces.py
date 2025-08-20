myStr ="This is String" 

print(len(myStr))

print("Len Without Spaces:", len(myStr.replace(" ","")))

print("Using list comprehension", len([ch for ch in myStr if ch != " "]))

print("Using filter", len(list(filter(lambda ch: ch != " ", myStr ))))