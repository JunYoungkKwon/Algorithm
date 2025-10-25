N = int(input())
cnt = 99
if N <= 99:
    print(N)
else:
    for i in range(100, N+1):
        i = str(i)
        if int(i[0]) - int(i[1]) == int(i[1]) - int(i[2]):
            cnt += 1
    print(cnt)

