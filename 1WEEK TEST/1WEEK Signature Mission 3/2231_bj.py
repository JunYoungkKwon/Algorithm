N = int(input())

for i in range(1, N+1):
    sum = 0
    for a in str(i):
        sum += int(a)
    if sum + i == N:
        print(i)
        break
    if N == i:
        print(0)





