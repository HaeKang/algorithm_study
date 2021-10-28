n, c = map(int, input().split())
arr = []

for _ in range(n):
    arr.append(int(input()))

arr.sort()

# 공유기 거리 최소값
start = 1

# 공유기 거리 최대값
end = arr[n-1] - arr[0]
ans = 0

while start <= end:
    mid = (start + end) // 2    # 공유기 간격
    pre = arr[0]    # 공유기 설치 위치
    cnt = 1  # 공유기 설치 개수

    for i in range(1, n):
        if arr[i] >= pre + mid:
            pre = arr[i]
            cnt += 1

    if cnt >= c:
        start = mid + 1
        ans = mid
    else:
        end = mid - 1

print(ans)
