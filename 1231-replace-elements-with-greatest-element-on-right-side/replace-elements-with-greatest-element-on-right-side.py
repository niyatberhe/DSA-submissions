class Solution:
    def replaceElements(self, arr: list[int]) -> list[int]:
        r_max=-1
        for i in range(len(arr)-1,-1,-1):
            new_max=max(r_max,arr[i])
            arr[i]=r_max
            r_max=new_max
            
        return arr