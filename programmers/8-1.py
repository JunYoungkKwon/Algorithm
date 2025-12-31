def solution(numbers, target):
    answer = 0
    n = len(numbers)

    def dfs(idx, total):
        nonlocal answer

        # 모든 숫자를 다 사용한 경우
        if idx == n:
            if total == target:
                answer += 1
            return

        # + 선택
        dfs(idx + 1, total + numbers[idx])
        # - 선택
        dfs(idx + 1, total - numbers[idx])

    dfs(0, 0)
    return answer
