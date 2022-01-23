answer = 0

def dfs(numbers, sum, cnt, target):
    global answer
    if cnt == len(numbers):
        if sum == target:
            answer += 1
            return
        else:
            return
    
    dfs(numbers, sum + numbers[cnt], cnt+1, target)
    dfs(numbers, sum - numbers[cnt], cnt+1, target)
    

def solution(numbers, target):
    dfs(numbers, 0, 0, target)
    return answer
