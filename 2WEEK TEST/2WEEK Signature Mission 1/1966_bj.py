from collections import deque


for _ in range(int(input())):
    N, me = map(int, input().split())
    priorities  = deque(map(int, input().split()))

    ans = 0
    while True:

        if priorities[0] == max(priorities):
            ans += 1
            if me == 0:
                print(ans)
                break

            priorities.popleft()
            me -= 1
        else:
            priorities.append(priorities.popleft())
            if me == 0:
                me = len(priorities) -1
            else:
                me -= 1

# 4개 나는2번째(중요도2)
# 1 2 3 4 me = 2
# 2 3 4 1 me = 1
# 3 4 1 2 me = 3
# 4 1 2 3 me = 2
