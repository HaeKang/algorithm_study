# https://programmers.co.kr/learn/courses/30/lessons/60057

def solution(s):
    result_list = []    # 문자열들의 길이 저장

    # 문자열 길이가 1인 경우엔 답은 1
    if len(s) == 1:
        return 1

    # 1개로 압축 ~ len(s) // 2 개로 압축 경우 까지 for문 수행
    for i in range(1, len(s) // 2 + 1):

        result_str = ""  # 최종 완성 문자열

        cnt = 1
        cut_str = s[:i]  # 압축할 문자열 -> "0" idx 부터 "i-1" idx까지

        # i 만큼 증가시켜가며 문자열 비교
        # i 부터 (압축할 문자열 개수) s 문자열 길이까지 i씩 더해가며 for문 수행 
        # i개 만큼 문자열을 자르겠단 의미
        for k in range(i, len(s), i):
            
            # "k" idx 부터 "k+i-1" idx 까지
            if s[k:k + i] == cut_str:    # 이전 문자열이랑 동일하면
                cnt += 1

            else:   # 문자열이 바뀐 경우
                if cnt == 1:    # 문자열이 한 번 나온경우엔 ""로 대체
                    cnt = ""

                result_str += str(cnt) + cut_str    # 최종 문자열에 추가

                cnt = 1
                cut_str = s[k:k+i]  # 압축할 문자열 변경

        # 마지막 문자열 처리
        if cnt == 1:
            cnt = ""

        result_str += str(cnt) + cut_str
        result_list.append(len(result_str)) # i개의 문자열로 짤랐을때의 최종 문자열 길이 넣음


    return min(result_list) # 문자열 길이 중 최소값 
