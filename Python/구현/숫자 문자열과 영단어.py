def solution(s):
    answer = ''
    dic = {'zero': '0', 'one': '1', 'two': '2', 'three': '3', 'four': '4',
           'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}

    tmp_str = ''
    for i in range(len(s)):
        
        # 숫자가 온 경우
        if ord(s[i]) < 58:
            print(s[i], " ", tmp_str)
            if tmp_str != '':
                answer += dic[tmp_str]
                tmp_str = ''

            answer += s[i]

        # 그 외 경우
        else:
            tmp_str += s[i]

        # dic에 key가 있는 경우
        if tmp_str in dic:
            answer += dic[tmp_str]
            tmp_str = ''

    answer = int(answer)

    return answer

