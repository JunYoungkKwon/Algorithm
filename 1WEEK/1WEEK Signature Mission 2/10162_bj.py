time = int(input())
A = B = C = 0
if time % 10 != 0:
    print(-1)
else:
    A = time // 300
    B = (time % 300) // 60
    C = (time % 300) % 60 // 10
    print(A, B, C)

