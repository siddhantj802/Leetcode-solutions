class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
      res = 0
      rowLen = len(bank)
      colLen = len(bank[0])
      count = 0
      lastCount = 0

      for i in bank:
          count = 0
          for j in i:
              if j == "1":
                  count += 1
          if count != 0:
               res = res + count * lastCount
               lastCount = count
        
      return res
