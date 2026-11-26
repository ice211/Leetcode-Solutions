class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        row1 = set("qwertyuiop")
        row2 = set("asdfghjkl")
        row3 = set("zxcvbnm")

        res= []
        for each in words:
            ans = set()
            for c in each:
                if c.lower() in row1:
                    ans.add(1)
                elif c.lower() in row2:
                    ans.add(2)
                else:
                    ans.add(3)
            if len(ans) == 1:
                res.append(each)
        return res



            