import heapq


def solution(scoville, K):
    heapq.heapify(scoville)
    answer = 0

    while len(scoville) >= 2:
        min_num = heapq.heappop(scoville)

        # 제일 작은 값이 이미 K 이상이면 끝
        if min_num >= K:
            return answer

        # 두 번째 최소값 꺼냄
        second_min = heapq.heappop(scoville)
        new_scoville = min_num + second_min * 2
        heapq.heappush(scoville, new_scoville)
        answer += 1

    # 마지막 하나만 남은 경우 처리
    # 하나 남아 있는데 그 값도 K보다 작으면 실패
    if scoville and scoville[0] >= K:
        return answer
    else:
        return -1


solution([1, 2, 3, 9, 10, 12],7)