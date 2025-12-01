
#1번 컴퓨터가 웜 바이러스에 걸렸을 때,
# 1번 컴퓨터를 통해 웜 바이러스에 걸리게 되는 컴퓨터의 수를 첫째 줄에 출력

N = int(input()) #컴퓨터의 수
M = int(input()) #연결된 컴퓨터 쌍의 수
computer = [[] for _ in range(N+1)]
virus = [0] * (N+1)

for _ in range(M):
    A, B = map(int ,input().split())
    computer[A].append(B)
    computer[B].append(A)

for com in computer[1]:
    for co in computer[com]:
        virus[co] = 1



print(sum(virus))



