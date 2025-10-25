import sys
N = int(input())
s = list(map(int, sys.stdin.readline().split()))
s.sort()
min_s = s[0]
for i in range(1, min_s+1):
    if min_s % i == 0:
        check = 0
        for k in s:
            if k % i == 0:
                check += 1
        if check == len(s):
            print(i)




