from collections import deque

def solution(priorities, location):
    deq = deque((p, i) for i, p in enumerate(priorities))
    ans = []

    while deq:
        p, l = deq.popleft()
        # 남아있는 프로세스 중 더 높은 우선순위가 있다면
        if deq and p < max(x[0] for x in deq):
            deq.append((p, l))  # 뒤로 보냄
        else:
            ans.append(l)
            if l == location:  # 목표 위치 프로세스면 종료
                return len(ans)

# 실행 예시
print(solution([2, 1, 3, 2], 2))  # 1
