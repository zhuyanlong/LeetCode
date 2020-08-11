# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

#递归
# class Solution:
#     def postorderTraversal(self, root):
#         res=[]
#         self.dfs(root,res)
#         print(res)

#     def dfs(self,root,res):
#         if root==None:
#             return
#         self.dfs(root.left,res)
#         self.dfs(root.right,res)
#         res.append(root.val)

#栈
class Solution:
    def postorderTraversal(self, root):
        res=[]
        if root==None:
            return res
        stack=[root]
        while stack:
            tmp=stack.pop()
            if tmp.left:
                stack.append(tmp.left)
            if tmp.right:
                stack.append(tmp.right)
            #倒序插值，但是我也确实想不出应该怎么正序插值
            res.insert(0,tmp.val)
        # print(res)
        return res

def main():
    t=TreeNode(1)
    t.right=TreeNode(2)
    t.right.left=TreeNode(3)
    s=Solution()
    s.postorderTraversal(t)

main()