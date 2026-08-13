class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        freq=dict()
        for num in nums:
            if num in freq:
                freq[num]+=1
            else:
                freq[num]=1

        for num in freq:
            if freq[num]>=2:
                return True
                break
        return False