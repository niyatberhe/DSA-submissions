# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        current=list1
        idx=0

        while idx<a-1:
            current=current.next
            idx+=1

        snap=current
        while idx<=b:
            current=current.next
            idx+=1

        snap.next=list2

        while list2.next:
            list2=list2.next
        list2.next=current

        return list1