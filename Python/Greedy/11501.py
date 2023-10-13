# https://www.acmicpc.net/problem/11501
import sys
input = sys.stdin.readline

t = int(input())


while t:
    n = int(input())
    arr = list(map(int, input().split()))

    # target_max = max(arr)
    # target_idx = arr.index(target_max)

    # if target_idx == 0:
    #     print(0)
    # else:
    #     ans = 0
    #     for i in range(len(arr)):
    #         if i < target_idx:
    #             ans += (target_max - arr[i])

    #         # 최대값 갱신
    #         if i == target_idx and target_idx != len(arr) - 1:
    #             target_max = max(arr[target_idx + 1:])
    #             target_idx = arr.index(
    #                 target_max, target_idx + 1, len(arr))

    #     print(ans)

    ans = 0

    target_max = arr[-1]

    for i in range(n-2, -1, -1):
        if arr[i] > target_max:
            target_max = arr[i]
        else:
            ans += (target_max - arr[i])

    print(ans)

    t -= 1
