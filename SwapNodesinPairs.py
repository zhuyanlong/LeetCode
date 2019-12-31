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
    def swapPairs(self, head):
        dummy=ListNode(0)
        dummy.next=head
        if head.next==None or head==None:
            # print("Y")
            return head
        p=dummy
        while p.next and p.next.next:
            tmp=p.next.next
            p.next.next=tmp.next
            tmp.next=p.next
            p.next=tmp
            p=tmp.next
        return dummy.next


def main():
    l=ListNode(1)
    l.addNode(2)
    l.addNode(3)
    l.addNode(4)
    # l.addNode(5)
    s=Solution
    s.swapPairs(None,l).printNode()
    # l.printNode()

main()
