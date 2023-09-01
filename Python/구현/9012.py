# https://www.acmicpc.net/problem/9012

import sys
input = sys.stdin.readline

t = int(input())

while t:
    target = str(input())

    open_stack = []

    flag = True

    for data in target:
        if data == "(":
            open_stack.append("(")

        elif data == ")":
            if open_stack:
                open_stack.pop()
            else:
                flag = False
                break

    if len(open_stack) > 0:
        flag = False

    if flag:
        print("YES")
    else:
        print("NO")

    t -= 1
