dp = [0] *91
n = int(input())

def fib(y):
    if y <= 2:
        return 1
    if dp[y] != 0:
        return dp[y]

    dp[y] = fib(y-1) + fib(y-2)
    return  dp[y]

print(fib(n))


