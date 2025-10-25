import heapq
N = int(input())
# 다솜이가 다른 후보보다 표가 많아져야 함 최소값

vote = [int(input()) for _ in range(N)]

dd = vote[0]

vote_heap = [-v for v in vote[1:]]
heapq.heapify(vote_heap)

count = 0

if N ==1:
    print(0)
else:
    while True:
        max_vote = -vote_heap[0]
        if dd <= max_vote:
            heapq.heapreplace(vote_heap, -max_vote+1)
            count += 1
            dd += 1
        else:
            break
    print(count)




