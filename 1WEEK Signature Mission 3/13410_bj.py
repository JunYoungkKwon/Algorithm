N, K = map(int, input().split())
case = [int(str(N * i)[::-1]) for i in range(1, K+1)]
print(max(case))