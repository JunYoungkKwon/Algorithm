from math import gcd

x = int(input())

if x == 2:
    a, b = map(int, input().split())
    gcdRes = gcd(a, b)

if x == 3:
    a, b, c = map(int, input().split())
    gcdRes = gcd(a, b, c)

for i in range(1, gcdRes +1):
    if gcdRes % i == 0:
        print(i)

