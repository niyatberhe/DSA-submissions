# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: ListNode | None) -> ListNode | None:
        dummy=ListNode(0)
        new_cur,cur=dummy,head.next
        while cur and cur.next:
            mergesum=0
            while cur.val!=0:
                mergesum+=cur.val
                cur=cur.next
            new_cur.next=ListNode(mergesum)
            cur=cur.next
            new_cur=new_cur.next
        
        return dummy.next
