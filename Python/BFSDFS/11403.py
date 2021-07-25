
n = int(input())
arr = []

for i in range(n):
    arr.append(list(map(int, input().split())))


check = [0 for i in range(n)]


def dfs(start, end):
    for i in range(n):
        if check[i] == 0 and arr[start][i] == 1:
            check[i] = 1
            dfs(i, end)


for i in range(n):
    for j in range(n):
        dfs(i, j)

        if check[j] == 1:
            print("1", end=' ')
        else:
            print("0", end=' ')

        check = [0 for i in range(n)]
    print()
