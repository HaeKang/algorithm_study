def binary_search(arr, start, end):
    while start <= end:
        mid = (start + end) // 2

        if arr[mid] == mid:
            return mid
        elif arr[mid] > mid:
            end = mid - 1
        else:
            start = mid + 1
    return None


n = int(input())
arr = list(map(int, input().split()))
arr.sort()


idx = binary_search(arr, 0, n-1)

if idx != None:
    print(idx)
else:
    print(-1)
