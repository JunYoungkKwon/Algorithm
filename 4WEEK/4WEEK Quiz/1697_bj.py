```python
# 빠른 시간이라서 bfs
while 덱이 빌 때 까지:
    현재 좌표 , 시간 = 덱에서 왼쪽부터 뽑은 값
    if 수빈 = 동생:
        시간 출력
        return

    for 다음위치 in (x-1, x+1, x * 2):
        if 방문 X and 범위 내 값이면:
            다음위치 방문 = True
            덱에 위치 append


print 최종 결과값
```

        










