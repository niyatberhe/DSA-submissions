class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        lst_1=list(words[0])
        for word in words:
            lst_2=[]
            for char in word:
                if char in lst_1:
                    lst_2.append(char)
                    lst_1.remove(char)
            
            lst_1=lst_2

        return lst_1
