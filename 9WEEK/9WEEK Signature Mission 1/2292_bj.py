# 1 -> 1
# 2~7 -> 2 1+ 6
# 8~19 -> 3 1 + 18
# 20~37 -> 4 1 + 36
# 38~61 -> 5
# 0 -> 2
# 1 -> 3
def hap(n):
    if n == 0:
        return 1
    else:
        n = n+1
        return n*(n+1)//2
N = int(input())

for n in range(166666667):
    if N == 1:
        print(1)
        break
    if 6*n+2 <= N <= 1+ (6 * hap(n)):
        print(n+2)
        break
