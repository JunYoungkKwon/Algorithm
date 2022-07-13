#이것도 참고 했음..
#점화식 짜는 게 너무 어려움..
#대충 어떤 식으로 코드를 짜야 할 지 알겠는데 아무리 봐도 너무 복잡하게 짜게 됨 ㅠ

N= int(input())
M= int(input())
vips = [int(input()) for _ in range(M)]

DP=[0]*(N+1)

DP[0] =1
DP[1] =1
DP[2] =2

for i in range(3,N+1):
    DP[i] = DP[i-1] + DP[i-2]

ans=1
if M>=1:
    pre=0
    for i in range(M):
        #index slice
        # pre를 기억해줬다가, 이전 값 반영
        ans *= DP[vips[i]-1-pre]
        pre =vips[i]
    #마지막 값 반영
    ans *= DP[N-pre]
else:
    ans = DP[N]
print(ans)