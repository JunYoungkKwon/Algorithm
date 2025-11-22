# 경사로는 낮은 칸에 놓으며, L개의 연속된 칸에 경사로의 바닥이 모두 접해야 한다.
# 낮은 칸과 높은 칸의 높이 차이는 1이어야 한다.
# 경사로를 놓을 낮은 칸의 높이는 모두 같아야 하고, L개의 칸이 연속되어 있어야 한다.
#
#
# 경사로를 놓은 곳에 또 경사로를 놓는 경우
# 낮은 칸과 높은 칸의 높이 차이가 1이 아닌 경우
# 낮은 지점의 칸의 높이가 모두 같지 않거나, L개가 연속되지 않은 경우
# 경사로를 놓다가 범위를 벗어나는 경우

import sys
input = sys.stdin.readline

def can_pass(line, L):
    N = len(line)
    used = [False] * N  # 경사로가 이미 놓인 칸 표시
    for i in range(N-1):
        cur = line[i]
        nxt = line[i+1]
        if cur == nxt:
            continue
        elif cur - nxt == 1:
            # 내려막길: i+1 부터 L칸이 nxt와 같고 비어있어야 함
            for j in range(i+1, i+1+L):
                if j < 0 or j >= N:  # 범위 벗어나면 실패
                    return False
                if line[j] != nxt or used[j]:
                    return False
            for j in range(i+1, i+1+L):
                used[j] = True
        elif nxt - cur == 1:
            # 오르막길: i부터 뒤로 L칸이 cur와 같고 비어있어야 함
            for j in range(i, i-L, -1):  # i, i-1, ..., i-L+1
                if j < 0 or j >= N:
                    return False
                if line[j] != cur or used[j]:
                    return False
            for j in range(i, i-L, -1):
                used[j] = True
        else:
            # 높이차 2 이상이면 불가
            return False
    return True

def main():
    N, L = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(N)]

    ans = 0
    # 각 행 검사
    for r in range(N):
        if can_pass(A[r], L):
            ans += 1

    # 각 열 검사 (열을 1차원 리스트로 만들어서 검사)
    for c in range(N):
        col = [A[r][c] for r in range(N)]
        if can_pass(col, L):
            ans += 1

    print(ans)

if __name__ == "__main__":
    main()



