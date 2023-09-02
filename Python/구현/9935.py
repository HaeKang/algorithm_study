# https://www.acmicpc.net/problem/9935

import sys
input = sys.stdin.readline

target_str = input().strip()
explosion_str = input().strip()

stack = []

for s in target_str:
    stack.append(s)

    check_str = stack[-len(explosion_str):]
    check_str = ''.join(check_str)
    if check_str == explosion_str:
        for _ in range(len(explosion_str)):
            stack.pop()

if len(stack) == 0:
    print("FRULA")
else:
    print(''.join(stack))
