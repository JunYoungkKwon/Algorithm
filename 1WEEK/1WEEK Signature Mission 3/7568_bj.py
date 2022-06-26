N = int(input())
li = []
for _ in range(N):
    wei, hei = map(int, input().split())
    li.append((wei, hei))

for i in range(N):
    cnt = 1
    for j in range(N):
        if li[i][0] < li[j][0] and li[i][1] < li[j][1]:
            cnt += 1
    print(cnt, end=" ")