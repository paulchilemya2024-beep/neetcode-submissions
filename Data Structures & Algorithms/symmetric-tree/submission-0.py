# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode | None) -> bool:
        if not root:
            return True
        
        return self._is_mirror(root.left, root.right)
    def _is_mirror(self,tree1,tree2):
        #Base Case
        if not tree1 and not tree2:
            return True
        if not tree1 or not tree2 or tree1.val != tree2.val:
            return False
        
        return self._is_mirror(tree1.left,tree2.right) and self._is_mirror(tree1.right,tree2.left)

        

        

        