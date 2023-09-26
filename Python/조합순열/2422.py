# https://www.acmicpc.net/problem/2422
"""
5 3
1 2
3 4
1 3

3
"""
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [i for i in range(1, n+1)]
except_arr = [[0] * (n+1) for _ in range(n+1)]
for _ in range(m):
    num1, num2 = map(int, input().split())
    except_arr[num1][num2] = 1
    except_arr[num2][num1] = 1


# 모든 조합 구하기
combi_arr = []
def make_combi(result):
    if len(result) == 3:
        combi_arr.append(result)
        return
    
    start = 0
    if len(result) != 0:
        start = arr.index(result[-1]) + 1
    
    for i in range(start, len(arr)):
        # 제외항목 체크
        tmp_arr = result + [arr[i]]

        except_flag = True
        if len(tmp_arr) == 1:
            pass
        elif len(tmp_arr) == 2:
            if except_arr[tmp_arr[0]][tmp_arr[1]] == 1:
                except_flag = False
        elif len(tmp_arr) == 3:
            if except_arr[tmp_arr[0]][tmp_arr[1]] == 1 or except_arr[tmp_arr[0]][tmp_arr[2]] == 1 or except_arr[tmp_arr[1]][tmp_arr[2]] == 1:
                except_flag = False

        if except_flag:
            make_combi(tmp_arr)
    

make_combi([])
print(len(combi_arr))
