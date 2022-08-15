M, N = map(int, input().split())

sosu_li = []
for i in range(M, N+1):
    sosu = True
    if i > 1:
        for j in range(2, i):
            if i % j == 0:
                sosu = False
                break
        if sosu:
            print(i)