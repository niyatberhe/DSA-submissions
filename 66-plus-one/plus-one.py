class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        dig_str=[str(num) for num in digits]
        s=''.join(dig_str)
        s=str(int(s)+1)
        
        return [int(i) for i in s]