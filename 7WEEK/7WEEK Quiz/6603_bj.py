from itertools import combinations

cnt = 0
while True:
    a, *b = map(int, input().split())
    if a == 0:
        break
    if cnt:
        print("")
    cnt +=1
    for com in combinations(b, 6):
        print(*com)

