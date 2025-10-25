N, K = map(int, input().split())
count = 0

for h in range(N+1):
    for m in range(60):
        for s in range(60):
            time = f"{h}{m}{s}"  # 시,분,초를 이어붙임
            if str(K) in time:   # K가 하나라도 있으면
                count += 1

if str(K) in time:
    count -= 1
print(count)

