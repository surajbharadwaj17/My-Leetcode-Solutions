#
# @lc app=leetcode id=538 lang=python3
#
# [538] Convert BST to Greater Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self) -> None:
        self.total = 0
        
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        if root:
            self.convertBST(root.right)
            self.total += root.val
            root.val = self.total

            self.convertBST(root.left)

        return root
        
# @lc code=end

