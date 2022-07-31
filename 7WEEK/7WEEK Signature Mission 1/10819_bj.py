from itertools import permutations
N = int(input())
num = list(map(int, input().split()))
perm = permutations(num)
ans = 0

def find_max(list):
    res = 0
    for i in range(len(list)-1):
        res += abs(list[i] - list[i+1])
    return res

for per in perm:
    ans = max(ans, find_max(per))
print(ans)