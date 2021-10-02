# input 받음
string = input()

# 영어 -> 아스키코드 변환
x = ord(string[0]) - 96
y = int(string[1])

# 이동할 수 있는 경우의 수
ans = 0

# 이동할 수 있는 좌표
dx = [-2, -1, 1, 2, 2, 1, -1, -2]
dy = [-1, -2, -2, -1, 1, 2, 2, 1]

for i in range(len(dx)):
    nx = x + dx[i]
    ny = y + dy[i]

    if nx <= 8 and nx >= 1 and ny <= 8 and ny >= 1:
        ans += 1

print(ans)
