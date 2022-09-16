class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        count = 0
        for word in sentences:
            words = word.split(" ")
            count = max(count , len(words))
            
        return count
            
            
            
            
            
        
