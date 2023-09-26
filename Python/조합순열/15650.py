# https://www.acmicpc.net/problem/15650

import sys
from itertools import combinations
input = sys.stdin.readline

n, m = map(int, input().split())

arr = [i for i in range(1, n+1)]

# 구현
combi_arr = []
def make_combi(result):
    global m

    if len(result) == m:
        combi_arr.append(result)
        return
    
    start = 0
    if len(result) != 0:
        start = arr.index(result[-1]) + 1
    
    for i in range(start, len(arr)):
        make_combi(result + [arr[i]])

make_combi([])

# 라이브러리 사용
combi_arr = list(combinations(arr, m))

for combi in combi_arr:
    for c in combi:
        print(c, end = " ")
    print("")


