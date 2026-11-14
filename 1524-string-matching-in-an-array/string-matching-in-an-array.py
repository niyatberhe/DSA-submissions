class Solution:
    def stringMatching(self, words: list[str]) -> list[str]:
        res=set()
        for word in words:
            idx=words.index(word)
            rem=words[:idx]+words[idx+1::]

            for i in rem:
                if word in i:
                    res.add(word)

        return list(res)