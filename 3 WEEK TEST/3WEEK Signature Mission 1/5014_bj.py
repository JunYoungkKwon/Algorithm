# F층 건물
# 스타티링크는 G층
# 강호는 S층
# 버튼을 최소 몇 번 눌러야 하는지 구하는 프로그램을 작성하시오.
# G층에 갈 수 없다면, "use the stairs"를 출력
# 첫째 줄에 F, S, G, U, D가 주어진다.
# (1 ≤ S, G ≤ F ≤ 1000000, 0 ≤ U, D ≤ 1000000)
# 건물은 1층부터 시작하고, 가장 높은 층은 F층이다.

from collections import deque

F, S, G, U, D = map(int, input().split())

visited = [False]* (F+1)

def is_valid(s):
    return 1 <= s <= F

def bfs():
    ans = 0
    deq = deque()
    deq.append((S, ans))

    while deq:
        s, count = deq.popleft()

        #목표 지점 도달시
        if s == G:
            return count

        for i in (U, -D):
            ns = s + i
            if is_valid(ns) and not visited[ns]:
                visited[ns] = True
                deq.append((ns, count+1))
    return "use the stairs"

print(bfs())