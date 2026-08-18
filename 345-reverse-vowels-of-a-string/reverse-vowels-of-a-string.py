class Solution:
    def reverseVowels(self, s: str) -> str:
        s=list(s)
        vowels={'a','A','e','E','i','I','o','O','u','U'}
        left,right=0,len(s)-1
        while left<right:
            if s[left] not in vowels:
                left+=1
            elif s[right] not in vowels:
                right-=1
            else:
                s[right],s[left]=s[left],s[right]
                left+=1
                right-=1

        return ''.join(s)