# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sumNumbers(self, root):
        res=[]
        if root==None:
            return 0
        stack=[(root,0)]
        val=[]
        while stack:
            tmp=stack.pop()
            #节点层次不对，出栈
            while len(val)!=tmp[1]:
                val.pop()
            val.append(str(tmp[0].val))
            if tmp[0].left:
                stack.append((tmp[0].left,tmp[1]+1))
            if tmp[0].right:
                stack.append((tmp[0].right,tmp[1]+1))
            # 遍历到叶子节点
            if not tmp[0].left and not tmp[0].right:
                res.append(int("".join(val)))
        s=0
        for item in res:
            s+=item
        return s


def main():
    t=TreeNode(4)
    t.left=TreeNode(9)
    t.right=TreeNode(0)
    t.left.left=TreeNode(5)
    t.left.right=TreeNode(1)
    s=Solution()
    print(s.sumNumbers(t))

main()