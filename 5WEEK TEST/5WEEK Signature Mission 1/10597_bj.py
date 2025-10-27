import sys
sys.setrecursionlimit(10000)

s = sys.stdin.readline().strip()
L = len(s)

# N 추정
if L < 10:
    N = L
else:
    N = 9 + (L - 9) // 2

used = [False] * (N + 1)
ans = []

def backtracking(idx, cnt):
    #인덱스 끝에 돌달하고 모든 숫자 다 사용했으면
    if idx == N and cnt == N:
        print(ans)
    #1자리
    if idx + 1 <N:
        x = int(s[idx])

        if x != 0:

            if 1 <= x <= N and not used[x]:
                used[x] = True
                ans.append(x)
                backtracking(idx+1, cnt+1)
                used[x] = False
                ans.pop()




    #2자리





backtracking(0, 0)

