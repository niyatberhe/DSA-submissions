class Solution:
    def compress(self, chars: list[str]) -> int:
        insert,i=0,0
        while i<len(chars):
            group=1
            while (group+i)<len(chars) and chars[group+i]==chars[i]:
                group+=1
            chars[insert]=chars[i]
            insert+=1
            if group>1:
                count=str(group)
                chars[insert:insert+len(count)]=list(count)
                insert+=len(count)
            i+=group

        return insert