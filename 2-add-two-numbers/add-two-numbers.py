# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
        dummy=ListNode()
        cur=dummy
        power_10,l1_num=0,0
        while l1:
            l1_num+=((l1.val)*10**(power_10))
            l1=l1.next
            power_10+=1
        
        power_10,l2_num=0,0
        while l2:
            l2_num+=((l2.val)*10**(power_10))
            l2=l2.next
            power_10+=1

        sum_string=str(l2_num+l1_num)[::-1]
        for num in sum_string:
            cur.next=ListNode(int(num))
            cur=cur.next

        return dummy.next