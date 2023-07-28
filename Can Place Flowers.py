class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        lenA = len(flowerbed)
        cnt = 0

        if lenA < n:
            return False

        for i in range(lenA):
            if flowerbed[i]==0:
                if ((i==0 or  flowerbed[i-1]==0) and (i == lenA-1 or flowerbed[i+1]==0 )):
                    flowerbed[i] = 1
                    cnt += 1

                if cnt >= n:
                    return True
        return cnt >= n
        
