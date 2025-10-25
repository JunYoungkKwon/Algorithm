import sys
input = sys.stdin.readline

#나무의 수, 가져가려는 나무의 길이 (1 ≤ N ≤ 1,000,000, 1 ≤ M ≤ 2,000,000,000)
N, M = map(int, input().split())
tree = list(map(int, input().split()))
min = 0
max_tree = max(tree)

ans = 0
while min <= max_tree:
    mid = (max_tree + min) // 2

    got = 0
    #ans는 가져가는 나무 높이 합
    for i in tree:
        if i > mid:
            got +=  i-mid

    if got >= M:
        ans = mid
        min = mid+1
    else:
        max_tree = mid - 1

print(ans)