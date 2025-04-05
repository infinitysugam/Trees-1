# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right





class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if len(preorder) == 0:
            return None
        
        root  = TreeNode(preorder[0])

        index = -1
        for i in range(0,len(inorder)):
            if inorder[i]== root.val:
                index = i 
                break
        
        l_inorder = inorder[0:index]
        r_inorder = inorder[index+1:len(inorder)]

        l_preorder = preorder[1:len(l_inorder)+1]
        r_preorder = preorder[len(l_inorder)+1:len(preorder)]


        root.left = self.buildTree(l_preorder,l_inorder)

        root.right = self.buildTree(r_preorder,r_inorder)

        return root

