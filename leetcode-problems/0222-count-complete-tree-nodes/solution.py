class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        # counting 1 for every node that is not None
        return 1 + self.countNodes(root.left) + self.countNodes(root.right) if root else 0
