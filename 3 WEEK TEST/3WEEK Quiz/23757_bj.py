import heapq
hq = []
N, M = map(int, input().split())
present = list(map(int, input().split()))
for i in present:
    heapq.heappush(hq, -i)

child = list(map(int, input().split()))

for i in child:
    a = -heapq.heappop(hq)
    if i > a:
        print(0)
        break
    else:
        heapq.heappush(hq, -(a-i))
else:
    print(1)






