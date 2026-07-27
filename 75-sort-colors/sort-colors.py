class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        color_count={
            "red":0,
            "white":0,
            "blue":0    
        }

        for i in range(len(nums)):
            if nums[i]==0:
                color_count["red"]+=1
            elif nums[i]==1:
                color_count["white"]+=1
            elif nums[i]==2:
                color_count["blue"]+=1
            
        zeros,ones,twos=color_count["red"],color_count["white"],color_count["blue"]
        for i in range(zeros):
            nums[i]=0
        for i in range(ones):
            nums[zeros+i]=1
        for i in range(twos):
            nums[zeros+ones+i]=2
            

        