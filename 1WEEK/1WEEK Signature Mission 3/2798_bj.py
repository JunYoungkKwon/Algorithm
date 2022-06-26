from itertools import combinations
N , M = map(int, input().split())
A = list(map(int, input().split()))
test = []
for com in combinations(A, 3):
    if sum(com) <= M:
        test.append(sum(com))
test.sort()
print(test[-1])

