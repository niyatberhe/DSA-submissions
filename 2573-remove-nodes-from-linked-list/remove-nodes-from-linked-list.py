# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        lst=[]
        current=head
        while current:
            while lst and current.val>lst[-1]:
                lst.pop()
            lst.append(current.val)
            current=current.next

        dumy=ListNode()
        ts=dumy
        for n in lst:
            ts.next=ListNode(n)
            ts=ts.next

        return dumy.next