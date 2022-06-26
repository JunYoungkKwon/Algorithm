N = int(input())

result = 0
for i in range(1,N+1):
    i = str(i)
    for num in '369':
        result += i.count(num)
print(result)
