def solution(name):
    answer = 0
    n = len(name)

    # 1. 상하 이동 비용
    for c in name:
        answer += min(ord(c) - ord('A'), ord('Z') - ord(c) + 1)

    # 2. 좌우 이동 최소값
    move = n - 1  # 기본: 오른쪽으로만 이동

    for i in range(n):
        next_i = i + 1
        while next_i < n and name[next_i] == 'A':
            next_i += 1

        # 오른쪽 갔다가 돌아오기
        move = min(move, i * 2 + (n - next_i))

        # 왼쪽 갔다가 다시 오른쪽
        move = min(move, (n - next_i) * 2 + i)

    return answer + move
