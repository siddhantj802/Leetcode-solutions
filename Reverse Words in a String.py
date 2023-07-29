class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip()
        tempList = s.split()
        res = ""
        lenS = len(tempList)

        for i in range(lenS):
            res += tempList[lenS - i -1] + " "

        return res.strip()
