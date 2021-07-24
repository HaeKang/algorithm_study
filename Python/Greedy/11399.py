
n = int(input())
arr = list(map(int, input().split()))

arr.sort()

tmp_sum = 0
result = 0

for i in range(n):
    result = result + tmp_sum + arr[i]
    tmp_sum += arr[i]

print(result)
