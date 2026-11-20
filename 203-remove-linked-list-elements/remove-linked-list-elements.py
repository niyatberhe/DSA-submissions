# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode | None, val: int) -> ListNode | None:
        lst=[]
        cur=head
        while cur:
            lst.append(cur.val)
            cur=cur.next

        res=[num for num in lst if num!=val]
        dummy=ListNode(0)
        cur=dummy
        for num in res:
            new_node=ListNode(num)
            cur.next=new_node
            cur=cur.next
        
        return dummy.next