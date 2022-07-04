import heapq as hq
present = []
for _ in range(int(input())):
    a = list(map(int, input().split()))
    if a[0] ==0:
        if present: #선물 o
            print(-hq.heappop(present))

        else: #선물 x
            print(-1)

    else: #0이 아니면 선물 충전
        for i in a[1:]:
            hq.heappush(present, -i)
