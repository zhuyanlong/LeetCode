# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

#这道题可以直接根据根节点来判断

class BTree:
    def __init__(self):
        self.root=None
    def treeInsert(self,value):
        #用来定位待插入节点的父节点
        y=None
        x=self.root
        t=TreeNode(value)
        while x!=None:
            y=x
            if t.val<x.val:
                x=x.left
            else:
                x=x.right
        if y==None:
            self.root=t
        else:
            if t.val<y.val:
                y.left=t
            else:
                y.right=t
    def inorderTravel(self,x):
        if x!=None:
            self.inorderTravel(x.left)
            print(x.val)
            self.inorderTravel(x.right)
        else:
            return

#迭代法
# class Solution:
#     def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
#         maxval=0
#         minval=0
#         if p.val>q.val:
#             maxval=p.val
#             minval=q.val
#         else:
#             maxval=q.val
#             minval=p.val
#         tmp=root
#         while tmp!=None:
#             if maxval>=tmp.val and minval<=tmp.val:
#                 return tmp
#             else:
#                 if minval>=tmp.val:
#                     tmp=tmp.right
#                 elif maxval<=tmp.val:
#                     tmp=tmp.left
#         return None

#递归法
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if p.val>root.val and q.val>root.val:
            return self.lowestCommonAncestor(root.right,p,q)
        elif p.val<root.val and q.val<root.val:
            return self.lowestCommonAncestor(root.left,p,q)
        else:
            return root

def main():
    t=BTree()
    t.treeInsert(6)
    t.treeInsert(2)
    t.treeInsert(8)
    t.treeInsert(0)
    t.treeInsert(4)
    t.treeInsert(7)
    t.treeInsert(9)
    t.treeInsert(3)
    t.treeInsert(5)
    s=Solution()
    print(s.lowestCommonAncestor(t.root,t.root.left,t.root.left.right).val)
    # t.inorderTravel(t.root)

main()
