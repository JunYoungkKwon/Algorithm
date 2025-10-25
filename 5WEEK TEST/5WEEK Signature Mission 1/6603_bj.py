from itertools import combinations
while True:
    data = list(map(int, input().split()))
    N = data[0]
    if N == 0:
        break
    lst = data[1:]
    ls = []
    for com in combinations(lst, 6):
        ls.append(com)

    for i in ls:
        print(*i)
    print()


