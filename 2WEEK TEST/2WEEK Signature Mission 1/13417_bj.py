from collections import deque

for _ in range(int(input())):
    deq = deque()
    T = int(input())
    deq.extend(input().split())
    deq_test = deque()
    for i in range(T):

        if not deq_test:
            deq_test.append(deq[i])
        else:
            if deq_test[0] < deq[i]:
                deq_test.append(deq[i])
            else:
                deq_test.appendleft(deq[i])
    print("".join(deq_test))
