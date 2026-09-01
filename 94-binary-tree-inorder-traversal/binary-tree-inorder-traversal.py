# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result=[]
        stk=[]
        cur_node=root

        while cur_node or stk:
            while cur_node:
                stk.append(cur_node)
                cur_node=cur_node.left
            cur_node=stk.pop()
            result.append(cur_node.val)
            cur_node=cur_node.right

        return result