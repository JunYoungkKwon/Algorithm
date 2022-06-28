N = int(input())
first = int(input())
ans = 0
buy = [int(input()) for _ in range (N-1)]
if N ==1:
    print(ans)
else:
    while True:
        buy.sort(reverse=True)
        if buy[0] >= first:
            buy[0] -= 1
            first += 1
            ans += 1
        else:
            print(ans)
            break