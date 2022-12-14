class Solution:
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
       res = []
       for circle in queries:
           count = 0
           for point in points:
               if (circle[0]-point[0]) ** 2 + (circle[1]-point[1]) ** 2 <= circle[2] ** 2:
                   count += 1
           res.append(count)
       return res
       
