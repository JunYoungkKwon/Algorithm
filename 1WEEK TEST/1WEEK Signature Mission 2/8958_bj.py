t = int(input())
for _ in range(t):
    case = input()
    sum = 0
    bonus = 0
    for i in case:
        if i == 'O':
            bonus += 1
            sum += bonus
        else:
            bonus = 0
    print(sum)


