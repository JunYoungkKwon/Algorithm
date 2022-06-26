H, M = map(int, input().split())
if M - 45 < 0:
    H = H-1
    M = M + 15
    if H < 0:
        H= 23
else:
    M = M-45
print(H, M)