a = int(input())
b = []
for i in range (a, 3, -1):
    if '4' in str(i) or '7' in str(i):
        if '9' not in str(i) and '8' not in str(i):
            if '6' not in str(i) and '5' not in str(i):
                if '3' not in str(i) and '2' not in str(i):
                    if '1' not in str(i) and '0' not in str(i):
                        b.append(i)
print(max(b))



