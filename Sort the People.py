from functools import reduce
class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        tallest = zip(names , heights)
        tallest = sorted(tallest , key = lambda x: x[1])
        
        ans = []
        
        for tall in tallest:
            ans.append(tall[:-1])
        ans = reduce(lambda a,b:a+b, ans)
        
        return ans[::-1]
    
        
