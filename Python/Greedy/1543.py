# https://www.acmicpc.net/problem/1543
import sys
input = sys.stdin.readline

doc = input().rstrip()
target = input().rstrip()
target_len = len(target)


def find_doc(start_idx):
    global doc, target, target_len
    tmp_ans = 0

    next_idx = -1
    for i in range(start_idx, len(doc)):
        if next_idx != -1:
            if i < next_idx:
                continue

            if i + target_len > len(doc):
                break

            else:
                if doc[i:i + target_len] == target:
                    tmp_ans += 1
                    next_idx = i + target_len

        else:
            if doc[i:i + target_len] == target:
                tmp_ans += 1
                next_idx = i + target_len

    return tmp_ans


ans = 0
for i in range(len(doc)):
    ans = max(ans, find_doc(i))

print(ans)
