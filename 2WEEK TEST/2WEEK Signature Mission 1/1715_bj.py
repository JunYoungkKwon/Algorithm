import heapq
N = int(input())
hq = []
sum = 0
for i in range(N):
    heapq.heappush(hq, int(input()))

while len(hq) > 1:
    a = heapq.heappop(hq)
    b = heapq.heappop(hq)
    c = a + b
    sum += c
    heapq.heappush(hq, c)

print(sum)





