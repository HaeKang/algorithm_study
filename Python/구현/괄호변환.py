# 문자열 w -> u, v로 분리
def divide(w):
    openP = 0
    closeP = 0

    for i in range(len(w)):
        if w[i] == '(':
            openP += 1
        else:
            closeP += 1
        if openP == closeP:
            return w[:i + 1], w[i + 1:]


# 문자열 u가 "올바른 괄호 문자열" 인지 check
def isBalanced(u):
    stack = []

    for p in u:
        if p == '(':
            stack.append(p)
        else:
            if not stack:
                return False
            stack.pop()

    return True


def solution(w):
    # 1번
    if not w:
        return ""

    # 2번
    u, v = divide(w)

    # 3번
    if isBalanced(u):
        # 3-1번
        return u + solution(v)

    # 4번
    else:
        # 4-1
        answer = '('
        # 4-2
        answer += solution(v)
        # 4-3
        answer += ')'

        # 4-4
        for p in u[1:len(u) - 1]:
            if p == '(':
                answer += ')'
            else:
                answer += '('

        # 4-5
        return answer
