# https://school.programmers.co.kr/learn/courses/30/lessons/150370
def solution(today, terms, privacies):
    answer = []
    
    today_lst = list(map(int, today.split(".")))
    year = today_lst[0]
    month = today_lst[1]
    day = today_lst[2]
    
    today_day = (year * 12 * 28) + (month * 28) + day
    print(today_day)
    
    term_dict = {}
    for term in terms:
        a, b = term.split(" ")
        term_dict[a] = int(b) * 28
    
    for idx, privaciry in enumerate(privacies):
        date, term = privaciry.split()
        
        date_lst = list(map(int, date.split(".")))
        year = date_lst[0]
        month = date_lst[1]
        day = date_lst[2]
        
        now_day = (year * 12 * 28) + (month * 28) + day + term_dict[term]
        print(now_day)
        
        if now_day <= today_day:
            answer.append(idx + 1)
    
    answer.sort()
    
    return answer
