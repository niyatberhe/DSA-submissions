class Solution:
    def isValid(self, s: str) -> bool:
        open_stk=[]
        close_2_open={
            ')':'(',
            ']':'[',
            '}':'{'
        }
        for char in s:
            if char in close_2_open:
                if open_stk and open_stk[-1]==close_2_open[char]:
                    open_stk.pop()
                else:
                    return False
            else:
                open_stk.append(char)

        if not open_stk:
            return True
        else:
            return False
                
        