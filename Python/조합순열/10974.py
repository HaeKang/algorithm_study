# https://www.acmicpc.net/problem/10974

import sys
from itertools import permutations
input = sys.stdin.readline


n = int(input())

arr = [i for i in range(1, n+1)]

# 라이브러리 사용
perms = list(permutations(arr, n))
for perm in perms:
    for p in perm:
        print(p, end = " ")
    print("")


# 재귀를 통한 구현

checked = [0 for _ in range(1, n+1)]
def make_perm(ans, checked):
    if len(ans) == n:
        for a in ans:
            print(a, end = " ")
        print("")

    for i in range(len(arr)):
        if checked[i] == 0:
            checked[i] = 1
            ans.append(arr[i])
            make_perm(ans, checked)
            checked[i] = 0
            ans.pop()

make_perm([], checked)
