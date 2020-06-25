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

    def preorderTravel(self,x):
        if x!=None:
            print(x.val)
            self.preorderTravel(x.left)
            self.preorderTravel(x.right)
        else:
            return
    def postorderTravel(self,x):
        if x!=None:
            self.preorderTravel(x.left)
            self.preorderTravel(x.right)
            print(x.val)
        else:
            return
    def maxDepth(self, root):
        if root==None:
            return 0
        else:
            leftnode=self.maxDepth(self,root.left)
            rightnode=self.maxDepth(self,root.right)
        return max(leftnode+1,rightnode+1)
    def BFS(self,root):
        res=[]
        queue=[root]
        if root!=None:
            res.append(root.val)
        while queue:
            tmp=queue[0]
            del queue[0]
            if tmp.left!=None:
                queue.append(tmp.left)
                res.append(queue[-1].val)
            else:
                res.append(None)
            if tmp.right!=None:
                queue.append(tmp.right)
                res.append(queue[-1].val)
            else:
                res.append(None)
        print(res)


class Solution:
    def isSymmetric(self, root):
        if root!=None:
            if root.left and root.right:
                queue1=[root.left]
                queue2=[root.right]
                if root.left.val!=root.right.val:
                    return False
                while queue1 and queue2:
                    tmp1=queue1[0]
                    del queue1[0]
                    tmp2=queue2[0]
                    del queue2[0]
                    if tmp1.left!=None:
                        queue1.append(tmp1.left)
                        num1=tmp1.left.val
                    else:
                        num1="None"
                    if tmp2.right!=None:
                        queue2.append(tmp2.right)
                        num2=tmp2.right.val
                    else:
                        num2="None"
                    if num1!=num2:
                        return False
                    if tmp1.right!=None:
                        queue1.append(tmp1.right)
                        num1=tmp1.right.val
                    else:
                        num1="None"
                    if tmp2.left!=None:
                        queue2.append(tmp2.left)
                        num2=tmp2.left.val
                    else:
                        num2="None"
                    if num1!=num2:
                        return False
                return True
            elif not root.left and not root.right:
                return True
            else:
                return False
        else:
            return True


def main():
    t=BTree()
    t.treeInsert(1)
    t.treeInsert(2)
    t.treeInsert(3)
    t.treeInsert(4)
    t.treeInsert(5)
    t.BFS(t.root)

main()