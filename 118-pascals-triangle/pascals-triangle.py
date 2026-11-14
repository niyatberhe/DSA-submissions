class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        res=[[1]]
        for i in range(numRows-1):
            above=[0]+res[-1]+[0]
            cur=[]
            for j in range(len(res[-1])+1):
                cur.append(above[j]+above[j+1])

            res.append(cur)

        return res