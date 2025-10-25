# from collections import deque
#
# N, K = map(int, input().split())
#
# def bfs():
#     deq = deque()
#     deq.append((N, 0))  # (숫자, 교환 횟수)
#     visited = set()
#     visited.add((N, 0))
#     result = -1
#
#     while deq:
#         x, cnt = deq.popleft()
#
#         # 교환을 K번 다 했을 때 최댓값 후보 갱신
#         if cnt == K:
#             result = max(result, x)
#             continue
#
#         str_x = list(str(x))
#         length = len(str_x)
#
#         for i in range(length):
#             for j in range(i+1, length):
#                 # 두 자리 교환
#                 str_x[i], str_x[j] = str_x[j], str_x[i]
#                 if str_x[0] != "0":  # 0으로 시작하면 안 됨
#                     nx = int("".join(str_x))
#                     if (nx, cnt+1) not in visited:
#                         visited.add((nx, cnt+1))
#                         deq.append((nx, cnt+1))
#                 # 원상복구
#                 str_x[i], str_x[j] = str_x[j], str_x[i]
#
#     return result
#
# # 한 자리 수면 교환 불가능
# if len(str(N)) == 1 or (len(str(N)) == 2 and str(N)[1] == "0"):
#     print(-1)
# else:
#     print(bfs())
