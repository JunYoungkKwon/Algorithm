def solution(n, times):
    left = 1
    right = max(times) * n
    answer = right

    while left <= right:
        mid = (left + right) // 2

        total = 0
        for t in times:
            total += mid // t

        if total >= n:  # 모두 처리 가능
            answer = mid
            right = mid - 1
        else:           # 시간 부족
            left = mid + 1

    return answer
