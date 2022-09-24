def solution(queue1, queue2):
    answer = -2
    while True:
        sum1 = sum(queue1)
        sum2 = sum(queue2)
        if sum1 == sum2:
            break
        elif sum1 > sum2:

    return answer

print(solution([3, 2, 7, 2], [4, 6, 5, 1]))
# [3, 2, 7, 2]	[4, 6, 5, 1]	2
# [1, 2, 1, 2]	[1, 10, 1, 2]	7
# [1, 1]	[1, 5]	-1