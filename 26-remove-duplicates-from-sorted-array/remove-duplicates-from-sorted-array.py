class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        l=0
        seen=set()

        for r in range(len(nums)):
            if nums[r] not in seen:
                seen.add(nums[r])
                nums[l]=nums[r]
                l+=1

        return l