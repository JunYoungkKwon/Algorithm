from collections import deque

# deq = ([])

N, M = map(int, input().split())
find_num = list(map(int, input().split()))
deq = deque([_ for _ in range(1, N+1)])
ans = 0

for i in range(M):
    while True:
        if deq[0] == find_num[i]:
            deq.popleft()
            break
        else:
            if deq.index(find_num[i]) > len(deq) // 2:
                deq.rotate(1)
                ans += 1
            else:
                deq.rotate(-1)
                ans += 1
print(ans)