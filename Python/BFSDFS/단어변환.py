# https://school.programmers.co.kr/learn/courses/30/lessons/43163?language=python3
from collections import deque

def solution(begin, target, words):

    answer = 0
    
    if begin == target:
        return 0
    else:
        q = deque()
        checked = [0 for _ in range(len(words))]
        q.append([begin, 0])
        
        while q:
            word, cnt = q.popleft()
            
            if word == target:
                answer = cnt
                break
            
            for i in range(len(words)):
                if checked[i] != 0:
                    continue
                
                word_diff = 0
                for j in range(len(word)):
                    if word[j] != words[i][j]:
                        word_diff += 1
                
                # 차이가 한개인 경우
                if word_diff == 1:
                    checked[i] = 1
                    q.append([words[i], cnt + 1])
    
    return answer
