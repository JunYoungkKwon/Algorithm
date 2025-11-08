N, M = map(int, input().split())
tree_li = list(map(int, input().split()))

low = 0
high = max(tree_li)

while low <= high:
    mid = (low + high) // 2
    hap = 0

    for tree in tree_li:
        if tree > mid:
            hap += (tree - mid)

    if hap >= M:
        low = mid + 1
    else:
        high = mid - 1


print(high)

