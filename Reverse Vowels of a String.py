class Solution:
    def reverseVowels(self, s: str) -> str:
        lenS = len(s)
        vowel = "aeiouAEIOU"
        lookup = ""
        cnt = -1
        
        res = ""

        for i in range(lenS):
            if s[i] in vowel:
                lookup += s[i]
                cnt += 1
                

       # length = len(lookup)
       #print(length)
        for i in s:
            if i not in vowel:
                res = res + i
            elif i in vowel and cnt > -1:
                res = res + lookup[cnt]
                cnt -= 1 

        return res
        
