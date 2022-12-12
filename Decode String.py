class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        
        
        for i in range(len(s)):
            if s[i] != "]":
                stack.append(s[i])
            else:
                str1 = ""
                while stack[-1] != "[":
                    
                    str1 = stack.pop() + str1
                stack.pop()
                num = ""

                while stack and stack[-1].isdigit():
                    
                    num = stack.pop() + num

                stack.append(int(num) * str1)
        return "".join(stack)    
            
            
                
