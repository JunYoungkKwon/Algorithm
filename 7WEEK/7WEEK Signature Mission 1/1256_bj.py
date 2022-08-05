import math
N,M,K = map(int,input().split())
DP=[[1]*(M+1) for _ in range(N+1)]

for i in range(1,N+1):
    for j in range(1,M+1):
        DP[i][j] = DP[i-1][j] + DP[i][j-1]
# for k in range(N+1):
#     print(*DP[k])

if DP[N][M]<K:
    print(-1)
else:
    word=""
    while True:
        if N==0 or M==0:
            word+="z"*M
            word+="a"*N
            break
        #기준은 , a로 시작하냐 ,안하냐이다.
        flag = DP[N-1][M]
        if K<=flag:
            word+="a"
            N-=1
        else:
            word +="z"
            M-=1
            K-=flag
    print(word)