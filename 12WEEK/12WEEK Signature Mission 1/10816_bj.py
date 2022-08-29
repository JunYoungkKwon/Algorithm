from collections import defaultdict
N = int(input())
card= list(map(int, input().split()))
M = int(input())
card_ans= list(map(int, input().split()))
defa = defaultdict(int)

for ca in card:
    defa[ca] += 1

for ca in card_ans:
    print(defa[ca], end=" ")