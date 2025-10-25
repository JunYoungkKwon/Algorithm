from itertools import permutations

# 입력 6개 단어
li = [input().strip() for _ in range(6)]
ans = []

# 6개 단어 중 3개를 가로줄로 뽑는 순열
for com in permutations(li, 3):
    # 남은 3개 단어는 세로 후보
    remaining = li.copy()
    for w in com:
        remaining.remove(w)

    # 가로줄 3개
    r1, r2, r3 = com

    # 세로줄 3개 만들기
    c1 = r1[0] + r2[0] + r3[0]
    c2 = r1[1] + r2[1] + r3[1]
    c3 = r1[2] + r2[2] + r3[2]
    vertical_words = [c1, c2, c3]

    # 세로줄이 남은 단어 3개와 일치하는지 확인
    if all(word in remaining for word in vertical_words):
        # 퍼즐 완성 가능
        ans.append((r1, r2, r3))

# 사전순으로 가장 앞서는 퍼즐 출력
if ans:
    ans.sort()
    for row in ans[0]:
        print(row)
else:
    print(0)
