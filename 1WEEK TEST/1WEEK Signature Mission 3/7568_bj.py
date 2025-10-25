N = int(input())
wei = []
hei = []
grade = []
for i in range(N):
    weight, height = map(int, input().split())
    wei.append(weight)
    hei.append(height)

for n in range(N):
    gra = 1
    for k in range(N):
        if wei[n] < wei[k] and hei[n] < hei[k]:
            gra += 1
    grade.append(gra)
print(*grade)
