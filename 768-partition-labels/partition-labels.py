class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_idx=dict()

        for idx,char in enumerate(s):
            last_idx[char]=idx

        sizes=[]
        size,end=0,0
        for idx,char in enumerate(s):
            size+=1
            end=max(end,last_idx[char])

            if idx==end:
                sizes.append(size)
                size=0

        return sizes