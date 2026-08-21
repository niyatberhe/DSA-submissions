class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        letter_set=set()
        result=0
        left=0

        for right in range(len(s)):
            while s[right] in letter_set:
                letter_set.remove(s[left])
                left+=1

            letter_set.add(s[right])
            result=max(result,right-left+1)

        return result