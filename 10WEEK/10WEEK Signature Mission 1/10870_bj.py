n = int(input())
s = [0, 1]
for i in range(2, n + 1):
    s.append(s[i - 1] + s[i - 2])
print(s[n])
# N = int(input())
# cache = [0]
# def dp(N):
#     if N <= 1:
#         return cache[N]
#     cache[N] = dp(N-1) + dp(N-2)
#     return cache[N]
#
# print(dp(N))

