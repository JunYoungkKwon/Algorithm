for _ in range(3):
    ans = 0
    li = list(map(int, input().split()))
    for num in li:
        if num == 1:
            ans += 1
    if ans == 4:
        print('E')
    elif ans == 3:
        print('A')
    elif ans == 2:
        print('B')
    elif ans == 1:
        print('C')
    else:
        print('D')

