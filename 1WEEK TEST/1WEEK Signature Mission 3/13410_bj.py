N, K  =map(int, input().split())
cal = []
for i in range(K+1):
    a = str(N*i)
    rev_a = int(a[::-1])
    cal.append(rev_a)

print(max(cal))
