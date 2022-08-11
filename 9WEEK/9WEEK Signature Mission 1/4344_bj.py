for _ in range(int(input())):
    N, *score = list(map(int, input().split()))
    mid_score = sum(score) / N
    cnt = 0
    for k in score:
        if k > mid_score:
            cnt += 1
    ans = (cnt / N) * 100
    score = '{:.3f}'.format(round(ans, 3))
    print(f"{score}%")