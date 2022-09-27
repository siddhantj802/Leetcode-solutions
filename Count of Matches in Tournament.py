class Solution:
    def numberOfMatches(self, n: int) -> int:
        def nom(x):
            
            if x==1:
                return 0
            if x%2==0:
                return x//2+ nom(x//2)
            else:
                return x//2+ nom(x//2+1)
        return nom(n)
