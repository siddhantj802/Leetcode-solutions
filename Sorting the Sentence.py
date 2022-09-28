class Solution:
    def sortSentence(self, s: str) -> str:
        ans = []
        s = s.split()
        words = sorted( s, key = lambda item : item[-1] , reverse=False)
        
        for word in words:
            ans.append(word[:-1])
            
        return " ".join(ans)
        
