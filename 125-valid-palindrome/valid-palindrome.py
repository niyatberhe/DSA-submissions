class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_cleaned=''
        for i in s:
            if i.isalnum():
                s_cleaned+=i
        s_cleaned=s_cleaned.lower()

        l,r=0,len(s_cleaned)-1
        while l<r:
            if s_cleaned[l]!=s_cleaned[r]:
                return False
            l+=1
            r-=1

        return True
