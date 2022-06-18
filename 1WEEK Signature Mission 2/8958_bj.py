cnt = int(input())
arr = []
for _ in range(cnt):
    res = input()
    score = 0
    sum_score = 0
    for i in range (len(res)):
        if res[i] == "O":
            score += 1
            sum_score += score
        else:
            score = 0
    print(sum_score)

