N = int(input())
score = list(map(int, input().split()))
max_score = max(score)
ans = 0
for sco in score:
    ans += (sco/max_score) * 100
print(ans/N)