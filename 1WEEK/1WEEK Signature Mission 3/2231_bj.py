num = int(input())
hap = 0
for i in range(1, num+1):
    N = list(map(int, str(i)))
    hap = i + sum(N)
    if num == hap:
        print(i)
        break

    if i == num:
        print(0)





