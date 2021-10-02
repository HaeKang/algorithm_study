# 두가지 방법으로 풀었음
# 파이썬 내장 함수인 isalpha 함수를 이용하는 방법과 아스키코드값을 이용한 경우

string = input()

num = 0
ans = []

# 파이썬은 isalpha라는 내장함수로 해당 문자열이 알파벳인지 숫자인지 알 수 있음

for i in string:
    if i.isalpha():
        ans.append(i)
    else:
        num += int(i)

ans.sort()

if num > 0:
    num_str = str(num)
    ans.append(num_str)

print(''.join(ans))


# 아스키코드값 사용한 방법
num2 = 0
ans2 = []

for i in string:
    if ord(i) >= 65 and ord(i) <= 90:
        ans2.append(i)
    else:
        num2 += int(i)

ans2.sort()
if num2 > 0:
    num_str = str(num2)
    ans2.append(num_str)

print(''.join(ans2))
