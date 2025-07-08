def exponentFunc(base, exponent):
    if exponent == 0:
        return 1
    return base * exponentFunc(base, exponent - 1)

finalResult = exponentFunc(2,3)
print(finalResult)