#코드 참고용으로 베낀 것
#내가 직접 코딩 못했음
from collections import deque

N, K = input().split()

M = len(N)
K = int(K)
v_chk = [[False] * 11 for i in range(1000001)]
q = deque()
q.append([[ch for ch in N], 0])

v_chk[int(N)][0] = True


def swap(N, idx1, idx2):
    temp = N[idx1]
    N[idx1] = N[idx2]
    N[idx2] = temp


answer = -1


def bfs():
    ans = -1
    while q:
        n, cnt = q.popleft()
        if cnt == K:
            ans = max(ans, int("".join(n)))
            continue
        for i in range(M):
            for j in range(i + 1, M):
                if i == 0 and n[j] == '0':
                    continue
                swap(n, i, j)
                n_int = int(''.join(n))
                if not v_chk[n_int][cnt + 1]:
                    v_chk[n_int][cnt + 1] = True
                    q.append([n.copy(), cnt + 1])
                swap(n, i, j)
    return ans


answer = bfs()
print(answer)