class Solution:
    def defangIPaddr(self, address: str) -> str:
        ans = ""
        ipadd = address.split(".")
        
        for i in range(len(ipadd) - 1):
            ans = ans + ipadd[i] + "[.]"
        ans = ans + ipadd[-1]
        
        return ans
            
        
     
