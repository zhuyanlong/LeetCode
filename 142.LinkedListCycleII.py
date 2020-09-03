# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head):
        if head==None:
            return
        hnode=ListNode(0)
        hnode.next=head
        fast=hnode
        slow=hnode
        while fast!=None:
            slow=slow.next
            fast=fast.next
            if fast!=None:
                fast=fast.next
            if slow==fast:
                break
            # print(slow.val,fast.val)
        t=hnode
        while fast!=None:
            t=t.next
            fast=fast.next
            if t==fast:
                return t
        return

def PrintNode(head):
    tmp=head
    res=[]
    while tmp!=None:
        if tmp not in res:
            res.append(tmp)
            tmp=tmp.next
        else:
            break
    return res

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
