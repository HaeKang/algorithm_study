# https://www.acmicpc.net/problem/10819
"""
6
20 1 15 8 4 10
62
"""
import sys
from itertools import permutations
input = sys.stdin.readline

n = int(input())

arr = list(map(int, input().split()))

checked = [0] * len(arr)

# 라이브러리 ㄴㄴ
perm_arr = []

def make_perm(cnt, ans):
    if cnt == n:
        perm_arr.append(ans)
        return
    
    for i in range(n):
        if checked[i] == 0:
            checked[i] = 1
            make_perm(cnt + 1, ans + [arr[i]])
            checked[i] = 0

make_perm(0, [])

# 라이브러리 사용
perm_arr = permutations(arr, n)

ans = 0
# |A[0] - A[1]| + |A[1] - A[2]| + ... + |A[N-2] - A[N-1]|
for perm in perm_arr:
    tmp_ans = 0
    for i in range(1, n):
        tmp_ans += abs(perm[i-1] - perm[i])
    
    ans = max(ans, tmp_ans)

print(ans)
