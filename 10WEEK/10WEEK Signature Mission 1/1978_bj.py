N = int(input())
num = list(map(int, input().split()))
ans = 0
for i in range(N):
    sosu = True
    if num[i] > 1:
        for j in range(2, num[i]):
            if num[i] % j == 0:
                sosu = False
                break
        if sosu:
            ans += 1
print(ans)