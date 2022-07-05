# 조합으로도 풀 수 있지만 bfs+백 트래킹을 연습
import sys

def bfs(idx, sum):
    global cnt
    if idx == N:
        return
    sum += li[idx]

    if sum == S:
        cnt +=1

    bfs(idx +1,sum)
    bfs(idx + 1, sum -li[idx])

N, S = map(int, input().split())
li = list(map(int, input().split()))
cnt = 0
bfs(0, 0)
print(cnt)