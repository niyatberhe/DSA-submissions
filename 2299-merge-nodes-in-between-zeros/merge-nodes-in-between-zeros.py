# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current=head
        dumy=ListNode()
        tail=dumy

        while current.next:
            sum_node=ListNode(0)
            while current.next.val!=0:
                sum_node.val+=current.next.val
                current=current.next
            tail.next=sum_node
            tail=tail.next
            current=current.next

        return dumy.next