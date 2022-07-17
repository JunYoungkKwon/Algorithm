# 띄어쓰기를 해서 출력 했었는데 답은 그게 아님.. ㅎㅎ.. 잘 확인하고 하자!
A, B = map(str, input().split())
ans = [["."] * len(A) for _ in range(len(B))]
a, b = 0, 0
tf = False
for i in range (len(A)):
    for j in range (len(B)):
        if A[i] == B[j]:
            tf = True
            a = i
            b = j
            break
    if tf:
        break

for i in range (len(B)):
    ans[i][a] = B[i]
for j in range (len(A)):
    ans[b][j] = A[j]
for i in range (len(B)):
    print(''.join(s for s in ans[i]))

