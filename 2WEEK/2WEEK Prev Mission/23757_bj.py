import heapq as hq
N, M = map(int, input().split())
max_hq = []
ans = 1
for i in map(int, input().split()):
    print(i)

    hq.heappush(max_hq, -i)

for j in map(int, input().split()):
    present = -hq.heappop(max_hq)
    if present < j:
        ans = 0
        break
    else:
        hq.heappush(max_hq, -(present-j))
print(ans)
