# 각 유저는 한 번에 한 명의 유저를 신고할 수 있습니다.
# 신고 횟수에 제한은 없습니다. 서로 다른 유저를 계속해서 신고할 수 있습니다.
# 한 유저를 여러 번 신고할 수도 있지만, 동일한 유저에 대한 신고 횟수는 1회로 처리됩니다.
# k번 이상 신고된 유저는 게시판 이용이 정지되며, 해당 유저를 신고한 모든 유저에게 정지 사실을 메일로 발송합니다.
# 유저가 신고한 모든 내용을 취합하여 마지막에 한꺼번에 게시판 이용 정지를 시키면서 정지 메일을 발송합니다.
from collections import defaultdict
def solution(id_list, report, k):
    answer = [0] * len(id_list)
    #중복 신고 제거
    report = set(report)
    report_user = defaultdict(set)
    reported_user = defaultdict(int)

    for re in report:
        report_peo, reported_peo = re.split()
        report_user[report_peo].add(reported_peo)
        reported_user[reported_peo] += 1
    #     print(f"{report_peo} {reported_peo}")
    # print(f"{report_user}")
    # print(f"{reported_user}")

# muzi~neo
    i= 0
    for id in id_list:
        for n in report_user[id]:
            if reported_user[n] >= k:
                answer[i] += 1
        i += 1




    return answer
print(solution(["muzi", "frodo", "apeach", "neo"], ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"], 2))
# #[2,1,1,0]