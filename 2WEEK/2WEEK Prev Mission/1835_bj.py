from collections import deque

deq = deque()
N = int(input())
for i in range(N,0, -1):
    deq.appendleft(i)
    for _ in range(i):
        deq.appendleft(deq.pop())
print(*list(deq))


