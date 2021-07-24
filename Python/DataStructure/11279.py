import heapq as hq
import sys

# Max Heap

n = int(input())
arr = []

for i in range(n):
    x = int(sys.stdin.readline())
    if x == 0:
        if arr:
            print(-1 * hq.heappop(arr))
        else:
            print("0")
    else:
        hq.heappush(arr, x * -1)
