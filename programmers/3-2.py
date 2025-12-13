#작업의 소요시간이 짧은 것, 작업의 요청 시각이 빠른 것, 작업의 번호가 작은 것
import heapq
def solution(jobs):
    hq = []
    for i in range(len(jobs)):
        heapq.heappush(hq, (jobs[i][1], jobs[i][0], i))
    print(hq)



    answer = 0
    return answer

solution([[0, 3], [1, 9], [3, 5]])