from collections import deque

T = int(input())
gears = [deque(map(int, input().strip())) for _ in range(T)]

K = int(input())

for _ in range(K):
    num, d = map(int, input().split())
    num -= 1  # 인덱스 보정

    rotate_dirs = [0] * T
    rotate_dirs[num] = d

    # 왼쪽으로 영향 전파
    for i in range(num - 1, -1, -1):
        if gears[i][2] != gears[i + 1][6]:
            rotate_dirs[i] = -rotate_dirs[i + 1]
        else:
            break

    # 오른쪽으로 영향 전파
    for i in range(num + 1, T):
        if gears[i - 1][2] != gears[i][6]:
            rotate_dirs[i] = -rotate_dirs[i - 1]
        else:
            break

    # 실제 톱니 회전
    for i in range(T):
        if rotate_dirs[i] != 0:
            gears[i].rotate(rotate_dirs[i])

# 최종 점수 계산 (0번 index가 1인지 확인)
answer = sum(1 for i in range(T) if gears[i][0] == 1)
print(answer)
