class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        lenA = len(word1)
        lenB = len(word2)
        diff = abs(lenA - lenB)
        temp = ""
        res = ""

        for i in range(max(lenA , lenB) - diff):
            temp = temp + word1[i] + word2[i]

        if lenA == lenB:
            res = temp
        
        elif lenA > lenB:
            res = temp + word1[-diff :]

        else:
            res = temp + word2[-diff:]

        return res
        
