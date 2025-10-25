from collections import deque

N, K = map(int, input().split())
wheel = deque(['?'] * N)

pos = 0  # 화살표 위치 (항상 인덱스 0)

for _ in range(K):
    S, ch = input().split()
    S = int(S)
    # 시계 방향으로 S칸 회전 → deque는 음수로 회전
    wheel.rotate(S)
    # 화살표가 가리키는 곳은 항상 인덱스 0
    if wheel[0] == '?':
        wheel[0] = ch
    elif wheel[0] != ch:
        print('!')
        exit()

# 중복 알파벳 체크
seen = set()
for c in wheel:
    if c != '?' and c in seen:
        print('!')
        exit()
    seen.add(c)

print(''.join(wheel))
