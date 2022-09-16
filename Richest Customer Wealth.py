class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        total = 0
        for i in accounts:
            temp = 0
            for j in i:
                temp += j
                
            total = max(temp , total)
            
        return total
            
                
                
        
