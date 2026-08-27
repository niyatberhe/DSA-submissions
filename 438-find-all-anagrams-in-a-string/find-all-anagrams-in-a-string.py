class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p)>len(s):
            return []

        p_count,s_count={},{}
        for i in range(len(p)):
            p_count[p[i]]=1+p_count.get(p[i],0)
            s_count[s[i]]=1+s_count.get(s[i],0)

        if p_count==s_count:
            result=[0]
        else:
            result=[]

        left=0
        for right in range(len(p),len(s)):
            s_count[s[right]]=1+s_count.get(s[right],0)
            s_count[s[left]]-=1

            if s_count[s[left]]==0:
                s_count.pop(s[left])
            left+=1
            if p_count==s_count:
                result.append(left)

        return result