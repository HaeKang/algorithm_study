# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=2&problemLevel=3&contestProbId=AV15Khn6AN0CFAYD&categoryId=AV15Khn6AN0CFAYD&categoryType=CODE&problemTitle=&orderBy=INQUERY_COUNT&selectCodeLang=PYTHON&select-1=3&pageSize=10&pageIndex=1#none

T = int(input())


def dfs(cnt):
    global answer

    # 모든 교환 횟수 소모. 이전 답과 비교
    if cnt == 0:
        tmp = int(''.join(arr))
        answer = max(answer, tmp)
        return

    for i in range(arr_len):
        for j in range(i + 1, arr_len):
            arr[i], arr[j] = arr[j], arr[i]
            tmp_ans = ''.join(arr)

            # visited 딕셔너리에 (tmp_ans, cnt-1) 의 값이 default인 1이면 안나온 케이스인것.
            if visited.get((tmp_ans, cnt - 1), 1) == 1:
                visited[(tmp_ans, cnt-1)] = 0   # 해당 tmp_ans의 cnt회차 저장
                dfs(cnt - 1)

            # 원상복구
            arr[i], arr[j] = arr[j], arr[i]


# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    answer = -1

    arr, cnt = input().split()

    cnt = int(cnt)
    arr = list(arr)

    arr_len = len(arr)
    visited = {}
    dfs(cnt)
    print("#{} {}".format(test_case, answer))
