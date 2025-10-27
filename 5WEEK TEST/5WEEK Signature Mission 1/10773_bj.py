import sys
input = sys.stdin.readline

stk = []
for _ in range(int(input())):
    a = int(input())
    stk.pop() if a == 0 else stk.append(a)
print(sum(stk))
