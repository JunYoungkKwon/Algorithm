a = [int(input()) for _ in range(9)]
max = max(a)
for i in range(9):
    if max == a[i]:
        print(max)
        print(i+1)
