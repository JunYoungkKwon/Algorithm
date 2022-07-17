#순차 탐색으로 진행하면 시간 복잡도 = O(MN)
#이분 탐색으로 진해아면 시간 복잡도 = O((M+N)logN)
from bisect import bisect_left, bisect_right
input()
card = sorted(list(map(int, input().split())))
input()
compare = list(map(int, input().split()))


for i in compare:
     print(bisect_right(card, i) - bisect_left(card, i), end=" ")