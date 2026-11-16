class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        hashmap=defaultdict(int)
        res=[]
        for sublist in nums1:
            hashmap[sublist[0]]+=sublist[1]

        for sublist in nums2:
            hashmap[sublist[0]]+=sublist[1]

        hashmap=dict(sorted(hashmap.items()))
        for key in hashmap:
            res.append([key,hashmap[key]])

        return res
