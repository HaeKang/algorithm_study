import heapq

def solution(operations):
    heap = []
    
    for o in operations:
        o = o.split(' ')
        num = int(o[1])
        
        # 숫자삽입
        if o[0] == 'I':
            heapq.heappush(heap, num)
        
        # 삭제
        elif o[0] == 'D':
            if len(heap) == 0:
                continue
                
            if num == 1: 
                heap = heapq.nlargest(len(heap), heap)[1:]  # 최대값 제외
                heapq.heapify(heap) # list -> heap
                
            else:  
                heapq.heappop(heap)


    if heap:
        return [max(heap), min(heap)]
    else:
        return [0,0]
