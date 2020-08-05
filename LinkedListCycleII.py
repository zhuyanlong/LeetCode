# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head):
        if head==None:
            return None
        fast=head
        slow=head
        while fast!=None:
            fast=fast.next
            slow=slow.next
            if fast!=None:
                fast=fast.next
                if fast==slow:
                    break
        if fast==None:
            return None
        #这是最关键的点，当两个节点相遇以后，slow从头开始走，再次相遇的时候，就是环开头，我很难想到原因
        slow=head
        while slow!=fast:
            slow=slow.next
            fast=fast.next
        return fast

def main():
    l=ListNode(3)
    l.next=ListNode(2)
    l.next.next=ListNode(0)
    l.next.next.next=ListNode(-4)
    # l.next.next.next.next=ListNode(4)
    l.next.next.next.next=l.next
    s=Solution()
    print(s.detectCycle(l).val)

main()