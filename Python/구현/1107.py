# https://www.acmicpc.net/problem/1107
"""
5457
3
6 7 8

6

500000
8
0 2 3 4 6 7 8 9

11117
"""

import sys
input = sys.stdin.readline

n = int(input())
m = int(input())

# 리모컨 버튼 key : 숫자, value : True, False (사용 가능, 불가능)
remote_btn = {}
for i in range(0, 10):
    remote_btn[str(i)] = True

arr = list(map(int, input().split()))
for num in arr:
    remote_btn[str(num)] = False


# 맨 처음 값은 초기값 100에서 +, - 만 사용하여 이동한 횟수
ans = abs(n - 100)
if m != 100:
    for num in range(1000001):
        num_str = str(num)
        
        check_flag = True

        # 고장난 버튼이 있는지 check
        for num2 in num_str:
            if remote_btn[num2] == False:
                check_flag = False
                break
        
        # 고장난 버튼이 없으면
        if check_flag:
            # min(기존 ans, num 숫자 누름 + n까지의 거리)
            ans = min(ans, len(num_str) + abs(n - num))

print(ans)
    
