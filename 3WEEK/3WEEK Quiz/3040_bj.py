from itertools import combinations

li = [int(input()) for _ in range(9)]

for com in combinations(li, 7):
    if sum(com) == 100:
        for c in com:
            print(c)