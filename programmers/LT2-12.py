# [REETCODE] Binary Tree Maximum Path Sum
class Solution:
    def maxPathSum(self, root):
        ans = root.val

        def dfs(root):
            if not root: return 0

            left = max(dfs(root.left), 0)
            right = max(dfs(root.right), 0)

            nonlocal ans
            ans = max(ans, root.val + left + right)

            return root.val + max(left, right)

        dfs(root)
        return ans
