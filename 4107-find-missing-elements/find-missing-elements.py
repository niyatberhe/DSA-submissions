class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        smallest=min(nums)
        largest=max(nums)

        res=[]

        compare=[x for x in range(smallest,largest+1)]
        for num in compare:
            if num not in nums:
                res.append(num)

        return res