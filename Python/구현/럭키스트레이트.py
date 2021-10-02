# 백준 18406 https://www.acmicpc.net/problem/18406
# 단순하게 문자열 길이 2로 나눠서 left 부분과 right 부분 합 비교

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
