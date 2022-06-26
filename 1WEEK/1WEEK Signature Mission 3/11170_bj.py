N = int(input())
for i in range(N):
    count = 0
    a, b = map(int, input().split())
    for i in range(a, b+1):
        w = str(i)
        count += w.count('0')
    print(count)



