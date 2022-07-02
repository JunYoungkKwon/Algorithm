import heapq

M, N = map(int, input().split())
pre = list(map(int, input().split()))
present = list(map(int, input().split()))
max_hq = []

for a in pre:
    heapq.heappush(max_hq, -a)

ans = 1
for b in present:
    max_num = -heapq.heappop(max_hq)
    if max_num >= b:
        heapq.heappush(max_hq, -(max_num-b))
    else:
        ans = 0
        break

print(ans)













