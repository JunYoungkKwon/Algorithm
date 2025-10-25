import heapq

hq = []

for _ in range(int(input())):
    x = list(map(int, input().split()))
    #선물 주는 경우
    if x[0] == 0:
        # 선물 있는 경우
        if hq:
            print(-(heapq.heappop(hq)))

        else:
            print(-1)

    # 선물 충전하는 경우
    else:
        for i in x[1:]:
            heapq.heappush(hq, -i)





