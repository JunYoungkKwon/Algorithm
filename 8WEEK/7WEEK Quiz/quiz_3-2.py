from itertools import combinations
from collections import defaultdict
def solution(orders, course):
    answer = []
    for cours_size in course:
        cnt_combi = defaultdict(int)
        for order in orders:
            if int(cours_size) > len(order):
                continue
            else:
                for com in combinations(order, cours_size):
                    com = "".join(sorted(com))
                    cnt_combi[com] += 1
        print(cnt_combi)

        for k, v in cnt_combi.items():
            if max(cnt_combi.values()) == v:
                if max(cnt_combi.values()) == 1:
                    break
                else:
                    answer.append(str(k))
    answer.sort()
    return answer


print(solution(["XYZ", "XWY", "WXA"],	[2,3,4]))
