# https://www.acmicpc.net/problem/11652
import sys
input = sys.stdin.readline

"""
5
1
2
1
2
1

1
"""

n = int(input())

# key : 숫자, value : 횟수
dict = {}

for _ in range(n):
    num = int(input())

    if num in dict:
        dict[num] = dict[num] + 1
    else:
        dict[num] = 1

arr = []
for key in dict:
    # 숫자, 나온횟수 arr에 append
    arr.append([key, dict[key]])

arr.sort(key = lambda x : (x[1], -x[0]), reverse = True)
print(arr[0][0])
