class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
       minOps = 2000
       

       for i in range(len(blocks)-k+1):
           newStr = blocks[i:i+k]
           temp = 0
           
           for ch in newStr:
                if ch == 'W':
                    temp += 1

           minOps = min(temp , minOps)
       return minOps
