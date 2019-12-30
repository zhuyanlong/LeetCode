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
        while tmp.next!=None:
            print(tmp.val)
            tmp=tmp.next
        print(tmp.val)

class Solution:
    def mergeTwoLists(self, l1, l2):
        l=ListNode(0)
        p=l
        while l1!=None and l2!=None:
            if l1.val<l2.val:
                tmp=ListNode(l1.val)
                p.next=tmp
                p=p.next
                l1=l1.next
            else:
                tmp=ListNode(l2.val)
                p.next=tmp
                p=p.next
                l2=l2.next
        if l1==None:
            while l2!=None:
                tmp=ListNode(l2.val)
                p.next=tmp
                p=p.next
                l2=l2.next
        if l2==None:
            while l1!=None:
                tmp=ListNode(l1.val)
                p.next=tmp
                p=p.next
                l1=l1.next
        l.next.printNode()
        return l.next

def main():
    l=ListNode(1)
    l.addNode(2)
    l.addNode(4)
    # l.printNode()
    p=ListNode(1)
    p.addNode(3)
    p.addNode(4)
    # p.printNode()
    s=Solution
    s.mergeTwoLists(None,l,p)

main()

# class Solution:
#     def mergeTwoLists(self, l1, l2):