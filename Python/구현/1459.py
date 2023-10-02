# https://www.acmicpc.net/problem/1459
import sys
input = sys.stdin.readline

x, y, w, s = map(int, input().split())


# 1번 방법
ans = (x + y) * w

# 1번 방법이 대각선 가중치보다 적을때
if ans < s:
    print(ans)

else:
    # 2번 방법

    # 짝수인 경우
    if (x+y) % 2 == 0:
        ans = min(ans, max(x, y) * s)

    else:
        ans = min(ans, (max(x, y) - 1) * s + w)

    # 대각선 + 평행이동
    ans = min(ans, (min(x, y) * s) + (max(x, y) - min(x, y)) * w)

    print(ans)
