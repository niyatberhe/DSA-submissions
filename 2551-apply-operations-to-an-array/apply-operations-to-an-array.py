class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        zero_arr=[]
        not_zero_arr=[]
        for i in range(len(nums)-1):
            if nums[i]==nums[i+1]:
                nums[i]*=2
                nums[i+1]=0
            else:
                continue

        for j in nums:
            if j==0:
                zero_arr.append(j)
            else:
                not_zero_arr.append(j)

        return not_zero_arr+zero_arr     
