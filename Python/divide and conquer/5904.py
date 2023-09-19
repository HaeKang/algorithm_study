# https://www.acmicpc.net/problem/5904
# 처음엔 dp 생각하고 풀었으나, 메모리초과
import sys
input = sys.stdin.readline

n = int(input())

moo_str = ["m", "o", "o"]

# n : 찾고자 하는 n번째 글자
# depth : 차수
# l : 이전 차수 길이


def moo(n, depth, prev_len):
    if n <= 3:
        return(moo_str[n - 1])

    # 이전 문자열 길이 * 2 , 새로운 o의 갯수, 새로운 m 갯수 1개
    new_len = 2 * prev_len + depth + 2 + 1

    # 현재 길이가 n보다 작으면 재귀
    if new_len < n:
        return moo(n, depth + 1, new_len)

    else:
        # n은 prev_len보다 반드시 크므로 새로 추가한 가운데와 뒷부분만 확인 필요

        # 가운데 영역일 경우
        if n <= prev_len + depth + 2 + 1:
            if n - prev_len == 1:
                return "m"
            else:
                return "o"

        # 뒷부분인 경우
        else:

            # 뒷부분은 결국 현재 depth 차수보다 아래 차수의 결과값이므로 다시 맨 처음으로 돌아가서 구함
            return moo(n - (prev_len + depth + 2 + 1), 1, 3)


print(moo(n, 1, 3))
