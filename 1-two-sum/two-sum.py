class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        mapp={}
        for idx, num in enumerate(nums):
            if target-num in mapp:
                return [mapp[target-num],idx]
            mapp[num]=idx
