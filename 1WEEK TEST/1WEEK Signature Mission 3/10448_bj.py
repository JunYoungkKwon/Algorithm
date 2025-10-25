from itertools import combinations_with_replacement

T = int(input())
dic = []
for i in range(1, 50):
    dic.append(i*(i+1)//2)

for _ in range(T):
    N = int(input())
    found = False
    for com in combinations_with_replacement(dic, 3):
        if sum(com) == N:
            found = True
            break

    print(1 if found else 0)


