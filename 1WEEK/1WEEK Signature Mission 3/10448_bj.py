from itertools import product
N = int(input())
case =[(i**2 + i) // 2 for i in range(1, 45)]
res = []
#중복 순열이 가능해서 product
for com in product(case, repeat = 3):
    res.append(str(sum(com)))

for _ in range(N):
    num = input()
    if num in res:
        print(1)
    else:
        print(0)