# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

#dfs递归法，因为要构造子序列所以空间复杂度极高，时间复杂度低
class Solution:
    def sortedArrayToBST(self, nums):
        if len(nums)==0:
            return
        root=TreeNode(nums[len(nums)//2])
        self.leftdfs(nums[:len(nums)//2],root)
        self.rightdfs(nums[len(nums)//2+1:],root)
        return root

    def leftdfs(self,nums,t):
        if len(nums)==0:
            return
        if len(nums)==1:
            t.left=TreeNode(nums[0])
            return
        t.left=TreeNode(nums[len(nums)//2])
        self.leftdfs(nums[:len(nums)//2],t.left)
        self.rightdfs(nums[len(nums)//2+1:],t.left)

    def rightdfs(self,nums,t):
        if len(nums)==0:
            return
        if len(nums)==1:
            t.right=TreeNode(nums[0])
            return
        t.right=TreeNode(nums[len(nums)//2])
        self.leftdfs(nums[:len(nums)//2],t.right)
        self.rightdfs(nums[len(nums)//2+1:],t.right)

def PrintTree(root):
    stack=[root]
    while stack:
        tmp=stack.pop()
        print(tmp.val)
        if tmp.left:
            stack.append(tmp.left)
        if tmp.right:
            stack.append(tmp.right)

def main():
    nums=[-10,-3,0,5,9]
    s=Solution()
    root=s.sortedArrayToBST(nums)
    print(root.left.val)
    print(root.left.left.val)
    print(root.right.val)
    print(root.right.left.val)
    # PrintTree(root)

main()