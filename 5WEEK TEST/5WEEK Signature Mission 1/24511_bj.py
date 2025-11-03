import sys
input = sys.stdin.readline
# 큐 스택 스택 큐
# 1  4
#
# 2 4 7
# 스택이면 기존 숫자 그대로고 큐면 변경

N = int(input())
structure = list(map(int, input().split()))
li = list(map(int, input().split()))
M = int(input())
C = list(map(int, input().split()))
A = []
for num in range(N):
    if structure[num] == 0:
        A.append(li[num])


if A:
    for c in C:
        for i in range(len(A)):
            sa = A[i]
            A[i] = c
            c = sa

        print(c, end =" ")
else:
    print(*C)