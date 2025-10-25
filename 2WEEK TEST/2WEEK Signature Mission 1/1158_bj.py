from collections import deque
N, K = map(int, input().split())

deq = deque([_ for _ in range(1, N+1)])
ans = []
while True:
    if len(deq) < 1:
        break
    deq.rotate(-(K-1))
    ans.append(deq[0])
    deq.popleft()

print("<" + ", ".join(map(str, ans)) + ">")


