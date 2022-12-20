class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        ans = []
        n = len(boxes)
        mid = []
        
        for i in range(n):
            if boxes[i] == "1":
                mid.append(i)
        for i in range(n):
            sum = 0
            for j in mid:
                sum = sum + abs(i-j)
            ans.append(sum)

        return ans
