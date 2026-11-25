class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        for l in range(len(numbers)-1):
            if target-numbers[l] in numbers[l+1::]:
                r=l+1
                while r<len(numbers):
                    if numbers[r]==target-numbers[l]:
                        return [l+1,r+1]
                    r+=1
            else:
                continue
            