from collections import defaultdict
class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        counter=defaultdict(int)
        for num in nums:
            counter[num]+=1

        for num in nums:
            if counter[num]==1:
                return num