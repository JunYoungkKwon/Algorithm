N = int(input())
ans = 0
for _ in range(N):
    stk = []
    for st in input():
        if stk: #데이터 O
            if stk[-1] == st:
                stk.pop()
            else:
                stk.append(st)

        else: # 데이터 X
            stk.append(st)
    if stk:
        ans += 0
    else:
        ans += 1
print(ans)

