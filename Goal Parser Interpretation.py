class Solution:
    def interpret(self, command: str) -> str:
        mystack = []
        ans = ""
        mydict = {
            'G' : 'G',
            '()': 'o',
             '(al)': "al"
        }
        
        for i in command:
            ans = ans + i
            
            if ans in mydict:
                mystack.append(mydict[ans])
                ans = ""
            
        return ''.join(mystack)
        
