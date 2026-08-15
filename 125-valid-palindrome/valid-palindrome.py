class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean_s=""
        for i in s:
            if i.isalnum():
                clean_s+=i.lower()

        if clean_s==clean_s[::-1]:
            return True
        else:
            return False
