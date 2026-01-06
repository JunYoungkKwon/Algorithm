#후보키from collections import Counter
from itertools import combinations

def solution(relation):
    n = len(relation[0]) #인적사항 수
    l = len(relation) #학생의 수
    visited = [False] * n #후보키 체크
    answer = 0

    #유일성 키 구하기
    for x in range(n):
        cnt = Counter()
        for y in range(l):
            #이미 값이 있다면 후보키 X
            if cnt[relation[y][x]] :
                continue
            else:
                cnt[relation[y][x]] += 1
        #유일성 후보키
        if len(cnt) == l:
            visited[x] = True
            answer += 1


from itertools import combinations


def solution(relation):
    row = len(relation)
    col = len(relation[0])

    candidate_keys = []

    for r in range(1, col + 1):
        for comb in combinations(range(col), r):

            if any(set(key).issubset(comb) for key in candidate_keys):
                continue

            seen = set()
            for i in range(row):
                seen.add(tuple(relation[i][c] for c in comb))

            if len(seen) == row:
                candidate_keys.append(comb)

    return len(candidate_keys)





