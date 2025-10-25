from collections import deque
ans = []
origin = []
for i in range(int(input())):
    deq = deque(map(int, input().split()))

    if i == 0:
        origin = deque(deq)

    while deq:
        a = deq[0]
        ans.append(a)
        deq.popleft()
        # a= 3
        if a > 0:
            deq.rotate(a-1)

        else:
            deq.rotate(-a)

for ch in ans:
    print(origin.index(ch)+1, end = " ")
