import heapq
from collections import defaultdict

def solution(operations):
    min_h = []
    max_h = []
    dic = defaultdict(int)

    for s in operations:
        cmd, num = s.split()
        num = int(num)

        # 삽입
        if cmd == "I":
            heapq.heappush(min_h, num)
            heapq.heappush(max_h, -num)
            dic[num] += 1

        # 삭제
        elif cmd == "D":
            if num == -1:  # 최소값 삭제
                while min_h:
                    x = heapq.heappop(min_h)
                    if dic[x] > 0:
                        dic[x] -= 1
                        break
            else:          # 최대값 삭제
                while max_h:
                    x = -heapq.heappop(max_h)
                    if dic[x] > 0:
                        dic[x] -= 1
                        break

    max_val = None
    min_val = None

    while max_h:
        x = -heapq.heappop(max_h)
        if dic[x] > 0:
            max_val = x
            break

    while min_h:
        x = heapq.heappop(min_h)
        if dic[x] > 0:
            min_val = x
            break

    if max_val is None or min_val is None:
        return [0, 0]

    return [max_val, min_val]
