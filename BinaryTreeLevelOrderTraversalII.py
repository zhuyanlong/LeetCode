# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
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

class Solution:
    def levelOrderBottom(self, root):
        res=[]
        queue=[(root,0)]
        if root==None:
            return []
        res.append([root.val])
        while queue:
            tmp=queue[0]
            del queue[0]
            if tmp[0].left!=None:
                queue.append((tmp[0].left,tmp[1]+1))
                if len(res)<=tmp[1]+1:
                    res.insert(0,[queue[-1][0].val])
                else:
                    res[0].append(queue[-1][0].val)
            if tmp[0].right!=None:
                queue.append((tmp[0].right,tmp[1]+1))
                if len(res)<=tmp[1]+1:
                    res.insert(0,[queue[-1][0].val])
                else:
                    res[0].append(queue[-1][0].val)
        print(res)
        return res

def main():
    t=BTree()
    t.treeInsert(3)
    t.treeInsert(1)
    t.treeInsert(2)
    t.treeInsert(4)
    t.treeInsert(5)
    s=Solution()
    s.levelOrderBottom(t.root)

main()
