from itertools import combinations
N, M = map(int, input().split())
card = list(map(int, input().split()))

min_diff = float("inf")
best_card = 0
for com in combinations(card, 3):
    if sum(com) <= M:
        diff = M - sum(com)

        if diff < min_diff:
            min_diff = diff
            best_card = sum(com)


print(best_card)