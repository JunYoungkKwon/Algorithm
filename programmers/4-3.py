def solution(citations):
    citations.sort()
    low = min(citations)
    high = max(citations)

    ans = 0
    while low <= high:
        # mid값이 h임
        chk = 0
        mid = (low + high) // 2

        for a in citations:
            if mid <= a:
                chk += 1
        if chk >= mid:
            ans = mid
            low = mid + 1
        else:
            high = mid - 1
    return ans

solution([3, 0, 6, 1, 5])