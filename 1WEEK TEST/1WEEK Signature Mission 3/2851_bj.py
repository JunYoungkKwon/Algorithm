mush = [int(input()) for _ in range(10)]

total = 0
for a in mush:
    total += a
    if total >= 100:
        # 거리 비교, 같으면 더 큰 값을 선택
        if abs(100 - total) <= abs(100 - (total - a)):
            print(total)
        else:
            print(total - a)
        break
else:
    print(total)
