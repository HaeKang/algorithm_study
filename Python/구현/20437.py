import sys
from collections import deque

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    # 알파벳 등장 인덱스 저장
    alpha = [[] for _ in range(26)]

    input_str = input().strip()  # strip : 공백제거
    k = int(input())

    # 최소 최대 길이
    min_len = 123456
    max_len = -1

    for i in range(len(input_str)):
        alpha_code = ord(input_str[i]) - ord('a')
        alpha[alpha_code].append(i)

    # 후보군 알파벳 넣음 (a : 0 ~)
    candidate_alpha = []

    for i in range(len(alpha)):
        if len(alpha[i]) >= k:
            candidate_alpha.append(i)

    if len(candidate_alpha) == 0:
        print(-1)
    else:
        # 문자열 찾기
        for i in range(len(candidate_alpha)):
            target = candidate_alpha[i]
            for j in range(len(alpha[target]) - k + 1):
                tmp = alpha[target][j+k-1] - alpha[target][j] + 1

                if tmp < min_len:
                    min_len = tmp

                if tmp > max_len:
                    max_len = tmp

        print(min_len, max_len)
