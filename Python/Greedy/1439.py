s = input()
ans = 0

zero = 0
one = 0

for i in range(1, len(s)):
    if s[i-1] != s[i]:
        if s[i-1] == '0':
            zero += 1
        else:
            one += 1

if s[len(s) - 1] == '0':
    zero += 1
else:
    one += 1


print(min(zero, one))
