class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        range_set = set()
        for i in ranges:
            for j in range(i[0],i[1]+1):
                if j not in range_set and j in range(left,right+1):
                    range_set.add(j)
            if len(range_set)-1==right-left:
                return True
        return False