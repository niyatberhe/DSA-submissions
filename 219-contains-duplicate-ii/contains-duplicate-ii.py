class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        left=0
        window_set=set()

        for right in range(len(nums)):
            if right-left>k:
                window_set.remove(nums[left])
                left+=1
            if nums[right] in window_set:
                return True
            window_set.add(nums[right])

        return False