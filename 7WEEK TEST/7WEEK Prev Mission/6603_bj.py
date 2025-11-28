from itertools import combinations

while True:
    case = list(map(int, input().split()))
    if case[0] == 0:
        break
    for com in combinations(case[1::], 6):
        print(*com)
    print("")

