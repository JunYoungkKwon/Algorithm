# ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"]	[2,3,4]	["AC", "ACDE", "BCFG", "CDE"]
# 코스요리 메뉴는 최소 2가지 이상의 단품메뉴로 구성하려고 합니다.
# 또한, 최소 2명 이상의 손님으로부터 주문된 단품메뉴 조합에 대해서만 코스요리 메뉴 후보에 포함
from collections import Counter
from itertools import combinations


def solution(orders, course):
    answer = []

    # 주문 문자열 정렬
    orders = [''.join(sorted(order)) for order in orders]

    # 코스 설정
    for k in course:
        comb_counter = Counter()
        # 코스 요리 설정
        for order in orders:
            if len(order) >= k:
                combs = combinations(order, k)
                for com in combs:
                    a = "".join(com)
                    comb_counter.update([a])

        candidates = [comb for comb, cnt in comb_counter.items() if cnt >= 2]

        if not candidates:
            continue

        # max_cnt = max(comb_counter[comb] for comb in candidates)
        max_test = max(comb_counter.values())
        # print(max_cnt, max_test)

        for comb in candidates:
            if comb_counter[comb] == max_test:
                answer.append(comb)

    return sorted(answer)





