while True:
    B, N = map(int, input().split())

    if B == 0 and N == 0:
        exit()

    low, high = 1, B
    min_diff = float("inf")
    best_a = 0

    while low <= high:
        mid = (low+high)//2
        power = mid**N
        diff = abs(power - B)

        if diff < min_diff:
            min_diff = diff
            best_a = mid

        if power < B:
            low = mid + 1
        else:
            high = mid - 1

    print(best_a)


