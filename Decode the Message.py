
class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        alphabet = list(string.ascii_lowercase)
        
        ans = ""
        keydict = {}
        
        count = 0
        
        for letter in key:
            if letter!= " " and letter not in keydict:
                keydict[letter] = alphabet[count]
                count += 1
                
            if len(keydict) == 26:
                break
        keydict[" "] = " "    
        for msg in message:
            ans = ans +  keydict[msg] 
            
        return ans
                
            
            
        
