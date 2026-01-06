from itertools import permutations


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        for per in permutations(nums, len(nums)):
            ans.append(list(per))
        return ans
