class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        aPointer = 0
        aLen = len(s)
        bPointer = 0
        bLen = len(t)
       
        
        while aPointer < aLen and bPointer < bLen:
            if s[aPointer] == t[bPointer]:
                aPointer += 1

            bPointer += 1
            
       
        return aPointer == aLen

