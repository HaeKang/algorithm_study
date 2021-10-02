# n : 시 (hour) m : 찾고자 하는 수 (문제에선 3)
n, m = map(int, input().split())

ans = 0

# 시
for i in range(n+1):
    # 분
    for j in range(60):
        # 초
        for k in range(60):
            # find 함수에서 값을 못찾으면 -1을 반환 ~ 따라서 -1보다 크면 m이 있다는 의미
            if str.find(str(i)+str(j)+str(k), str(m)) > -1:
                ans += 1

print(ans)


# https://www.acmicpc.net/problem/18312 백준에 해당 문제와 완전 거의 똑같은 유사한 문제가 있음!
# 문제는 이런 방식으로 풀면 틀렸다고 나옴
# 아래는 수정한 코드

# n : 시 (hour) m : 찾고자 하는 수 (문제에선 3)
n, m = map(int, input().split())

ans = 0

# 시
for i in range(n+1):
    # 분
    for j in range(60):
        # 초
        for k in range(60):

            if i < 10:
                hour = '0' + str(i)
            else:
                hour = str(i)

            if j < 10:
                min = '0' + str(j)
            else:
                min = str(j)

            if k < 10:
                sec = '0' + str(k)
            else:
                sec = str(k)

            if str.find(hour+min+sec, str(m)) > -1:
                ans += 1

print(ans)


# 첫번째 코드로 하면 안되는 이유는 '0'을 고려하지 않았다고 생각 ~> 따라서 시, 분, 초가 10 이하면 앞에 0을 붙여줌
