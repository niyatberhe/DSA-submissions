class Solution:
    def freqAlphabets(self, s: str) -> str:
        decrypt=''
        i=len(s)-1
        while i>=0:
            if s[i]=='#':
                decrypt+=chr(int(s[i-2:i])+96)
                i-=2
            else:
                decrypt+=chr(int(s[i])+96)
            i-=1
        
        return decrypt[::-1]