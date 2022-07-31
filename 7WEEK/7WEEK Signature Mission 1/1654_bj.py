K, N = map(int, input().split())
light = [int(input()) for _ in range(K)]
lo = 1
hi = max(light)+1
def is_possibel(m):
    cnt = 0
    for li in light:
        cnt += (li // m)
    # print(cnt)
    if cnt >= N:
        return True
    else:
        return False

while lo +1 < hi:
    mid = (lo + hi) // 2
    # print(f'lo = {lo} mid = {mid} hi = {hi}')
    if is_possibel(mid):
        lo = mid
    else:
        hi = mid

print(lo)