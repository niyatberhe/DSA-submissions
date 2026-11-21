class Solution:
    def validPalindrome(self, s: str) -> bool:
        def helperPalind(string):
            l,r=0,len(string)-1
            while l<r:
                if string[l]!=string[r]:
                    return False
                l+=1
                r-=1
            return True

        l,r=0,len(s)-1
        while l<r:
            if s[l]!=s[r]:
                return helperPalind(s[l+1:r+1]) or helperPalind(s[l:r])
            l+=1
            r-=1
        return True