# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.prev = None
        return self.helper(root)

    

    def helper(self,root):
        if root is None:
            return True
        if not self.helper(root.left):
            return False
        print(root.val)
        if (self.prev != None and root.val<=self.prev.val):
            return False
        self.prev = root
        return self.helper(root.right)

        