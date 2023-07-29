class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        firstmin = secondmin = float('inf')

        for num in nums:
            if num <= firstmin:
                firstmin = num
            elif num <= secondmin:
                secondmin = num
            else:
                return True
                
        return False

     
