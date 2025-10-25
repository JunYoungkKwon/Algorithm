# N = int(input())
# A = list(map(int, input().split()))
#
# # A를 정렬한 결과를 저장
# sorted_A = sorted(A)
#
# # 각 값이 B(정렬된 A)에서 어디에 있는지 기록할 딕셔너리
# # 중복 처리를 위해 index가 아닌 카운트를 쓸 예정
# index_map = {}
# for i, v in enumerate(sorted_A):
#     if v not in index_map:
#         index_map[v] = i
#
# # 실제 결과 저장
# P = []
# used = {}
#
# for a in A:
#     idx = index_map[a]
#     P.append(idx)
#     # used[a] = used.get(a, 0) + 1
#     index_map[a] = idx+1
#
# print(*P)
