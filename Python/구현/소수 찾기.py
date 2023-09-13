# https://school.programmers.co.kr/learn/courses/30/lessons/42839
import math
# from itertools import permutations


def check_num(n):
    if n < 2:
        return False

    sqrt_num = math.sqrt(n)

    for i in range(2, int(sqrt_num) + 1):
        if n % i == 0:
            return False

    return True


def perm(arr, n):
    result = []

    if n == 1:
        for i in arr:
            result.append([i])
    elif n > 1:
        for i in range(len(arr)):
            tmp = [i for i in arr]
            tmp.remove(arr[i])

            for p in perm(tmp, n-1):
                result.append([arr[i]] + p)

    return result


def solution(numbers):
    answer = []
    for i in range(1, len(numbers)+1):
        # num_list = list(permutations(numbers, i))  # 순열

        num_list = perm(list(numbers), i)

        for j in range(len(num_list)):
            result_num = int(''.join(map(str, num_list[j])))
            if check_num(result_num):
                answer.append(result_num)

    return len(list(set(answer)))

