from collections import deque

def solution(bridge_length, weight, truck_weights):
    time = 0
    bridge = deque([0] * bridge_length)  # 다리 위 상태 (길이만큼 0으로 초기화)
    current_weight = 0                   # 현재 다리 위 총 무게

    for truck in truck_weights:
        while True:
            time += 1
            out = bridge.popleft()       # 한 칸 앞으로 이동
            current_weight -= out

            # 트럭이 올라갈 수 있으면
            if current_weight + truck <= weight:
                bridge.append(truck)     # 트럭 올리기
                current_weight += truck
                break
            else:
                # 못 올라가면 0을 넣고 시간만 흐르게 하기
                bridge.append(0)

    # 마지막 트럭이 완전히 건너는 시간 추가
    time += bridge_length

    return time
