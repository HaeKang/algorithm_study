# https://www.acmicpc.net/problem/14891
import sys
from collections import deque
input = sys.stdin.readline


arr = [list(input().rstrip()) for _ in range(4)]


def turn(target, dir):
    return_lst = []

    # 시계방향
    if dir == 1:
        return_lst.append(target[-1])

        for i in range(len(target) - 1):
            return_lst.append(target[i])

    # 반시계방향
    else:
        for i in range(1, len(target)):
            return_lst.append(target[i])
        return_lst.append(target[0])

    return return_lst

# 회전시킬 target의 오른쪽 톱니바퀴 회전


def turn_right(num, dir):
    if num > 3:
        return

    if arr[num - 1][2] != arr[num][6]:
        turn_right(num + 1, dir * -1)
        arr[num] = turn(arr[num], dir)

# 회전시킬 target의 왼쪽 톱니바퀴 회전


def turn_left(num, dir):
    if num < 0:
        return

    if arr[num + 1][6] != arr[num][2]:
        turn_left(num - 1, dir * -1)
        arr[num] = turn(arr[num], dir)


for _ in range(int(input())):
    num, dir = map(int, input().split())

    num -= 1

    turn_right(num + 1, dir * -1)
    turn_left(num - 1, dir * -1)

    arr[num] = turn(arr[num], dir)

ans = 0
for i in range(4):
    if arr[i][0] == '1':
        ans += 2 ** i

print(ans)
