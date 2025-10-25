T = input()

count0 = 0
count1 = 0

if T[0] == '0':
    count0 += 1
else:
    count1 += 1

for i in range(1, len(T)):
    if T[i] != T[i-1]:
        if T[i] == '0':
            count0 += 1
        else:
            count1 += 1





