a = list(map(int, input().split()))
mi = min(list(a))

while True:
    cnt = 0
    for i in range(5):
        if mi % a[i] == 0:
            cnt += 1
    if cnt > 2:
        print(mi)
        break
    mi += 1