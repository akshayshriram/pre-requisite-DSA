# Given a string s consisting of lowercase English letters, return the first letter to appear twice.

# Note:

# A letter a appears twice before another letter b if the second occurrence of a is before the second occurrence of b.
# s will contain at least one letter that appears twice.

# Input: s = "abccbaacz"
# Output: "c"

s = "nwcn"
# ans = ''
# for i in range(len(s) - 1):
#     if s[i] == s[i+1]:
#         ans = s[i]
#         break
# print(ans)
    
def repeatedCharacter(s):
    seen = set()
    for ch in s:
        if ch in seen:
            return ch
        seen.add(ch)
        print(seen)

ans = repeatedCharacter(s)
print(ans)
