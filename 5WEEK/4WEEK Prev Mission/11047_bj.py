N, K = map(int, input().split())
coin = [int(input()) for _ in range(N)]
coin.reverse()
ans = 0
for co in coin:
     ans += K // co
     K %= co

print(ans)

