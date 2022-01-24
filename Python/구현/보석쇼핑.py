def solution(gems):
    # 초기 ans값을 맨 처음 idx, 맨 마지막 idx로 설정
    answer = [0, len(gems)-1]

    # 보석 종류
    gem_kind = set(gems)

    # start 포인터, end 포인터
    s = 0
    e = 0

    # 현재 가지고 있는 보석 개수 리스트
    dic = {gems[0]: 1}

    while s < len(gems) and e < len(gems):
        if len(dic) < len(gem_kind):
            e += 1
            if e == len(gems):
                break
            if dic.get(gems[e]) is None:
                dic[gems[e]] = 1
            else:
                dic[gems[e]] = dic.get(gems[e]) + 1
        
        # 종류가 다 모아졌으면
        else:
            # 최소값 판단
            if (e-s+1) < (answer[1] - answer[0] + 1):
                answer = [s,e]
                
            if dic[gems[s]] == 1:
                del dic[gems[s]]
            
            else:
                dic[gems[s]] -= 1
            
            s += 1
            
                
    answer[0] += 1
    answer[1] += 1
    return answer
