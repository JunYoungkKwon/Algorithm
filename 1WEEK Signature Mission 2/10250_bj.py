cnt = int(input())
for _ in range(cnt):
    info = list(map(int, input().split()))

    if info[2] > info[0]:
        if info[2] % info[0] == 0:
            y = info[0]
        else:
            y = info[2] % info[0]
    else:
        y = info[2]

    if info[2] % info[0] == 0:

        x = int(info[2] / info[0])
    else:
        x = int(info[2] / info[0]) + 1
    print(f'{y*100+x}')