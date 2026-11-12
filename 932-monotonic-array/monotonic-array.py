class Solution:
    def isMonotonic(self, nums: list[int]) -> bool:
        if nums==sorted(nums) or nums[::-1]==sorted(nums):
            return True
        else:
            return False