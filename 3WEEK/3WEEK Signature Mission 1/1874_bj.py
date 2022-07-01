N = int(input())
stk = []
true = []
is_vpf = True
cnt = 1
for i in range(N):
    num = int(input())
    while cnt <= num:
        stk.append(cnt)
        true.append('+')
        cnt += 1
    if stk[-1] == num:
        stk.pop()
        true.append('-')
    else:
        is_vpf = False

if is_vpf == False:
    print('NO')
else:
    for i in true:
        print(i)