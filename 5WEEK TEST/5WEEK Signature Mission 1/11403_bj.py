# (0,1)   0->1
# (1,2)   1->2
# (2,0)   2->0
# ------------
# 0,3    0->3
# 1,6    1->6
# 3,4 3,5  3->4,5
# 4,0    4->0
# 5,6    5->6
# 6,2    6->2
#
# 정점 i에서 j로 가는 길이가 양수인 경로가 있으면 i번째 줄의 j번째 숫자를 1로, 없으면 0으로 출력
# 0 -> 3, 4, 5, 0, 6, 2

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]

ans = [[0] * N for _ in range(N)]


def bfs(start, cur):
    for nxt in range(N):
        if not chk[nxt] and board[cur][nxt] == 1:
            chk[nxt] = True
            ans[start][nxt] = 1
            bfs(start, nxt)




for i in range(N):
    chk = [False] * N
    bfs(i, i)


for i in ans:
    print(*i)