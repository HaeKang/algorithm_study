# https://www.acmicpc.net/problem/1992
import sys
input = sys.stdin.readline

"""
8
11110000
11110000
00011100
00011100
11110000
11110000
11110011
11110011

((110(0101))(0010)1(0001))
"""

n = int(input())
arr = [list(input().rstrip()) for _ in range(n)]

# (r1, c1) ~ (r2, c2) 범위의 값 체크
def check_range(r1, r2, c1, c2):
    target = arr[r1][c1]    # 최상단 값
    for r in range(r1, r2 + 1):
        for c in range(c1, c2 + 1):
            if target != arr[r][c]:
                return False
    
    return True

def solve(r1, r2, c1, c2, size):
    # print(r1, r2, c1, c2, size)

    # 1. 현재 범위 모두 같은 값인지 체크
    if check_range(r1, r2, c1, c2):
        # 1-1. 모두 같은 값이라면, 해당 값 출력 
        print(arr[r1][c1], end= "")
        return
    
    # 2. 다른 값이면 분할 시작
    else:
        print("(", end = "")

        size = r2 - r1 + 1  # 현재 사각형의 크기
        size = size // 2

        # 왼쪽 위
        solve(r1, r1 + size - 1, c1, c1 + size - 1, size)

        # 오른쪽 위
        solve(r1, r1 + size - 1, c1 + size, c2, size)

        # 왼쪽 아래
        solve(r1 + size, r2, c1 , c1 + size - 1, size)

        # 오른쪽 아래
        solve(r1 + size, r2, c1 + size, c2, size)

        print(")", end = "")
        return


solve(0, n -1, 0, n-1, n)
