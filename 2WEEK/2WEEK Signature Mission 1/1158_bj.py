# 요세푸스 -> 배열
# 배열로 구현 하려 했는데 구현이 안됨

N, K = map(int,input().split())
ans = []
ex = [i for i in range(1, N+1)]

cnt = 0

for _ in range(N):
    cnt += K -1
    if cnt >= len(ex):
        cnt = cnt % len(ex)
    ans.append(ex[cnt])
    del ex[cnt]
print(*ans)
