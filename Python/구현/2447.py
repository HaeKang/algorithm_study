# https://www.acmicpc.net/problem/2447
import sys
input = sys.stdin.readline

n = int(input())


def draw_star(n):
    if n == 1:
        return ['*']

    stars = draw_star(n // 3)

    ans = []
    for star in stars:
        ans.append(star * 3)

    for star in stars:
        ans.append(star + ' ' * (n//3) + star)

    for star in stars:
        ans.append(star * 3)

    return ans


ans = draw_star(n)
print('\n'.join(ans))
