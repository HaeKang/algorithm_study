n, x = map(int, input().split())
arr = list(map(int, input().split()))

ans = 0
ans_cnt = 1

sum = 0


for i in range(x):
    sum += arr[i]

ans = sum

for i in range(x, n, 1):
    sum += arr[i] - arr[i-x]
    if sum == ans:
        ans_cnt += 1
    elif sum > ans:
        ans = sum
        ans_cnt = 1


if ans == 0:
    print("SAD")
else:
    print(ans)
    print(ans_cnt)
