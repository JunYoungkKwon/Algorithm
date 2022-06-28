from collections import deque

N = int(input())
deq = deque(i for i in range(1, N+1))
move = deque(map(int, input().split()))
remove = [deq.popleft()]
re = move[0]
move.popleft()
while deq:

    if re > 0:
        deq.rotate(-(re-1))
        move.rotate(-(re - 1))

    else:
        deq.rotate(-re)
        move.rotate(-re)

    remove.append(deq.popleft())
    re = move.popleft()

print(*remove)