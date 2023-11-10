# https://school.programmers.co.kr/learn/courses/30/lessons/77486

def solution(enroll, referral, seller, amount):

    answer = [0] * len(enroll)
    
    dict = {}
    for idx, e in enumerate(enroll):
        dict[e] = idx
        
    for idx in range(len(seller)):
        s = seller[idx]
        a = amount[idx]
        
        profit = a * 100
        
        while s != '-' and profit > 0:
            idx2 = dict[s]
            answer[idx2] += profit - profit // 10
            profit = profit // 10
            s = referral[idx2]
            
    return answer
