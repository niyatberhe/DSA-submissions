class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        squares=[]
        for num in nums:
            squares.append(num**2)

        squares.sort()
        return squares