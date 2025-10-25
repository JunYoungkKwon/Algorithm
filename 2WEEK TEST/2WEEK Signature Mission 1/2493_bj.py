N = int(input())
lazer = list(map(int, input().split()))
stk = []
for i in range(N):
    height = lazer[i]
    while stk:


        #스택이 있는데 나보다 높이가 높다면
        if stk[-1][1] >= height:
            print(stk[-1][0], end =" ")
            break



        # 스택이 있는데 나보다 높이가 닞다면 제거
        else:
            # print(0, end =" ")
            stk.pop()

    if stk:
        stk.append((i+1, height))
    else:
        print(0, end=" ")
        stk.append((i + 1, height))