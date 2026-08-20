from collections import defaultdict
class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        count=defaultdict(int)
        ops=0
        
        for num in nums:
            if count[k-num]>0:
                ops+=1
                count[k-num]-=1
            else:
                count[num]+=1

        return ops