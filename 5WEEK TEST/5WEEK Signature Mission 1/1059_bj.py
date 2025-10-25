# A와 B는 양의 정수이고, A < B를 만족한다.
# A ≤ x ≤ B를 만족하는 모든 정수 x가 집합 S에 속하지 않는다.
# 집합 S와 n이 주어졌을 때, n을 포함하는 좋은 구간의 개수


L = int(input())
li = sorted(list(map(int, input().split())))
N = int(input())

prev = 0
next_val = 1001

for s in li:
    if s < N:
        prev = s
    elif s > N:
        next_val = s
        break
    elif s == N:
        print(0)
        exit()
ans = (N - prev) * (next_val - N) - 1  # -1: A < B 조건

print(ans)











