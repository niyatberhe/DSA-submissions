class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        res=[]
        nums.sort()
        for idx,val in enumerate(nums):
            if idx>0 and nums[idx-1]==val:
                continue
            l,r=idx+1,len(nums)-1
            while l<r:
                three_sum=val+nums[l]+nums[r]
                if three_sum>0:
                    r-=1
                elif three_sum<0:
                    l+=1
                else:
                    res.append([val,nums[l],nums[r]])
                    l+=1
                    while nums[l]==nums[l-1] and l<r:
                        l+=1
        
        return res