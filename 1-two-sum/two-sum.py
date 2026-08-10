class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for slow in range(len(nums)-1):
            for fast in range(slow+1,len(nums)):
                if nums[fast]+nums[slow]==target:
                    return [slow,fast]
        
        return []