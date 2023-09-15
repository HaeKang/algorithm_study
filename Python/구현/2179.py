# https://www.acmicpc.net/problem/2179
# 풀이 보고 배운 문제.. 어렵다!

import sys
input = sys.stdin.readline

n = int(input())

words = [input().rstrip() for _ in range(n)]
# 문자들을 인덱스랑 같이 저장 + 사전순 정렬
# 사전순으로 정렬시키면 가장 긴 접두사를 갖고 있는 문자들끼리 인접하게 됨!!
words2 = sorted(list(enumerate(words)), key=lambda x: x[1])


# w1, w2의 연속된 글자 하나하나가 같은지 탐색하여 같은 글자 길이 return
def check(w1, w2):
    cnt = 0
    for i in range(min(len(w1), len(w2))):
        if w1[i] == w2[i]:
            cnt += 1
        else:
            break
    return cnt


# 최장 접두사를 가진 문자열 담아둠 idx = 해당 문자열의 위치
length = [0] * (n+1)
max_len = 0

# sorted된 word2에 대해 진행
for i in range(n-1):
    tmp = check(words2[i][1], words2[i+1][1])   # 인접한 두 문자열의 최대 같은 글자 길이 get
    max_len = max(tmp, max_len)  # max와 비교

    length[words2[i][0]] = max(length[words2[i][0]], tmp)
    length[words2[i + 1][0]] = max(length[words2[i + 1][0]], tmp)

# 입력된 순서대로 word에 대해 진행
first = 0
for i in range(n):
    # 최장 접두사를 발견 못한 경우
    if first == 0:
        # 현재 접두사의 길이가 최장 접두사일 경우
        if length[i] == max(length):
            first = words[i]
            print(first)    # 답 출력
            pre = words[i][:max_len]
    else:
        if length[i] == max(length) and words[i][:max_len] == pre:
            print(words[i])  # 답 출력
            break
