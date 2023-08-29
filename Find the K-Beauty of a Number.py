class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        count = 0
        res = str(num)
        
        for i in range(len(res)-k+1):
            nums = int(res[i:i+k])
            print(nums)
            
            if nums != 0 and num % nums == 0:
                count += 1

        
        return count
