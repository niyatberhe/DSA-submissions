class Solution:
    def reverseWords(self, s: str) -> str:
        s_list=s.split(' ')
        res_list=[]
        for word in s_list:
            res_list.append(word[::-1])

        return ' '.join(res_list)