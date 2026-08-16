class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        diff=[]
        for i in range(len(nums)-k+1):
            diff.append(nums[i+k-1]-nums[i])
        
        return min(diff)