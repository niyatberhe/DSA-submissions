class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num_str=''
        res=[]
        for digit in digits:
            num_str+=str(digit)

        num_str=str((int(num_str))+1)
        for s in num_str:
            res.append(int(s))

        return res



