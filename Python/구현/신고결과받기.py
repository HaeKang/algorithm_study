def solution(id_list, report, k):
    answer = [0] * len(id_list)

    dic = {}  # key : 신고당한사람, value : 신고자
    dic2 = {}   # key : 신고자, value : 신고당한사람

    # 중복제거
    report = set(report)

    for data in report:
        data = data.split(" ")

        user_id = data[0]   # 신고자
        report_id = data[1]  # 신고당한사람

        if report_id in dic:
            dic[report_id].append(user_id)
        else:
            dic[report_id] = [user_id]

        if user_id in dic2:
            dic2[user_id].append(report_id)
        else:
            dic2[user_id] = [report_id]

    # 최종 정지
    close_id = []
    for key in dic:
        if len(dic[key]) >= k:
            close_id.append(key)

    for id in close_id:
        for i in range(0, len(id_list)):
            if id_list[i] in dic2:
                if id in dic2[id_list[i]]:
                    answer[i] += 1

    return answer
