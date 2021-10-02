# 백준 18406 https://www.acmicpc.net/problem/18406
# 단순하게 문자열 길이 2로 나눠서 left 부분과 right 부분 합 비교
# 파이썬 풀때 str이라는 변수명 쓰지 않도록 해야함 ~> 나중에 str.find 이런식의 함수 쓸때 문제발생

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
