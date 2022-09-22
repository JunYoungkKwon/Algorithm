for _ in range(int(input())):
    A, B = map(int, input().split())
    #최대 공약수 먼저 구하기
    a, b = A, B
    while A != 0:
        B = B % A
        A, B = B, A
    #구한 최대 공약수로 최소 공배수 구하기
    print(a*b // B)

