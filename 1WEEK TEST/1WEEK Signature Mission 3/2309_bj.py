from itertools import combinations

nums  = []
for _ in range(9):
    nums .append(int(input()))

for com in combinations(list, 7):

    if sum(com) == 100:
        for x in sorted(com):
            print(x)
        break



