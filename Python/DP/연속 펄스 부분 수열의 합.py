# https://school.programmers.co.kr/learn/courses/30/lessons/161988
def solution(sequence):
    
    seq_len = len(sequence)
    # [-1, 1, -1]을 곱한 sequence 구하기
    for idx in range(seq_len):
        if idx % 2 == 1:
            sequence[idx] *= -1 
    
    dp = [[0, 0] for _ in range(seq_len) ]
    
    for i in range(1, seq_len) :
        num = sequence[i]
        dp[i][0] = min(num, num + dp[i-1][0])
        dp[i][1] = max(num, num + dp[i-1][1])

    min_val = min(map(min, dp))
    max_val = max(map(max, dp))
        
    return max(abs(min_val), abs(max_val))
