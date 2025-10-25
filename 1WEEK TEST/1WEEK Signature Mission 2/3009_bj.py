a = []
b = []

for i in range(3):
    x, y = map(int, input().split())
    a.append(x)
    b.append(y)

if a.count(a[0]) == 1:
    x4 = a[0]
elif a.count(a[1]) == 1:
    x4 = a[1]
else:
    x4 = a[2]

if b.count(b[0]) == 1:
    y4 = b[0]
elif b.count(b[1]) == 1:
    y4 = b[1]
else:
    y4 = b[2]

print(x4, y4)