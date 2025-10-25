A = 300
B = 60
C = 10

T = int(input())

A_button = int(T / A)
T = T % A
B_button = int(T / B)
T = T % B
C_button = int(T / C)
T = T % C

if T == 0:
    print(A_button, B_button, C_button)
else:
    print(-1)

