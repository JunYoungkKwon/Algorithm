y = [False] * 101
x = [False] * 101
N = int(input())
ans = (100 * N)

for _ in range(N):
    x_pos, y_pos = map(int, input().split())
    cnt_x, cnt_y = 0, 0

    for i in range(x_pos, (10+x_pos)):
        if not x[i]:
            x[i] = True
        else:
            cnt_x += 1


    for j in range(y_pos, (10+y_pos)):
        if not y[j]:
            y[j] = True
        else:
            cnt_y += 1


    ans -= (cnt_x * cnt_y)

print(ans)


