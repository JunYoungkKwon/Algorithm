from collections import deque
ans = 0
N, M = map(int, input().split())
find = list((map(int, input().split()))) # 1, 2 ,3
deq = deque([i for i in range(1, N+1)]) # 1 ... 10



for i in range(M):
    while True:
        if deq[0] == find[i]:
            deq.popleft()
            break
        else:
            if deq.index(find[i]) >= len(deq) / 2:
                deq.appendleft(deq.pop())
                ans += 1
            else:
                deq.append(deq.popleft())
                ans += 1
print(ans)
