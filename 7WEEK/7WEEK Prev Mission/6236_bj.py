import sys
input = sys.stdin.readline

N, M = map(int, input().split())
money = []
for _ in range(N):
    money.append(int(input()))
lo = max(money)-1
hi = sum(money)

def is_possible(d):
    cnt = 0
    don = 0
    for li in money:
        if don >= li:
            don -= li
        else:
            cnt += 1
            don = d
            don -= li
    if cnt <= M:
        return True
    else:
        return False

while lo +1 < hi:
    mid = (lo + hi) // 2
    if is_possible(mid):
        hi = mid
    else:
        lo = mid
print(hi)