import sys, heapq
input = sys.stdin.readline
abs_heap = []

for _ in range(int(input())):
    x = int(input())
    if x == 0:
        if abs_heap:
            print(heapq.heappop(abs_heap)[1])
        else:
            print(0)


    else:
        heapq.heappush(abs_heap, (abs(x), x))


