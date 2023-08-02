class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = "aeoiu"
        maxCount = 0

        curWindow = s[:k]
        currCount = sum(1 for char in curWindow if char in vowels)
        maxCount = max(currCount , maxCount)

        for i in range(k , len(s)):
            if s[i-k] in vowels:
                currCount -= 1

            if s[i] in vowels:
                currCount += 1

            maxCount = max(maxCount , currCount)

        return maxCount

        
        


