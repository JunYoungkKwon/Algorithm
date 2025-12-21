def solution(n, lost, reserve):
    lost = set(lost)
    reserve = set(reserve)

    # 1. 여벌이 있지만 도난당한 학생 제거
    both = lost & reserve
    lost -= both
    reserve -= both

    # 2. 작은 번호부터 빌려주기
    for r in sorted(reserve):
        if r - 1 in lost:
            lost.remove(r - 1)
        elif r + 1 in lost:
            lost.remove(r + 1)

    return n - len(lost)

print(solution(5, [1, 2, 4, 5], [2, 3, 4]))
# 5, [1, 2, 4, 5], [2, 3, 4]