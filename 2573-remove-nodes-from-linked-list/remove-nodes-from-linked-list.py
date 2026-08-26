# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def reverse(head):
            prev,curr=None,head
            while curr:
                temp=curr.next
                curr.next=prev
                prev,curr=curr,temp
            
            return prev

        head=reverse(head)
        current=head
        max_val=current.val
        while current.next:
            if current.next.val<max_val:
                current.next=current.next.next
            else:
                max_val=current.next.val
                current=current.next
        
        return reverse(head)