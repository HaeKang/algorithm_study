def solution(lottos, win_nums):
    answer = []
    
    # key : 번호 개수 value : 순위
    rank_info = {6:1, 5:2, 4:3, 3:4, 2:5}
    
    cnt = 0

    for win_num in win_nums:
        for lotto in lottos:
            if win_num == lotto:
                cnt += 1
                
    min_rank = cnt
    max_rank = cnt + lottos.count(0)
    
        
    if max_rank in rank_info:
        answer.append(rank_info[max_rank])
    else:
        answer.append(6)
        
    if min_rank in rank_info:
        answer.append(rank_info[min_rank])
    else:
        answer.append(6)
    
    return answer
