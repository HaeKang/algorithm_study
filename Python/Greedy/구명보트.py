def solution(people, limit):
    ans = 0
    
    people.sort()
    sum = 0
    
    r = len(people) - 1
    l = 0
    
    while True:
        
        if r < l:
            break
        
        if people[l] + people[r] <= limit:
            l += 1
            r -= 1
            
        else:
            r -= 1
        
        ans += 1 
        
        if l == r:
            ans += 1
            break
    
    return ans
