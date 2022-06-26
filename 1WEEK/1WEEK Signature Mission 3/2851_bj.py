X = [int(input()) for _ in range(10)]
sum = 0
li = []
for i in X:
    if sum <= 100:
        sum += i
        li.append(sum)
    elif sum > 100:
        break
if abs(100 - li[-1]) <= abs(100 - li[-2]):
    print(li[-1])
else:
    print(li[-2])