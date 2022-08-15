while True:
    N = int(input())
    ans = 0
    if N == 0:
        break
    for i in range(N+1, N*2+1):
        sosu = True
        for j in range(2, int(i** 0.5)+1):
            if i % j == 0:
                sosu = False
                break
        if sosu:
            ans += 1
    print(ans)