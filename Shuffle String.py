class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        ans = [""] * len(s)
        
        for i , letter in enumerate(s):
            ans[indices[i]] = letter
            
        return "".join(ans)
