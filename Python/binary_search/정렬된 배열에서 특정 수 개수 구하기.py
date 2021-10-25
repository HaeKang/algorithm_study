def find_first(arr, target, start, end):
    while start <= end:
        mid = (start+end) // 2

        if (mid == 0 or arr[mid-1] < target) and arr[mid] == target:
            return mid
        elif arr[mid] >= target:
            end = mid - 1
        else:
            start = mid + 1

    return None


def find_last(arr, target, start, end):
    while start <= end:
        mid = (start+end) // 2

        if (mid == n-1 or target < arr[mid+1]) and arr[mid] == target:
            return mid
        elif arr[mid] > target:
            end = mid - 1
        else:
            start = mid + 1

    return None


n, x = map(int, input().split())

arr = list(map(int, input().split()))

arr.sort()

idx_first = find_first(arr, x, 0, n-1)

if idx_first == None:
    print(-1)
    exit()

idx_last = find_last(arr, x, 0, n-1)

print(idx_last - idx_first + 1)
