class Solution:
    def interpret(self, command: str) -> str:
        parsed=''
        i=len(command)-1
        while i>=0:
            if command[i]=='G':
                parsed+="G"
                i-=1
            elif command[i]==')' and command[i-1]=='l':
                parsed+='la'
                i-=4
            elif command[i]==')' and command[i-1]=='(':
                parsed+='o'
                i-=2
        
        return parsed[::-1]
