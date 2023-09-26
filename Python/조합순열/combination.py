import sys
from itertools import combinations
input = sys.stdin.readline

n, m = map(int, input().split())

arr = [i for i in range(1, n+1)]

# 재귀 통한 구현
combi_arr = []
def make_combi(result, cnt, target_cnt):
    if target_cnt== cnt:
        combi_arr.append(result)
        return
    
    start = 0
    if len(result) != 0:
        start = arr.index(result[-1]) + 1
    
    for i in range(start, len(arr)):
        make_combi(result + [arr[i]], cnt + 1, target_cnt)
        
make_combi([], 0, m)

# 라이브러리
combi_arr = list(combinations(arr, m))
print(combi_arr)
