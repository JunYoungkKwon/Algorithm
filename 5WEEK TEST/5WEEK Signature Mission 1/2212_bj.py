sensor = int(input())
K = int(input())
sensor_li = sorted(list(map(int, input().split())))


sensor_distance = []
for i in range(sensor-1):
    sensor_distance.append(sensor_li[i+1] -sensor_li[i])

if K >= sensor:
    print(0)
else:
    for i in range(K - 1):
        if sensor_distance:  # 리스트가 비어있지 않을 때만 제거
            sensor_distance.remove(max(sensor_distance))
    print(sum(sensor_distance))
