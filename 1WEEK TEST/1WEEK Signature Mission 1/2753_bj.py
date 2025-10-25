N = int(input())

if N % 4 == 0 and not N % 100 == 0:
    print(1)
elif N % 4 == 0 and N % 400 == 0:
    print(1)
else:
    print(0)


