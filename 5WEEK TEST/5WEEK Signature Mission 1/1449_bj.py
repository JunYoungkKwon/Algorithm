# 파이프에서 물이 새는 곳은 신기하게도 가장 왼쪽에서 정수만큼 떨어진 거리만 물이 샌다.
# 항승이는 길이가 L인 테이프를 무한개 가지고 있다.
# 항승이는 항상 물을 막을 때, 적어도 그 위치의 좌우 0.5만큼 간격을 줘야 물이 다시는 안 샌다고 생각한다.
#
# 첫째 줄에 물이 새는 곳의 개수 N과 테이프의 길이 L
# 입력
n, l = map(int, input().split())
positions = list(map(int, input().split()))

positions.sort()
count = 0
i = 0

while i < n:
    count += 1
    # 테이프 덮는 범위: 현재 위치 -0.5 ~ 현재 위치 + L -0.5
    end = positions[i] + l - 0.5
    i += 1
    # 범위 안에 있는 위치는 건너뛰기
    while i < n and positions[i] <= end:
        i += 1

print(count)