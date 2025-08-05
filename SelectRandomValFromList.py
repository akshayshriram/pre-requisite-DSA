import random
import secrets

a = [1, 4, 5, 2, 7]

print("using random", random.choice(a))

# Using random.randint()
# random.randint() generate a random index within the range of the list’s length, then access the element at that index. This approach gives you more control over the index and allows for indexing-based operations alongside random selection.
indx =  random.randint(0,len(a)-1)
print("Using random Int",a[indx])

# using secrets
print("Using secrets", secrets.choice(a))

# using random sample
print("Using random sample", random.sample(a,1)[0])

