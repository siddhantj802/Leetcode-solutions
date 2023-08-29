class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        lens = len(s)
        
        count = 0

        for i in range(lens-2):
            temp = ""
            for k in range(i , i+3):
                if s[k] in temp:
                    break
                else:
                    temp += s[k]
            else:
                count += 1

        return count
       
