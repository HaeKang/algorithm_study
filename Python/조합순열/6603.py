# https://www.acmicpc.net/problem/6603
import sys
from itertools import combinations
input = sys.stdin.readline

total_result = []


# def make_combi(result, arr):
#     if len(result) == 6:
#         total_result.append(result)
#         return

#     start = 0
#     if len(result) != 0:
#         start = arr.index(result[-1]) + 1

#     for i in range(start, len(arr)):
#         make_combi(result + [arr[i]], arr)


while True:
    arr = list(map(int, input().split()))
    if arr[0] == 0:
        break

    total_result.clear()
    total_result = list(combinations(arr[1:], 6))

    # make_combi([], arr[1:])

    total_result.sort()

    for total_r in total_result:
        for r in total_r:
            print(r, end=" ")
        print("")
    print("")
