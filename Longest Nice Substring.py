class Solution:
    def longestNiceSubstring(self, s: str) -> str:

        if len(s) < 2:
            return ""

        def check(substr):
            for ch in substr:
                if ch.upper() not in substr or ch.lower() not in substr:
                    return False

            return True

        maxLength = 0
        largeSubstr = ""

        for i in range(len(s)):
            for j in range(i+1 , len(s)+1):

                if check(s[i:j]) and j-i > maxLength:
                    maxLength = j-i
                    largeSubstr = s[i:j]
        return largeSubstr
