import heapq

def solution(scoville, K):
    cnt = 0
    heapq.heapify(scoville)

    while True:
        if len(scoville) == 1 or scoville[0] > K:
            break

        min_score = heapq.heappop(scoville)

        if min_score < K:
            min_score2 = heapq.heappop(scoville)
            mix_score = min_score + (2 * min_score2)
            heapq.heappush(scoville, mix_score)
            cnt += 1
    
    min_score = heapq.heappop(scoville)
    if min_score < K:
        cnt = -1
    
    return cnt

