# [프로그래머스] 폰켓몬
from itertools import combinations
def solution(nums):
    pick = len(nums) // 2
    s = list(set(nums))
    if pick >= len(s):
        return len(s)
    else:
        return pick



