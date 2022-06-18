num = [int(input()) for _ in range(9)]
maxnum = max(num)
for i in range (9):
    if maxnum == num[i]:
        print(maxnum)
        print(i+1)
