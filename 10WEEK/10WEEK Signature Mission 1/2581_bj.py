M = int(input())
N = int(input())

sosu_li = []
for i in range(M, N+1):
    sosu = True
    if i > 1:
        for j in range(2, i):
            if i % j == 0:
                sosu = False
                break
        if sosu:
            sosu_li.append(i)

if len(sosu_li) == 0:
    print(-1)
else:
    print(sum(sosu_li))
    print(min(sosu_li))