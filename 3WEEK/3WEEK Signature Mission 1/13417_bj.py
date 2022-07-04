from collections import deque
T = int(input())
for _ in range(T):
    N = int(input())
    li = list(map(str, input().split()))
    deq = deque()
    deq.append(li[0])
    for i in range (1, N):
        if deq[0] >= li[i]:
            deq.appendleft(li[i])
        else:
            deq.append(li[i])
    print(''.join(deq))





