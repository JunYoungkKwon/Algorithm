# 이 문제도 덱으로 푸는 건 알았지만 구현이 어려웠음
from collections import deque

for _ in range (int(input())):
    N, M = map(int, input().split())
    deq = deque(map(int, input().split()))
    ans = 0
    while deq:
        max_num = max(deq)
        first = deq.popleft()
        M -= 1

        if first == max_num:
            ans += 1
            if M < 0:
                print(ans)
                break

        else:
            deq.append(first)
            if M < 0:
                M = len(deq)-1

