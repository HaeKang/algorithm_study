import heapq as hq
import sys

n = int(input())
arr = []

for i in range(n):
    x = int(sys.stdin.readline())
    if x == 0:
        if arr:
            print(hq.heappop(arr)[1])
        else:
            print("0")
    else:
      # heap에 tuple 넣음, heap은 첫번째 값을 기준으로 정렬한다
        hq.heappush(arr, (abs(x), x))
