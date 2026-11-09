class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
            
        s_count=defaultdict(int)
        t_count=defaultdict(int)

        for i in s:
            s_count[i]+=1
        for j in t:
            t_count[j]+=1

        for i in s:
            if s_count[i]!=t_count[i]:
                return False
        
        return True