# https://www.acmicpc.net/problem/2885
import sys
input = sys.stdin.readline

k = int(input())


# k 보다 큰 2의 제곱 수 중 최소
choco_size = 1
while choco_size < k:
    choco_size *= 2

cnt = 0
tmp_size = choco_size
while True:
    if k % tmp_size == 0:
        break

    else:
        tmp_size = tmp_size // 2
        cnt += 1

print(choco_size, cnt)
