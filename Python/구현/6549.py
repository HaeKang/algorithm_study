# https://www.acmicpc.net/problem/6549
import sys
input = sys.stdin.readline

# https://codable.tistory.com/1 풀이 참고


while True:
    heights = list(map(int, input().split()))

    # 0이 들어오면 종료
    if heights[0] == 0:
        break

    stack = []
    n = heights[0]
    max_area = 0

    for i in range(1, n+1):

        # 현재 그래프의 x, y 값
        now_x = i
        now_y = heights[i]

        # 1. 스택이 비어있는 경우 append
        if len(stack) == 0:
            stack.append((now_x, now_y))

        else:

            # 2. 스택의 최상단 y값보다 현재 y값이 클 경우 append
            if stack[-1][1] <= now_y:
                stack.append((now_x, now_y))

            else:

                # 3. 스택에 값이 있고, 최상단값이 현재 y보다 큰 경우에 대해 진행
                while len(stack) > 0 and stack[-1][1] > now_y:

                    # 3-1. 스택 pop
                    stack_top = stack.pop()

                    # 3-2. 스택의 값이 이제 없는 경우, 넓이를 구할 사각형의 가로는 now_x - 1
                    if len(stack) == 0:
                        width = now_x - 1

                    # 3-3. 스택에 값이 남아있는 경우, 넓이를 구한 사각형의 가로는 now_x - (스택의 최상단 x좌표) - 1
                    else:
                        width = now_x - stack[-1][0] - 1

                    # 3-4. 답 갱신
                    max_area = max(max_area, stack_top[1] * width)

                # 4. 현재 값 스택에 append
                stack.append((now_x, now_y))

    # 5. 스택에 값이 남아있는 경우
    while stack:

        # 5-1. 스택 pop
        stack_top = stack.pop()

        # 5-2. 스택의 값이 이제 없는 경우, 넓이를 구할 사각형의 가로는 n
        if len(stack) == 0:
            width = n

        # 5-3. 스택에 값이 남아있는 경우, 넓이를 구할 사각형의 가로는 n - (스택의 최상단의 x값)
        else:
            width = (n - stack[-1][0])

        # 5-4. 답 갱신
        max_area = max(max_area, stack_top[1] * width)

    print(max_area)
