# https://school.programmers.co.kr/learn/courses/30/lessons/42627

import heapq

def solution(jobs):
    answer = 0

    now_time = 0    # 현재 시간
    prev_start = -1 # 이전 시작시간
    cnt = 0         # 작업 시작 갯수

    q = []  # [[wgt, 시작시간]]

    # 작업 시작 갯수가 jobs의 갯수랑 동일하면 종료
    while cnt < len(jobs):

        # 작업 시작 시간이 현재 time보다 작고 이전 시작 시간보다 큰 작업만 넣기
        for job in jobs:
            if prev_start < job[0] <= now_time:
                heapq.heappush(q, [job[1], job[0]])
        
        if len(q) == 0:
            now_time += 1        
        else:
            wgt, start_time = heapq.heappop(q)

            cnt += 1        # 작업 시작 갯수 추가

            prev_start = now_time   # 이전 시작 시간 초기화 
            now_time += wgt
            answer += (now_time - start_time) # 소요시간

    answer = answer // len(jobs)
    return answer
