from collections import deque


def bfs(start, board, chk):
    q = deque([start])
    chk[start] = True
    cnt = 1
    while q:
        n = q.popleft()
        for i in board[n]:
            if not chk[i]:
                chk[i] = True
                q.append(i)
                cnt += 1
    return cnt


def solution(n, wires):
    answer = n
    for i in range(len(wires)):
        board = [[] for _ in range(n + 1)]
        chk = [False] * (n + 1)
        for j in range(len(wires)):
            if i == j:
                continue
            y, x = wires[j]
            board[y].append(x)
            board[x].append(y)
        a = bfs(1, board, chk)
        answer = min(answer, abs((n - a) - a))

    return answer

print(solution(9,	[[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]]))
