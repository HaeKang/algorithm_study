import sys
input = sys.stdin.readline

global ans_min, ans_max

ans_min = 10000000001
ans_max = -10000000001

n = int(input())
number_list = list(map(int, input().split()))
cal_info = list(map(int, input().split()))   # 덧셈, 뺄셈, 곱셈, 나눗셈


def dfs(idx, result, plus_cnt, minus_cnt, mul_cnt, div_cnt):
    global ans_max, ans_min

    if idx == n:
        ans_min = min(ans_min, result)
        ans_max = max(ans_max, result)
        return

    if plus_cnt > 0:
        dfs(idx+1, result + number_list[idx],
            plus_cnt-1, minus_cnt, mul_cnt, div_cnt)

    if minus_cnt > 0:
        dfs(idx+1, result - number_list[idx],
            plus_cnt, minus_cnt - 1, mul_cnt, div_cnt)

    if mul_cnt > 0:
        dfs(idx+1, result * number_list[idx],
            plus_cnt, minus_cnt, mul_cnt - 1, div_cnt)

    if div_cnt > 0:
        result_copy = result

        if result_copy < 0:
            result_copy *= -1
            result_copy = result_copy // number_list[idx]
            result_copy *= -1
        else:
            result_copy = result_copy // number_list[idx]

        dfs(idx+1, result_copy,
            plus_cnt, minus_cnt, mul_cnt, div_cnt - 1)


dfs(1, number_list[0], cal_info[0], cal_info[1], cal_info[2], cal_info[3])

print(ans_max)
print(ans_min)
