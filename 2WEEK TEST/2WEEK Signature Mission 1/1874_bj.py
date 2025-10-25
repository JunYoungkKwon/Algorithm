import sys
input = sys.stdin.readline

ans = []
test = []

N = int(input())
cnt = 1
for i in range(N):
    num = int(input())

    while num >= cnt:
        ans.append(cnt)
        test.append("+")
        cnt += 1

    if ans[-1] == num:
        ans.pop()
        test.append("-")
    else:
        print("NO")
        break
else:
    for a in test:
        print(a)