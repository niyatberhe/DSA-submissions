class Solution:
    def validPalindrome(self, s: str) -> bool:
        left,right=0,len(s)-1

        while left<right:
            if s[left]!=s[right]:
                left_skipped,right_skipped=s[left+1:right+1],s[left:right]
                return (left_skipped==left_skipped[::-1] or right_skipped==right_skipped[::-1])
            
            left+=1
            right-=1
        
        return True