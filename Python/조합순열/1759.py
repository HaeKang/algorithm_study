# https://www.acmicpc.net/problem/1759
import sys
input = sys.stdin.readline

l, c = map(int, input().split())
arr = list(input().rstrip().split())


perm_arr = []
checked = [0] * (c)


def make_perm(tmp_arr, vowel_cnt, consonant_cnt):
    global l

    if len(tmp_arr) == l:
        if vowel_cnt >= 2 and consonant_cnt >= 1:
            perm_arr.append(''.join(tmp_arr))
        return

    for i in range(0, len(arr)):
        if checked[i] == 0:
            if len(tmp_arr) > 0:
                # 증가하는 형식인지 확인
                if ord(tmp_arr[-1]) >= ord(arr[i]):
                    continue

            checked[i] = 1
            # 모음갯수, 자음 갯수
            if arr[i] in ['a', 'e', 'i', 'o', 'u']:
                make_perm(tmp_arr + [arr[i]], vowel_cnt, consonant_cnt + 1)
            else:
                make_perm(tmp_arr + [arr[i]], vowel_cnt + 1, consonant_cnt)
            checked[i] = 0


make_perm([], 0, 0)
perm_arr.sort()
for perm in perm_arr:
    print(perm)
