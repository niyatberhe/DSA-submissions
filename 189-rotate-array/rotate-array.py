class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def helper(arr,l,r):
            while l<r:
                arr[l],arr[r]=arr[r],arr[l]
                l+=1
                r-=1
        k=k%len(nums)
        helper(nums,0,len(nums)-1)
        helper(nums,0,k-1)
        helper(nums,k,len(nums)-1)