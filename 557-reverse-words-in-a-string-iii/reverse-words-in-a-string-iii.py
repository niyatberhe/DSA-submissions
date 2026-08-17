class Solution:
    def reverseWords(self, s: str) -> str:
        s=list(s)
        left=0

        for right in range(len(s)):
            if s[right]==" " or right==len(s)-1:
                temp_l,temp_r=left,right-1
                
                if right==len(s)-1:
                    temp_r=right
                while temp_l<temp_r:
                    s[temp_l],s[temp_r]=s[temp_r],s[temp_l]
                    temp_l+=1
                    temp_r-=1
                
                left=right+1

        return ''.join(s)