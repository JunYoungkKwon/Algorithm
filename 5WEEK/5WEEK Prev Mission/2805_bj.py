N, M = map(int, input().split())
trees = list(map(int, input().split()))
lo, hi = 0, max(trees) #lo는 1부터 주어지는데 0으로 왜 설정한지 생각
mid = (hi + lo) // 2
s= 0
# 절단기 높이를 h로 했을 때 가져가는 나무의 양이 M 이상인가
def is_possible(h):
    global s
    s = 0
    for tree in trees:

        if tree >= h:
            s += tree - h
        else:
            s += 0
    if s >= M:
        return True
    else:
        return False

    # return sum(tree - h if tree >= h else 0 for tree in trees) >= M

while lo + 1 < hi:  # 적절한 벌목 높이를 찾는 알고리즘
    print(f'lo = {lo} mid = {mid}  hi = {hi} ')
    if is_possible(mid):
        lo = mid
    else:
        hi = mid


    mid = (lo + hi) // 2
print(lo)