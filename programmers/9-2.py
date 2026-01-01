def solution(distance, rocks, n):
    rocks.sort()
    rocks.append(distance)

    left, right = 1, distance
    answer = 0

    while left <= right:
        mid = (left + right) // 2
        prev = 0
        remove = 0

        for rock in rocks:
            if rock - prev < mid:
                remove += 1
            else:
                prev = rock

        if remove <= n:
            answer = mid
            left = mid + 1
        else:
            right = mid - 1

    return answer
