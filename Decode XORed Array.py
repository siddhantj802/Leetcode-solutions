class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        n = len(encoded)
        ans = [0] * (n+1)
        ans[0] = first
        for i in range(n):
            res = encoded[i]^ans[i]
            ans[i+1] = res
            print(ans[i+1])
        return ans
