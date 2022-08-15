N = int(input())
i=2
if N > 1:
    while N > 1:
        if N % i == 0:
            N = N // i
            print(i)
        else:
            i += 1
