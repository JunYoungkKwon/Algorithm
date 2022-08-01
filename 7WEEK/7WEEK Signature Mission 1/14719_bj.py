N, M = map(int, input().split())
rain = list(map(int, input().split()))

ans = 0
for i in range(1, M - 1):
    l = max(rain[:i])
    r = max(rain[i+1:])

    compare = min(l, r)

    if rain[i] < compare:
        ans += compare - rain[i]

print(ans)

