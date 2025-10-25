N = int(input())
case = input()
sum = 0
for i in range(1, 10):
    for n in case:
        if n == str(i):
            sum += i
print(sum)


