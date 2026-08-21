class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        current_sum=max_sum=sum(nums[:k])

        for i in range (len(nums)-k):
            current_sum+=nums[i+k]-nums[i]
            max_sum=max(max_sum,current_sum)

        return max_sum/k