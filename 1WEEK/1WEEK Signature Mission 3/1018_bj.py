N, M = map(int, input().split())
li = []
mini = []

for _ in range(N):
    li.append(input())

print(li)

for i in range (N-7):
    for j in range (M-7):
        c1 = 0
        c2 = 0

        for k in range(i, i+8):
            for l in range(j, j+8):
                if (k+l) % 2 == 0:
                    if li[k][l] == 'W':
                        c1 += 1
                    else:
                        c2 += 1
                else:
                    if li[k][l] == 'B':
                        c1 += 1
                    else:
                        c2 += 1
        mini.append(min(c1, c2))
print(min(mini))