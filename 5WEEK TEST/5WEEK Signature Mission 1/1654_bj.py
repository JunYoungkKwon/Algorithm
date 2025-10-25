K, N = map(int, input().split())
li = [int(input()) for _ in range(K)]

low = 1
high = max(li)
max_len = 0


while low <= high:
    mid = (high + low) // 2
    ans = 0

    for i in li:
        ans += (i // mid)

    if ans >= N:
        low = mid + 1
        max_len = max(max_len, mid)
    else:
        high = mid - 1

print(max_len)