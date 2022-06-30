# 에러 처리가 아직도 미숙 함 에러 처리를 완벽하게 못해서 논리적으로 더 사고하고 코드를 짜야 함
N, M = map(int, input().split())
stk = [[] for _ in range(7)]
ans = 0

for _ in range(N):
    a, b = map(int, input().split())
    if stk[a]:
        while stk[a]:
            if stk[a][-1] < b:
                stk[a].append(b)
                ans += 1
                break
            elif stk[a][-1] == b:
                break
            else:
                stk[a].pop()
                ans += 1

        if not stk[a]:
            stk[a].append(b)
            ans += 1

    else:
        stk[a].append(b)
        ans += 1

print(ans)

