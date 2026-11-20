# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: ListNode | None) -> ListNode | None:
        length=0
        cur=head
        while cur:
            length+=1
            cur=cur.next

        mid=(length//2)
        cur=head
        while mid>0:
            cur=cur.next
            mid-=1

        return cur