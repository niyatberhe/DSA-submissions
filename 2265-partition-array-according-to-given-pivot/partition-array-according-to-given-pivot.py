class Solution:
    def pivotArray(self, nums: list[int], pivot: int) -> list[int]:
        less=[]
        equal=[]
        great=[]

        for num in nums:
            if num<pivot:
                less.append(num)
            elif num>pivot:
                great.append(num)
            else:
                equal.append(num)

        return less+equal+great