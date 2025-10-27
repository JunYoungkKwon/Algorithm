import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
used = [False] * N
max_sum = 0

def backtracking(depth, prev_num, sum):
    global max_sum
    if depth == N:
        max_sum = max(max_sum, sum)
        return
    for i in range(N):
        if not used[i]:
            used[i] = True
            if depth == 0:
                backtracking(depth+1, i, sum)
            else:
                backtracking(depth + 1, i, sum + abs(A[prev_num] - A[i]))
            used[i] = False

backtracking(0, 0, 0)
print(max_sum)
