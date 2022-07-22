# while문 돌 때 hap 초기화를 해줘야 된다 깜빡해서 시간 걸림 ㅠ
N, M = map(int, input().split())
trees = list(map(int, input().split()))
start, end = 0, max(trees)
mid = (start + end) // 2
hap = 0
while start + 1 < end:
    hap = 0
    for tree in trees:
        if tree - mid >= 0:
            hap += tree - mid

        else:
            hap += 0

    if hap >= M:
        start = mid
    else:
        end = mid

    mid = (start + end) // 2
print(start)

