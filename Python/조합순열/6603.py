# https://www.acmicpc.net/problem/6603

import sys
from itertools import combinations
input = sys.stdin.readline

# 구현
def make_combi(result):
    if len(result) == 6:
        combi_arr.append(result)
        return
    
    start = 0
    if len(result) != 0:
        start = arr.index(result[-1]) + 1
    
    for i in range(start, len(arr)):
        make_combi(result + [arr[i]])

arr = []
combi_arr = []

while True:
    arr = list(map(int, input().split()))

    k = int(arr[0])

    if k == 0:
        break

    arr = arr[1:]

    # 구현
    combi_arr.clear()
    make_combi([])

    # 라이브러리
    combi_arr = list(combinations(arr, 6))
    
    for combi in combi_arr:
        for c in combi:
            print(c, end = " ")
        print("")
    print("")
