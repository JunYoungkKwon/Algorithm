#이전 타일은 점화식 찾기 쉬웠는데..
#이번 건 점화식이 어려워서 참고했음
N = int(input())
cases = [0] * 31
cases[2] = 3

for i in range(4, N+1, 2):
    cases[i] = 2 + cases[i-2] * 3 + sum(cases[:i-2]) * 2
    print(cases[:i-2])

print(str(cases[N]))
