# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        cur=list1
        i=0
        while i<=b:
            cur=cur.next
            i+=1
        cont=cur
        cur=list1
        j=0
        while j<a-1:
            cur=cur.next
            j+=1
        cur.next=list2
        while cur.next:
            cur=cur.next
        cur.next=cont

        return list1
            
