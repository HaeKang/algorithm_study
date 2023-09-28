# https://www.acmicpc.net/problem/5568
import sys
input = sys.stdin.readline

n = int(input())
k = int(input())

arr = [int(input()) for _ in range(n)]

perm_arr = []
checked = [0] * (n)


def make_perm(tmp_arr):
    global k

    if len(tmp_arr) == k:
        perm_arr.append(''.join(map(str, tmp_arr)))
        return

    for i in range(0, len(arr)):
        if checked[i] == 0:
            checked[i] = 1
            make_perm(tmp_arr + [arr[i]])
            checked[i] = 0


make_perm([])
perm_arr = set(perm_arr)
print(len(perm_arr))
