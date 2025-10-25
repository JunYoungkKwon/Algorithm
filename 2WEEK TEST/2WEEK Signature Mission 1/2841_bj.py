import sys
input = sys.stdin.readline
#손가락으로 프렛을 한 번 누르거나 떼는 것을 손가락을 한 번 움직였다고 한다

N, P = map(int, input().split())
stk = [[] for _ in range(7)]
cnt = 0
# N= 500000
for i in range(N):
    line, pret = map(int, input().split())

    # line번 스택에 있을 때
    if stk[line]:
        while stk[line]:
            if stk[line][-1] < pret:
                stk[line].append(pret)
                cnt += 1
                break

            elif stk[line][-1] > pret:
                stk[line].pop()
                cnt += 1
                if not stk[line]:
                    stk[line].append(pret)
                    cnt += 1
                    break
            else:
                break


    #line번 스택에 아무것도 없을 때
    else:
        stk[line].append(pret)
        cnt += 1

print(cnt)