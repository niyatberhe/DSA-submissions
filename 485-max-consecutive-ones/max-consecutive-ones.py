class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        l, res=0,0

        for r,num in enumerate(nums):
            if num==0:
                l=r+1
            res=max(res,r-l+1)

        return res