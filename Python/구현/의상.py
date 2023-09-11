# https://school.programmers.co.kr/learn/courses/30/lessons/42578

def solution(clothes):
    answer = 0
    
    cloth_dict = {}

    for cloth in clothes:
        c, c_type = cloth[0], cloth[1]
        
        if c_type in cloth_dict:
            cloth_dict[c_type].append(c)
        else:
            cloth_dict[c_type] = [c]
            
    if len(cloth_dict.keys()) == 1:
        return len(clothes)
    
    else:
        answer = 1
        for key in cloth_dict.keys():
            answer *= (len(cloth_dict[key]) + 1)
        
        answer -= 1
    
    return answer
