N = int(input())
A = 1
B = N
for i in range(1, 2*N, 2):
    print(" " * (B - 1) + "*" * i)
    B = B-1
for i in range((2*N)-3, 0, -2):
    print(" " * A + "*" * i)
    A += 1


