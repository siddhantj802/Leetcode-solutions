class Solution:
    def maxArea(self, height: List[int]) -> int:
        aPointer = 0
        bPointer = len(height) - 1
        area = 0

        while aPointer < bPointer:
            tempArea = min(height[aPointer] , height[bPointer]) * abs(aPointer - bPointer)
            area = max(area , tempArea)

            if height[aPointer] < height[bPointer]:
               aPointer += 1
            else:
             bPointer -= 1

        return area
            
