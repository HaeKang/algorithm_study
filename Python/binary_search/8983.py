'''
https://www.acmicpc.net/problem/8983
'''
import sys
input  = sys.stdin.readline

m, n, l = map(int, input().split()) # 사대 수, 동물 수, 사정거리

m_x = list(map(int, input().split()))   # 사대 x 좌표
m_x.sort()

animal = [list(map(int, input().split())) for _ in range(n)]    # 동물 좌표

# dist = | 사대위치 - 동물 x 좌표 | + 동물 y 좌표

ans = 0

for a in animal:
    x = a[0]
    y = a[1]

    
    start = 0
    end = m - 1

    # y좌표가 사정거리 보다 크면 잡을 수 없음.
    if y > l:
        continue

    # 해당 동물과 가장 가까운 사대 위치 찾기
    while start < end:
        mid = (start + end) // 2

        if m_x[mid] < x:
            start = mid + 1
        
        elif m_x[mid] > x:
            end = mid - 1
        
        else:
            start = mid
            break
    
    flag = False
    
    if abs(m_x[start] - x) + y <= l:
        flag = True
    elif start - 1  >= 0 and abs(m_x[start - 1] - x) + y <= l:
        flag = True
    elif start + 1 <= m - 1 and abs(m_x[start + 1] - x) + y <= l:
        flag = True

    if flag:
        ans += 1
    

print(ans)
