# https://school.programmers.co.kr/learn/courses/30/lessons/150365

from collections import deque

# bfs
# 남은 거리가 k보다 크면 impossible
# k - 최소거리 => 홀수라면, 도착점에 k만큼 도착 불가능
# 최소 거리에서 홀수만큼 이동하면, 다시 목적지에 도착할 수 없기 때문이다!

# d > l > r > u
dir_dict = {0 : 'd', 1 : 'l', 2 : 'r', 3 : 'u'}
dr = [1, 0, 0, -1]
dc = [0, -1, 1, 0]

def solution(n, m, x, y, r, c, k):
    answer = ''
    
    # 목적지까지 남은 거리
    def cal_dist(x1, y1):
        return abs(x1 - (r - 1)) + abs(y1 - (c - 1))
    
    # 최단거리가 k보다 크거나, 홀수만 남은 케이스
    if cal_dist(x - 1, y - 1) > k or (cal_dist(x - 1, y - 1) - k) % 2 > 0:
        return "impossible"
    
    q = deque()
    q.append([x - 1, y - 1, 0, ''])
    
    while q:
        now_x, now_y, now_cnt, now_route = q.popleft()
        
        # 답 찾은 케이스
        if (now_x == r - 1 and now_y == c - 1) and now_cnt == k:
            return now_route
        
        # 홀수인 케이스
        elif (now_x == r - 1 and now_y == c - 1) and (k - now_cnt) % 2 > 0:
            return  "impossible"
        
        for i in range(4):
            next_x = now_x + dr[i]
            next_y = now_y + dc[i]
            
            if 0<= next_x < n and 0 <= next_y < m:
                if cal_dist(next_x, next_y) + now_cnt + 1 > k:
                    continue
                
                q.append([next_x, next_y, now_cnt + 1, now_route + dir_dict[i]])
                break
    
    
    return answer
