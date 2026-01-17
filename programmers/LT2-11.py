# [REETCODE] Lowest Common Ancestor of a Binary Tree
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        min_val = min(p.val, q.val)
        max_val = max(p.val, q.val)

        def findCommon(root):
            val = root.val
            if val <= max_val and val >= min_val:
                return root
            elif val > max_val:
                return findCommon(root.left)
            elif val < min_val:
                return findCommon(root.right)

        return findCommon(root)