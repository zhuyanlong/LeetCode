#这道题目的原始解者对于链表的理解应该来说相当的精确
#你要比较哪个值就一定要确保那个值是存在的，否则一定会出错
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
    def addNode(self,x):
        l=ListNode(x)
        tmp=self
        while tmp.next!=None:
            tmp=tmp.next
        tmp.next=l

    def printNode(self):
        tmp=self
        res=[]
        while tmp.next!=None:
            res.append(tmp.val)
            tmp=tmp.next
        res.append(tmp.val)
        print(res)

#按照正常的思路先来模拟下这道题的解法
class Solution:
    def deleteDuplicates(self, head):
        i=ListNode(0)
        i.next=head
        p=i
        tmp=head
        while p.next!=None:
            while tmp.next and tmp.val==tmp.next.val:
                tmp=tmp.next
            if p.next==tmp:
                p=p.next
                tmp=tmp.next
            else:
                p.next=tmp.next
                tmp=tmp.next
        # i.printNode()
        return i.next

def main():
    l=ListNode(1)
    l.addNode(1)
    l.addNode(1)
    l.addNode(2)
    l.addNode(3)
    l.addNode(4)
    l.addNode(5)
    s=Solution
    s.deleteDuplicates(None,l).printNode()

main()




