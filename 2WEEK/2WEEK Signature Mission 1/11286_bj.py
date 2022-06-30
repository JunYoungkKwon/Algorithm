#절대값으로 변환한 값을 뺄 때 구분하기 위해서 튜플로 원래의 값 넣어주기
import sys
import heapq
abs_heap = []
input = sys.stdin.readline

for _ in range(int(input())):
    x = int(input())
    if x == 0:
        if abs_heap:
            print(heapq.heappop(abs_heap)[1])
        else:
            print(0)
    else:
        heapq.heappush(abs_heap, (abs(x), x))