# https://www.acmicpc.net/problem/2212

import sys
input = sys.stdin.readline

n = int(input())
k = int(input())
arr = list(map(int, input().split()))

if k >= n:
    print(0)
else:
    arr.sort()

    arr_dist = []
    for i in range(0, n-1):
        arr_dist.append(arr[i+1] - arr[i])
    arr_dist.sort()

    # 센서 간 거리차가 가장 큰 값을 k-1개 뺸 값
    ans = sum(arr_dist[:n-k])
    print(ans)
