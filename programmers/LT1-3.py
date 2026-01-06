from itertools import combinations


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        ans.append([])

        for i in range(1, len(nums) + 1):

            for pe in combinations(nums, i):
                ans.append(list(pe))

        return ans


