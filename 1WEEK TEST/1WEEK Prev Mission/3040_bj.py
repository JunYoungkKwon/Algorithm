from itertools import combinations
case = [int(input()) for _ in range(9)]
for com in combinations(case, 7):
    if sum(com) == 100:
        for res in com:
            print(res)
