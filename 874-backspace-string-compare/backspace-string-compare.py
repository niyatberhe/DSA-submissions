class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s_arr=[]
        t_arr=[]

        for i in s:
            if i=='#':
                if s_arr:
                    s_arr.pop()
                continue
            else:
                s_arr.append(i)

        for i in t:
            if i=='#':
                if t_arr:
                    t_arr.pop()
                continue
            else:
                t_arr.append(i)

        if ''.join(s_arr)==''.join(t_arr):
            return True
        return False