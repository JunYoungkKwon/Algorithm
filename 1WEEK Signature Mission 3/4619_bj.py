b, n = map(int, input().split())
while not(b == n == 0):
    a = 0
    while abs(b - (a ** n)) > abs(b - ((a + 1) ** n)):
        a += 1
    print(a)
    b, n = map(int, input().split())