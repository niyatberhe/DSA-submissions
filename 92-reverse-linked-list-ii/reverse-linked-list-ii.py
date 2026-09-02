# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dumy=ListNode(0,head)
        prev=dumy
        curr=dumy.next
        for i in range(left-1):
            prev=prev.next
            curr=curr.next
        left_prev=prev
        prev=None

        for i in range(right-left+1):
            nxt=curr.next
            curr.next=prev
            prev=curr
            curr=nxt

        left_prev.next.next=curr
        left_prev.next=prev

        return dumy.next