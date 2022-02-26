def solution(land):
    for i in range(1,len(land)):
        for j in range(4):
            
            max_val = 0
            for k in range(4):
                if k == j:
                    continue
                max_val = max(max_val, land[i-1][k])
                
            land[i][j] += max_val

    return max(land[len(land)-1])
