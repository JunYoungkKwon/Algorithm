N, M = map(int, input().split()) #N일, M번만 통장에서 돈을 빼
money = [int(input()) for _ in range(N)]

low = max(money)
high = sum(money)
answer = 0

while low <= high:
    mid = (low + high) // 2
    cnt = 1

    current = mid


    for m in money:
        if current < m:
            cnt += 1
            current = mid
        current -= m

    # 최소 금액 K를 출력
    if cnt <= M:
        answer = mid
        high = mid - 1
    else:
        low = mid + 1


print(answer)