class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
       lst = list(range(1 , n+1))
       length = len(lst)
       pos = 0


       while length > 1 :
           pos = (pos + k -1)%length
           lst.pop(pos)
           length = length - 1

       return lst[0] 
       
       
        
