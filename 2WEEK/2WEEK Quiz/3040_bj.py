from itertools import combinations
case = [int(input()) for _ in range(9)]
for com in combinations(case, 7):
    if sum(com) == 100:
        print(*com, sep="\n")

#FAIL
a = input()
alpha ='abcdefghijklmnopqrstuvwxyz'
for i in alpha:
    print(a.find(i), end= " ")

