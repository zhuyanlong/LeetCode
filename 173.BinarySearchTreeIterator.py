# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class BSTIterator:
    def __init__(self, root):
        self.nums=[]
        self.inorderTraversal(root)
        self.cur=0

    def next(self):
        """
        @return the next smallest number
        """
        self.cur+=1
        return self.nums[self.cur-1]

    def hasNext(self):
        """
        @return whether we have a next smallest number
        """
        return self.cur!=len(self.nums)

    def inorderTraversal(self,root):
        if root==None:
            return
        self.inorderTraversal(root.left)
        self.nums.append(root.val)
        self.inorderTraversal(root.right)


def main():
    t=TreeNode(7)
    t.left=TreeNode(3)
    t.right=TreeNode(15)
    t.right.left=TreeNode(9)
    t.right.right=TreeNode(20)
    s=BSTIterator(t)
    # print(s.nums)
    print(s.next())
    print(s.next())
    print(s.hasNext())
    print(s.next())
    print(s.hasNext())
    print(s.next())
    print(s.hasNext())
    print(s.next())
    print(s.hasNext())

main()
# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()