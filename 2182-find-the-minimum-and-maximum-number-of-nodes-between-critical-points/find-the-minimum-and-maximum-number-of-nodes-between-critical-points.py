# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        def is_critical(prev,current,nxt):
            return (prev.val>current.val<nxt.val or prev.val<current.val>nxt.val)
        
        prev,current=head,head.next
        nxt=current.next

        min_dis,max_dis=float("inf"),-1
        prev_crit_ind,first_crit_ind=0,0
        i=1
        while nxt:
            if is_critical(prev,current,nxt):
                if first_crit_ind:
                    max_dis=i-first_crit_ind
                    min_dis=min(min_dis,i-prev_crit_ind)
                else:
                    first_crit_ind=i
                
                prev_crit_ind=i
            prev,current,nxt=current,current.next,nxt.next
            i+=1

        if min_dis==float("inf"):
            min_dis=-1

        return [min_dis,max_dis]