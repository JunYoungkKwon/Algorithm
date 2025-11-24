# 자판의 크기 R, C와 상어의 수 M
# (r, c)는 상어의 위치, s는 속력, d는 이동 방향, z는 크기
# d가 1인 경우는 위, 2인 경우는 아래, 3인 경우는 오른쪽, 4인 경우는 왼쪽
# from collections import deque
#
# deq = deque()
# R, C, M = map(int, input().split())
# board = [[0]* (C+1) for _ in range(R+1)]
#
# dy = [-1,1,0,0]
# dx = [0,0,1,-1]
#
# def is_valid(y, x):
#     return 1 <= y <= R and 1 <= x <= C
#
# def catch_fish(li):
#     for i in range(1, R+1):
#         if board[i][li] != 0:
#             fish_pos = (i, li)
#             fish_size = board[i][li]
#             return fish_pos, fish_size
#     return None
#
# for _ in range(M):
#     r, c, s, d, z = map(int, input().split())
#     board[r][c] = z
#     deq.append((r, c, s, d, z))
#
# line = 1
# ans = 0
#
# while True:
#
#     if line > C:
#         print(ans)
#         break
#     fishing = catch_fish(line)
#
#     #못잡으면
#     if fishing is None:
#         line += 1
#         continue
#
#     #잡으면 덱에서 삭제
#     for x,y,_,_,_ in deq:
#         if
#
#
#
#
#
#     #잡은 물고기 삭제
#
#     #물고기 이동
#
#
#
#
#
#     line += 1
#
#
