# 스택으로 푸는 것도 알겠고 어떻게 구현 해야 될 지 정했음
# 그러나 ans의 갯수를 구하는 로직을 정하는게 어려웠음 레이저로 잘릴 떼, 선이 끝날 때에 관한 걸 논리적으로 생각을 못 함
li = list(input())
ans = 0
stk = []

for i in range(len(li)):
    if li[i] == '(':
        stk.append('(')

    else:
        if li[i-1] == '(':
            stk.pop()
            ans += len(stk)

        else:
            stk.pop()
            ans += 1

print(ans)


