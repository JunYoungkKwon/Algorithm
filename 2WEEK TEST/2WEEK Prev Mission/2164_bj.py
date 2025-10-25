from collections import deque
q = deque([_ for _ in range(int(input()), 0, -1)])

while len(q)>1:
    q.pop()
    q.appendleft(q[-1])
    q.pop()

print(*q)