from collections import deque
deque = deque()
for i in range (1, int(input())+1):
    deque.append(i)

while True:
    if len(deque) > 1:
        deque.popleft()
        deque.append(deque.popleft())
    else:
        print(deque[0])
        break

