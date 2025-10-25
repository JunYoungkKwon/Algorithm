num = []
for i in range(1, 10001):
    num.append(i)

for i in range(1, 10001):
    sum = i
    for ch in str(i):
        sum += int(ch)
    if num.count(sum) != 0:
        num.remove(sum)

for i in num:
    print(i)



