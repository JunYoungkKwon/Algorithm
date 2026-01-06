from itertools import combinations


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        li = []
        ans = []
        for a in range(1, n + 1):
            li.append(a)

        for co in combinations(li, k):
            ans.append(list(co))
        return ans
