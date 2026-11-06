from collections import Counter
class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        count_dict=Counter(nums)
        for num in count_dict:
            if count_dict[num]>len(nums)//2:
                return num
        