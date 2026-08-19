class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        tot=sum(skill)
        chem=0

        if tot%(len(skill)//2)!=0:
            return -1

        count=Counter(skill)
        target=tot//(len(skill)//2)

        for s in skill:
            if not count[s]:
                continue
            dif=target-s
            if not count[dif]:
                return -1
            chem+=s*dif
            count[s]-=1
            count[dif]-=1

        return chem