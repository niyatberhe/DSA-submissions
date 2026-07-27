class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        for n in range(len(heights)):
            for m in range(len(heights)-n-1):
                if heights[m]<heights[m+1]:
                    heights[m],heights[m+1]=heights[m+1],heights[m]
                    names[m],names[m+1]=names[m+1],names[m]
                else:
                    continue
        
        return names
        