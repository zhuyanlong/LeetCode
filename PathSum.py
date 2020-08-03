# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        return self.dfs(root,sum)

    def dfs(self,root,sum):
        #截至条件
        if root==None:
            return False
        #遍历到叶子节点
        if root.left==None and root.right==None and root.val==sum:
            return True
        #其他情况
        return self.dfs(root.left,sum-root.val) or self.dfs(root.right,sum-root.val)

def main():
    l=TreeNode(val=5)
    l.left=TreeNode(val=4)
    l.right=TreeNode(val=8)
    l.left.left=TreeNode(val=11)
    l.left.left.left=TreeNode(val=7)
    l.left.left.right=TreeNode(val=2)
    l.right.left=TreeNode(val=13)
    l.right.right=TreeNode(val=4)
    l.right.right.right=TreeNode(val=1)
    s=Solution()
    sum=22
    print(s.hasPathSum(l,sum))

main()