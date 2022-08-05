# p 응시자, 0 빈테이블, X 파티션

from collections import deque
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
person = []
chk_person = []
def is_valid(y, x):
    return 0 <= y < 5 and 0 <= x< 5

def bfs(start, last, board):
    q = deque
    q.append((start[0], start[1], 0))
    chk = [[0] * 5 for _ in range(5)]
    chk[start[0]][start[1]] = 1
    while q:
        y, x, d = q.popleft()
        if y == last[0] and x == last[1]:
            if d > 0:
                return True
            else:
                return False
            break

        for k in range(4):
            ny = y + dy[k]
            nx = x + dx[k]
            if is_valid(ny, nx) and not chk[ny][nx]:
                if board[ny][nx] == "X":
                    q.append((ny, nx, d+1))
                else:
                    q.append((ny, nx, d))

def solution(places):
    answer = []
    for pla in places:
        wait_room = pla
        for i in range(5):
            for j in range(5):
                if wait_room[i][j] == "P":
                    person.append((i, j))
        # 두 테이블 T1, T2가 행렬 (r1, c1), (r2, c2)에 각각 위치하고 있다면, T1, T2 사이의 맨해튼 거리는 |r1 - r2| + |c1 - c2| 입니다.
        for k in range(len(person)):
            for u in range(k+1, len(person)):
                if abs(person[k][0] - person[j][0]) + abs(person[k][1] - person[j][1]) <= 2:
                    chk_person.append((person[k], person[j]))
        if not chk_person:
            answer.append(1)
        else:
            for b in chk_person:
                if bfs(b[0], b[1], wait_room):
                    answer.append(1)
                else:
                    answer.append(0)
    return answer
places = [["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]
print(solution(places))