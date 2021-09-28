str = input()

left, right = 0, 0

for i in range(len(str) // 2):
    left += int(str[i])

for j in range(len(str)//2, len(str)):
    right += int(str[j])

if left == right:
    print("LUCKY")
else:
    print("READY")
