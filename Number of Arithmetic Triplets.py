class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        count = 0
        
        for num in nums:
            gtr = num + diff
            lsr = num - diff
            
            if gtr in nums and lsr in nums:
                count += 1
                
        return count
        
