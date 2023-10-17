# https://school.programmers.co.kr/learn/courses/30/lessons/42839

perm_lst = []

def check_prime(num):
    for i in range(2, num - 1):
        if num % i == 0:
            return False
    
    return True

def get_perm(tmp, numbers, checked, cnt):
    global perm_lst
    
    if len(tmp) == cnt:
        perm_lst.append(int("".join(tmp)))
        return
    
    for i in range(len(numbers)):
        if checked[i] == 0:
            checked[i] = 1
            get_perm(tmp + [numbers[i]], numbers, checked, cnt)
            checked[i] = 0

            
def solution(numbers):
    global perm_lst
    
    answer = []
    
    numbers = list(numbers)
    
    for i in range(1, len(numbers) + 1):
        checked = [0 for _ in range(len(numbers))]
        get_perm([], numbers, checked, i)
    
    perm_lst = list(set(perm_lst))
    
    for perm in perm_lst:
        if perm == 0 or perm == 1:
            continue 
        
        if check_prime(perm):
            answer.append(perm)
    
    return len(answer)
