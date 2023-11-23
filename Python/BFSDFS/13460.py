# https://www.acmicpc.net/problem/13460
# dfs로 풀었으나, bfs로 푸는게 더 좋을듯.
import sys
input = sys.stdin.readline

# 행, 열
n, m = map(int, input().split())

arr = [list(input().rstrip()) for _ in range(n)]
checked = []


# 파란공, 빨간공(시작점),  위치
blue = [0, 0]
red = [0, 0]
target = [0, 0]

for i in range(n):
    for j in range(m):
        if arr[i][j] == 'R':
            red = [i, j]
        
        elif arr[i][j] == 'B':
            blue = [i, j]
        
dr = [0, 0, -1, 1]
dc = [-1, 1, 0, 0]

ans = 1e9

def dfs(red, blue, cnt):
    global ans

    for i in range(4):

        # 파란공 이동
        blue_move_r = blue[0]
        blue_move_c = blue[1]
        blue_move_cnt = 0
        blue_flag = False

        while True:
            # 범위 체크
            if blue_move_r + dr[i] < 0 or blue_move_r + dr[i] >= n or blue_move_c + dc[i] < 0 or blue_move_c + dc[i] >= m:
                break
            
            # 장애물 체크
            if arr[blue_move_r + dr[i]][blue_move_c + dc[i]] == '#':
                break
            
            # 탈출구 체크
            elif arr[blue_move_r + dr[i]][blue_move_c + dc[i]] == 'O':
                blue_flag = True
                break
            
            blue_move_cnt += 1
            blue_move_r += dr[i]
            blue_move_c += dc[i]

        # 파란공 탈출하면 다음 케이스 따지러
        if blue_flag:
            continue

        # 빨간공 이동
        red_move_r = red[0]
        red_move_c = red[1]
        red_move_cnt = 0

        while True:
            # 범위 체크
            if red_move_r + dr[i] < 0 or red_move_r + dr[i] >= n or red_move_c + dc[i] < 0 or red_move_c + dc[i] >= m:
                break
            
            # 장애물 체크
            if arr[red_move_r + dr[i]][red_move_c + dc[i]] == '#':
                break
            
            # 탈출구 체크
            elif arr[red_move_r + dr[i]][red_move_c + dc[i]] == 'O':
                ans = min(ans, cnt + 1)
                return
            
            red_move_r += dr[i]
            red_move_c += dc[i]
            red_move_cnt += 1

        # 겹침 확인 (더 많이 움직인게 뒤로)
        if red_move_r == blue_move_r and red_move_c == blue_move_c:
            if red_move_cnt > blue_move_cnt:
                red_move_r -= dr[i]
                red_move_c -= dc[i]
            
            else:
                blue_move_r -= dr[i]
                blue_move_c -= dc[i]

        # print("이동 횟수 ", cnt + 1)
        # print("최종 파란공 위치 ",  blue_move_r, blue_move_c)
        # print("최종 빨간공 위치 ",  red_move_r, red_move_c)

        if cnt + 1 < 10:
            if [red_move_r, red_move_c, blue_move_r, blue_move_c] not in checked:
                checked.append([red_move_r, red_move_c, blue_move_r, blue_move_c])
                dfs([red_move_r, red_move_c], [blue_move_r, blue_move_c], cnt + 1)
                checked.remove([red_move_r, red_move_c, blue_move_r, blue_move_c] )
    

dfs(red, blue, 0)
if ans == 1e9:
    print(-1)
else:
    print(ans)
