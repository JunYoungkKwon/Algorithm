alpha ="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
stk = []
res = []
dic = {}
N = int(input())
case = input()
for i in range(N):
    res.append(int(input()))

for i in range(len(res)):
    dic[alpha[i]] = res[i]

for i in case:
    if i in alpha:
       stk.append(dic[i])
    else:
        a = stk.pop()
        b = stk.pop()
        if i == '+':
            stk.append(b + a)
        elif i == '-':
            stk.append(b - a)
        elif i == '*':
            stk.append(b * a)
        elif i == '/':
            stk.append(b / a)

print(f'{stk[0]:0.2f}')