import sys, heapq as hq
min_heap = []
for _ in range (int(input())):
    hq.heappush(min_heap, int(input()))
ans = 0
while len(min_heap) > 1:
    hap = hq.heappop(min_heap) + hq.heappop(min_heap)
    hq.heappush(min_heap, hap)
    ans += hap

print(ans)

