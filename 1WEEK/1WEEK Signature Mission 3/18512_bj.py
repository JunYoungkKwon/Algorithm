A, B, X, Y = map(int, input().split())

a = [A * i + X for i in range(10000)]
b = [B * i + Y for i in range(10000)]
c = []
mi = -1

for i in range(10000):
    if a[i] in b:
        c.append(A * i + X)
    elif b[i] in a:
        c.append(B * i + Y)

if len(c) == 0:
    print(-1)
else:
    c.sort()
    print(c[0])













