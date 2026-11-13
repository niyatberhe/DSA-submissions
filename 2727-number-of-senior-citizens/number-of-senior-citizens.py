class Solution:
    def countSeniors(self, details: List[str]) -> int:
        res_count=0
        for detail in details:
            if int(detail[-4:-2])>60:
                res_count+=1

        return res_count