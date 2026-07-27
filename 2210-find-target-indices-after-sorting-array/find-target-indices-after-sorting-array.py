class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        indices=[]
        nums.sort()
        for i in range(0, len(nums)):
            if nums[i]==target:
                if i not in indices:
                    indices.append(i)

        return indices