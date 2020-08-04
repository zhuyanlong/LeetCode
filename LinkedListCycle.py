# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

#感觉这道题要好想一些，用快慢指针就可以做到
class Solution:
    def hasCycle(self, head):
        slow=head
        fast=head
        while fast!=None:
            fast=fast.next
            slow=slow.next
            if fast!=None:
                fast=fast.next
                if fast==slow:
                    return True
        return False

def main():
    l=ListNode(0)
    l.next=ListNode(1)
    l.next.next=ListNode(2)
    l.next.next.next=ListNode(3)
    l.next.next.next.next=ListNode(4)
    l.next.next.next.next.next=l
    s=Solution()
    print(s.hasCycle(l))

main()
